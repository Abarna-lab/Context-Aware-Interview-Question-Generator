# Context-Aware-Interview-Question-Generator
This project generates context-aware interview questions from uploaded documents using Google's Gemini AI. It supports PDF, DOCX, and TXT files, extracting key concepts and formulating structured questions. 

## Installation & Setup  

### 1. Prerequisites  
- Python 3.8+  
- API key for **Google Gemini AI**  

### 2. Install Dependencies  
Run the following command to install required packages:  
```sh
pip install -r requirements.txt
```
### 3.Set Up Environment Variables
Create a ```.env ```file and add your API key (inside the quotes): 
```sh
GEMINI_API_KEY="your_api_key_here"
```

### 5.Run the Application
Once the environment variables are set, launch the Streamlit interface:
```sh 
streamlit run InterviewDeskSD.py
 ```

### 6.How to Test with a New Document
- Open the application in your browser.
- Click Upload File and select a PDF, DOCX, or TXT document.
- The system extracts text and generates 10–15 interview questions.
- Review the questions displayed on the interface.






