import streamlit as st
import inspect
import openai

# Monkey patch inspect.getargspec to use inspect.getfullargspec if it's not available
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

# Set up the Streamlit app
st.title("AI Search Assistant 🤖")
st.caption("This app allows you to search the web using AI")

# Get OpenAI API key from the user
openai_access_token = st.text_input("OpenAI API Key", type="password")

# Check if the API key is provided
if openai_access_token:
    # Initialize OpenAI with the provided API key
    openai.api_key = openai_access_token

    # Example: Define a function to perform a search using OpenAI's GPT model
    def search_with_openai(prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content'].strip()

    # Get search query from the user
    search_query = st.text_input("Enter your search query")

    # Button to trigger search
    if st.button("Search"):
        if search_query:
            # Perform the search using OpenAI
            result = search_with_openai(search_query)
            # Display the result
            st.write("Search Results:")
            st.write(result)
        else:
            st.write("Please enter a search query.")
else:
    st.write("Please enter your OpenAI API Key.")
