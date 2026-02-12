import streamlit as st
import pdfplumber

st.title("Registration SOP 5.1 – 5.11 Chatbot")

# Load PDF
def load_pdf():
    text = ""
    with pdfplumber.open("sop.pdf") as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

sop_text = load_pdf().lower()

question = st.text_input("Ask your question from SOP")

if question:
    question = question.lower()
    if question in sop_text:
        start = sop_text.find(question)
        answer = sop_text[start:start+800]  # show limited content only
        st.success(answer)
    else:
        st.error("Not available in SOP 5.1 to 5.11")
