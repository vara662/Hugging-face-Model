import streamlit as st
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


# -----------------------------
# LOAD HUGGING FACE TOKEN
# -----------------------------

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")


# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="Nexa AI",
    page_icon="AI",
    layout="centered"
)


# -----------------------------
# APP HEADER
# -----------------------------

st.title("Nexa AI")
st.caption("Ask • Learn • Create • Explore")


# -----------------------------
# CHECK TOKEN
# -----------------------------

if not HF_TOKEN:
    st.error("Hugging Face token not found!")
    st.info("Please check your .env file.")
    st.stop()


# -----------------------------
# CREATE AI CLIENT
# -----------------------------

client = InferenceClient(
    api_key=HF_TOKEN,
    provider="groq"
)


# -----------------------------
# CHAT MEMORY
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.title("Nexa AI")

    st.caption("Your Intelligent AI Assistant")

    st.divider()

    if st.button("Clear Chat"):

        st.session_state.messages = []

        st.rerun()

    st.divider()

    st.write("### Features")

    st.write("General Questions")
    st.write("Programming Help")
    st.write("Study Assistance")
    st.write("Project Ideas")
    st.write("Tamil & English Support")

    st.divider()

    st.success("AI Online")


# -----------------------------
# WELCOME SCREEN
# -----------------------------

if len(st.session_state.messages) == 0:

    st.info("Hello! I'm Nexa AI. How can I help you today?")

    st.write("### Try asking:")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Explain AI"):

            st.session_state.messages.append({
                "role": "user",
                "content": "Explain Artificial Intelligence in simple words."
            })

            st.rerun()

        if st.button("Coding Help"):

            st.session_state.messages.append({
                "role": "user",
                "content": "Explain Python programming for beginners."
            })

            st.rerun()

    with col2:

        if st.button("Study Tips"):

            st.session_state.messages.append({
                "role": "user",
                "content": "Give me effective study tips."
            })

            st.rerun()

        if st.button("Project Ideas"):

            st.session_state.messages.append({
                "role": "user",
                "content": "Give me some innovative AI project ideas."
            })

            st.rerun()


# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# -----------------------------
# CHAT INPUT
# -----------------------------

user_input = st.chat_input(
    "Ask Nexa AI anything..."
)


# -----------------------------
# GENERATE RESPONSE
# -----------------------------

if user_input:

    # Save user message

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })


    # Display user message

    with st.chat_message("user"):

        st.write(user_input)


    # Display AI response

    with st.chat_message("assistant"):

        try:

            with st.spinner("Nexa AI is thinking..."):

                response = client.chat.completions.create(

                    model="openai/gpt-oss-120b",

                    messages=[

                        {
                            "role": "system",
                            "content": """
You are Nexa AI, a helpful, friendly, and intelligent AI assistant.

You can answer questions about:
- Education
- Programming
- Artificial Intelligence
- Technology
- General Knowledge
- Creative ideas
- Daily life questions

If the user speaks Tamil or Tanglish,
reply naturally in Tamil or Tanglish.

If the user speaks English,
reply in English.

Give clear and easy-to-understand answers.

For programming questions,
explain step by step with examples when needed.

Be helpful, friendly, and concise.
"""
                        }

                    ] + st.session_state.messages,

                    max_tokens=1024,

                    temperature=0.7

                )


                # GET AI ANSWER

                answer = response.choices[0].message.content


                # DISPLAY ANSWER

                st.write(answer)


                # SAVE AI ANSWER

                st.session_state.messages.append({

                    "role": "assistant",

                    "content": answer

                })


        except Exception as e:

            st.error("AI Connection Error")

            st.code(str(e))