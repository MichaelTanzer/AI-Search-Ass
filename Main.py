import streamlit as st
import asyncio
from openai import AsyncOpenAI

# Function to perform asynchronous search using OpenAI's GPT model
async def search_with_openai(api_key, prompt):
    client = AsyncOpenAI(api_key=api_key)
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

# Function to run the async function in the Streamlit context
def run_async_func(api_key, prompt):
    return asyncio.run(search_with_openai(api_key, prompt))

# Set up the Streamlit app
st.title("AI Search Assistant 🤖")
st.caption("This app allows you to search the web using AI")

# Get OpenAI API key from the user
openai_access_token = st.text_input("OpenAI API Key", type="password")

# Check if the API key is provided
if openai_access_token:
    # Get search query from the user
    search_query = st.text_input("Enter your search query")

    # Button to trigger search
    if st.button("Search"):
        if search_query:
            # Perform the search using OpenAI
            result = run_async_func(openai_access_token, search_query)
            # Display the result
            st.write("Search Results:")
            st.write(result)
        else:
            st.write("Please enter a search query.")
else:
    st.write("Please enter your OpenAI API Key.")
