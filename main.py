import openai
import streamlit as st
from PyPDF2 import PdfReader

# Set up your OpenAI API credentials
openai.api_key = st.secrets['OPENAI_API_KEY']

# Load the PDF file
pdf_file = open('didx.pdf', 'rb')
pdf_reader = PdfReader(pdf_file)
pdf_text = ''
for page in pdf_reader.pages:
    pdf_text += page.extract_text()

# Define a function to generate a response using OpenAI GPT-3
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Define the Streamlit app
def app():
    user_input = st.text_input("Your question about DIDX:")
    if user_input:
        prompt = f"You: {user_input}\nAssistant: {pdf_text}"
        response = generate_response(prompt)
        st.text_area("Assistant's response:", value=response)

# Run the Streamlit app
if __name__ == '__main__':
    app()
