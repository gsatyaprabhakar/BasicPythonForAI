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
from google.genai import types

load_dotenv()
client = genai.Client()

SYSTEM_INSTRUCTION = (
    "You are a witty movie buff who loves making puns. "
    "Use the user's taste history to recommend movies and explain your choices "
    "when they ask why."
)


def reset_chat():
    st.session_state.conversation = []


def add_message(role, text):
    st.session_state.conversation.append({
        "role": role,
        "parts": [{"text": text}],
    })


st.title("💬 A movie-recommendation buddy")

if "conversation" not in st.session_state:
    reset_chat()

for message in st.session_state.conversation:
    role = "user" if message["role"] == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message["parts"][0]["text"])

user_input = st.chat_input("Say your interest...")

if user_input and user_input.strip():
    add_message("user", user_input)
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        config = types.GenerateContentConfig(system_instruction=SYSTEM_INSTRUCTION)
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=st.session_state.conversation,
            config=config,
        )
        reply = response.text or "I couldn't think of a good recommendation right now."
    except Exception as e:
        reply = f"Sorry, something went wrong: {e}"

    add_message("model", reply)
    with st.chat_message("assistant"):
        st.markdown(reply)

if st.sidebar.button("🗑️ Clear chat"):
    reset_chat()
    st.rerun()
