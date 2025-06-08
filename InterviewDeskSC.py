import streamlit as st
import fitz  # PyMuPDF for PDF parsing
import google.generativeai as genai
import docx
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv('.env')

# Configure Gemini API
MY_API_KEY = os.getenv('GEMINI_API_KEY')

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# Function to extract text from DOCX
def extract_text_from_docx(uploaded_file):
    doc = docx.Document(uploaded_file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Function to extract text from TXT
def extract_text_from_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8")

# Function to determine file type and extract text accordingly
def extract_text(uploaded_file):
    file_type = uploaded_file.name.split(".")[-1].lower()
    
    if file_type == "pdf":
        return extract_text_from_pdf(uploaded_file)
    elif file_type == "docx":
        return extract_text_from_docx(uploaded_file)
    elif file_type == "txt":
        return extract_text_from_txt(uploaded_file)
    else:
        return "Unsupported file format."

# Function to generate interview questions using Gemini AI
def generate_questions(document_text):
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f'''
**Context:**  
You are an AI-powered assistant designed to generate interview questions based on a given document. Your goal is to create **clear, direct, and easy-to-understand** questions that assess key concepts.

**Document Content:**  
{document_text}

**Your Task:**  
- Generate **10–15 interview questions** that accurately reflect the document's core themes.  
- Keep the questions **simple, direct, and readable** for a wide audience.  
- Ensure coverage across major topics without making questions overly complex.  
- Avoid explicitly listing key concepts but ensure questions naturally test comprehension.  

**Instructions for the Model:**  
1. Questions must be **clear and straightforward**, avoiding unnecessary complexity.  
2. Ensure **broad coverage** so all major sections of the document are addressed.  
3. **Avoid categorizing questions** by difficulty—just provide well-structured questions.  
4. Ensure **concise phrasing** while keeping the meaning intact.  
5. Questions should be **informative** but not overly technical unless required by the document's content.  

'''
    response = model.generate_content(prompt)
    return response.text if response else "No questions generated."

# Streamlit UI
st.title("AI-Powered Interview Question Generator 🎓")

uploaded_file = st.file_uploader("Upload a PDF, DOCX,TXT file or PPTX File", type=["pdf", "docx", "txt"])

if uploaded_file:
    st.success("File uploaded successfully!")

    # Extract document text
    document_text = extract_text(uploaded_file)
    
    if document_text == "Unsupported file format.":
        st.error("Please upload a valid PDF, DOCX or TXT file.")
    else:
        # Generate interview questions
        st.subheader("Generated Interview Questions:")
        questions = generate_questions(document_text)
        st.write(questions)
