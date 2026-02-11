import streamlit as st
import pdfplumber

st.set_page_config(page_title="VPro SOP Bot", page_icon="📘")

st.title("VPro SOP Chatbot (Sections 5.1 – 5.11 Only)")
st.write("Ask questions only from Sections 5.1 to 5.11.")

@st.cache_resource
def load_sop():
    text = ""
    with pdfplumber.open("sop.pdf") as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
    return text

sop_text = load_sop()

question = st.text_input("Enter your question:")

if question:
    results = []
    for line in sop_text.split("\n"):
        if question.lower() in line.lower():
            results.append(line)

    if results:
        st.success("Answer from SOP:")
        for r in results:
            st.write(r)
    else:
        st.error("Not found in SOP Sections 5.1–5.11.")
