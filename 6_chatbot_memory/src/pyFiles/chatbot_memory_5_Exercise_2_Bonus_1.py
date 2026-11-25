'''
## 🏋️ Exercise: A movie-recommendation buddy that remembers your taste

Build a chatbot that uses memory to give *personalized* answers.

1. Start a fresh `conversation = []` and reuse the `chat()` function from above.
2. Have this conversation, one `chat()` call at a time:
   - `"I love sci-fi and thrillers, but I can't stand horror movies."`
   - `"Suggest me a movie to watch tonight."`
3. Check that its suggestion respects what you said earlier (sci-fi/thriller, **not** horror). That's memory doing its job!
4. Then ask: `"Why did you pick that one?"` — it should explain using your stated taste.

**Bonus 1:** add a `reset()` function that empties the conversation list — a "new chat" button.

**Bonus 2:** give your bot a personality. Pass a `config` to `generate_content`:
```python
from google.genai import types
config = types.GenerateContentConfig(
    system_instruction="You are a witty movie buff who loves making puns."
)
# ...add config=config to the generate_content call
```

Have fun — try to make it forget on purpose by clearing the list, then watch it ask "who are you?" all over again. 😄
'''

import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

st.title("💬 A movie-recommendation buddy")

# The conversation list IS the memory. We keep it in st.session_state so it
# survives Streamlit's reruns (otherwise it would reset on every message).
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Show the whole conversation so far
for message in st.session_state.conversation:
    role = "user" if message["role"] == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message["parts"][0]["text"])

# Take new input from the user
user_input = st.chat_input("Say your interest...")

if user_input:
    # 1. add the user's message to memory and show it
    st.session_state.conversation.append({"role": "user", "parts": [{"text": user_input}]})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 2. send the ENTIRE conversation so the model has context
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=st.session_state.conversation
        )
        reply = response.text
    except Exception as e:
        reply = f"Sorry, something went wrong: {e}"

    # 3. add the AI's reply to memory and show it
    st.session_state.conversation.append({"role": "model", "parts": [{"text": reply}]})
    with st.chat_message("assistant"):
        st.markdown(reply)

# A simple "new chat" button that wipes the memory
if st.sidebar.button("🗑️ Clear chat"):
    st.session_state.conversation = []
    st.rerun()
