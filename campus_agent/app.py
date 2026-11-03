"""
minimalapp.py - Starting point for Lab 3

This is a basic Streamlit chat interface without ADK integration.
Students will modify this file to add agent connectivity.

Author: Zaid Abdulrahim
Course: AI Programming
"""
from dotenv import load_dotenv
import uuid
import streamlit as st
import asyncio
from google.genai import errors
from agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
load_dotenv()
# Page configuration - MUST be the first Streamlit command
st.set_page_config(
    page_title="Campus Resource Assistant",
    page_icon="🏛️",
    layout="centered"
)

# Title and introduction
st.title("🏛️ Campus Resource Assistant")

st.markdown("""
Ask me about campus resources like the library, tutoring center, 
advising office, or financial aid. I can help you find hours, 
locations, and contact information.
""")
# Create a session service for the AI agent
@st.cache_resource
def get_session_service():
    return InMemorySessionService()

session_service = get_session_service()
# Connect Streamlit to the existing AI agent
runner = Runner(
    agent=root_agent,
    app_name="campus_resource_app",
    session_service=session_service
)
# Create a unique session for this user
if "adk_session_id" not in st.session_state:
    st.session_state.adk_session_id = f"student_{uuid.uuid4().hex}"
if "adk_session_created" not in st.session_state:
    asyncio.run(
        session_service.create_session(
            app_name="campus_resource_app",
            user_id="student",
            session_id=st.session_state.adk_session_id
        )
    )
    st.session_state.adk_session_created = True

async def ask_agent(question):
    message = types.Content(
        role="user",
        parts=[types.Part(text=question)]
    )

    max_attempts = 3

    for attempt in range(max_attempts):
        answer = ""

        try:
            async for event in runner.run_async(
                user_id="student",
                session_id=st.session_state.adk_session_id,
                new_message=message
            ):
                if event.is_final_response() and event.content:
                    for part in event.content.parts:
                        if part.text:
                            answer += part.text

            return answer

        except errors.ServerError as e:
            if e.code not in (500, 502, 503, 504):
                raise

            if attempt == max_attempts - 1:
                raise

            wait_time = 2 ** (attempt + 1)
            print(
                f"Temporary Gemini error {e.code}. "
                f"Retrying in {wait_time} seconds..."
            )
            await asyncio.sleep(wait_time)

# Initialize chat history in session state
# This persists across Streamlit's reruns
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all messages from chat history
# Each message is a dict with 'role' and 'content' keys
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input using walrus operator for assignment + condition check
if prompt := st.chat_input("Ask about campus resources..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message immediately (Streamlit doesn't auto-show input)
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        response = asyncio.run(ask_agent(prompt))
    except Exception as e:
        response = (
            "Sorry, the AI service is temporarily unavailable. "
            "Please try again in a moment."
        )
        print(f"Agent error: {type(e).__name__}: {e}")

     
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Clear conversation button
if st.button("Clear Conversation"):
    st.session_state.messages = []
    st.rerun()
