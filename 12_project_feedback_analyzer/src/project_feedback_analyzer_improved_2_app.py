"""
The frontend: a Streamlit dashboard for a business owner.

Paste customer reviews (one per line), click Analyze, and see the results.
This app does NOT call Gemini directly. It calls OUR OWN backend (api.py),
exactly the way we called external APIs in Lesson 9.

Run it (in a SECOND terminal, while api.py is also running):
    uv run streamlit run app.py
"""

from collections import Counter
from pathlib import Path

import altair as alt
import requests
import streamlit as st

# Our own database code, kept in a separate file (database.py).
from project_feedback_analyzer_improved_1_database import init_db, save_results, load_history, DB_FILE

# The address of our own backend service.
API_URL = "http://127.0.0.1:8000/analyze"

# Make sure the table exists before the app uses it.
init_db()

st.title("📝 Customer Feedback Analyzer")
st.write("Paste your customer reviews below, one review per line.")

left_column, right_column = st.columns(2)

with left_column:
    if st.button("Load sample reviews"):
        sample_reviews_path = Path(__file__).resolve().parent.parent / "sample_reviews.txt"
        st.session_state.reviews_text = sample_reviews_path.read_text(encoding="utf-8")

with right_column:
    uploaded_file = st.file_uploader("Browse for a reviews file", type=["txt"])

if uploaded_file is not None:
    upload_id = f"{uploaded_file.name}:{uploaded_file.size}"
    if st.session_state.get("_loaded_upload_id") != upload_id:
        try:
            st.session_state.reviews_text = uploaded_file.getvalue().decode("utf-8")
            st.session_state._loaded_upload_id = upload_id
        except UnicodeDecodeError:
            st.warning("Please choose a UTF-8 encoded text file.")

reviews_text = st.text_area("Reviews", height=200, key="reviews_text")

if st.button("Analyze"):
    # Split the text box into separate reviews, ignoring blank lines.
    reviews = [line.strip() for line in reviews_text.split("\n") if line.strip()]

    if not reviews:
        st.warning("Please paste at least one review.")
    else:
        results = []
        # Go through each review and ask our backend to analyze it.
        for review in reviews:
            try:
                response = requests.post(API_URL, json={"text": review})
                data = response.json()
                results.append({
                    "review": review,
                    "label": data["label"],
                    "score": data["score"],
                    "theme": data["theme"],
                })
            except Exception:
                # One bad review should not stop the whole batch.
                results.append({
                    "review": review,
                    "label": "error",
                    "score": 0,
                    "theme": "error",
                })

        # Save results in session_state so they survive button clicks.
        st.session_state.results = results

# Show the results if we have any.
if "results" in st.session_state:
    results = st.session_state.results

    st.subheader("Results")
    review_filter = st.selectbox("Show reviews", ["negative", "positive", "all"])
    visible_results = (
        results
        if review_filter == "all"
        else [result for result in results if result["label"] == "positive"]
        if review_filter == "positive"
        else [result for result in results if result["label"] == "negative"]
    )
    st.dataframe(visible_results)

    # ---- A simple summary for the business owner ----
    scores = [r["score"] for r in results if r["label"] != "error"]
    positive = [r for r in results if r["label"] == "positive"]
    themes = [r["theme"] for r in results if r["theme"] != "error"]

    st.subheader("Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Reviews", len(results))
    if scores:
        col2.metric("Average score", round(sum(scores) / len(scores), 1))
        col3.metric("% Positive", f"{round(len(positive) / len(results) * 100)}%")

    if themes:
        # Counter tells us which theme appears most often.
        top_theme = Counter(themes).most_common(1)[0][0]
        st.info(f"Customers talk most about: **{top_theme}**")

    # ---- Save the full report to the database (Lesson 12) ----
    if st.button("💾 Save to database"):
        save_results(results)
        st.success(f"Saved {len(results)} reviews to {DB_FILE}")

# ---- Show everything we have ever saved (reads from the database) ----
with st.expander("📚 Saved history (all reviews in the database)"):
    history = load_history()
    if history:
        st.write(f"Total saved so far: {len(history)}")
        st.dataframe(
            [{"review": r[0], "label": r[1], "score": r[2], "theme": r[3]} for r in history]
        )
    else:
        st.write("Nothing saved yet. Analyze some reviews and click Save.")

with st.expander("View Reviews As Chart"):
    history = load_history()
    if history:
        theme_counts = Counter(r[3] for r in history if r[3] != "error")
        if theme_counts:
            st.bar_chart(theme_counts)
            pie_chart = alt.Chart(
                alt.Data(
                    values=[
                        {"theme": theme, "reviews": count}
                        for theme, count in theme_counts.items()
                    ]
                )
            ).mark_arc().encode(
                theta=alt.Theta("reviews:Q"),
                color=alt.Color("theme:N", legend=alt.Legend(title="Theme")),
                tooltip=[
                    alt.Tooltip("theme:N", title="Theme"),
                    alt.Tooltip("reviews:Q", title="Reviews"),
                ],
            )
            st.altair_chart(pie_chart, use_container_width=True)
        else:
            st.write("No theme data available yet.")
    else:
        st.write("Nothing saved yet.")
