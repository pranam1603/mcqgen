# AI MCQ Generator

An AI-powered web application that automatically generates Multiple Choice Questions (MCQs) from PDF and TXT documents using Large Language Models (LLMs), LangChain, and Streamlit.

## 🚀 Live Demo

Add your Streamlit deployment URL here:

https://mcq-generator-app.streamlit.app/

---

## ✨ Features

- Upload PDF or TXT documents
- Generate custom MCQs from document content
- Select the number of questions
- Specify the subject area
- Choose the complexity level of questions
- Automatic quiz evaluation and review
- Interactive Streamlit user interface
- Powered by OpenAI and LangChain

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### AI & LLM
- OpenAI API
- LangChain
- LangChain Expression Language (LCEL)

### Backend
- Python

### Data Processing
- PyPDF2
- JSON

### Deployment
- Streamlit Community Cloud

---

## 📌 Project Architecture

1. User uploads a PDF or TXT file.
2. The application extracts text from the document.
3. LangChain sends the content to the OpenAI model.
4. The model generates MCQs based on:
   - Subject
   - Number of questions
   - Complexity level
5. A second LLM chain evaluates the generated quiz.
6. Results are displayed in a structured table.

---

## 📂 Project Structure

```text
mcqgen/
│
├── StreamLitApp.py
├── Response.json
├── requirements.txt
│
└── src/
    └── mcqgenrator/
        ├── __init__.py
        ├── MCQGenerator.py
        ├── utils.py
        └── logger.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/pranam@1603/mcqgen.git
cd mcqgen
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_KEY=your_openai_api_key
```

---

## ▶️ Run Locally

```bash
streamlit run StreamLitApp.py
```

---

## 🎯 Learning Outcomes

This project helped me gain practical experience in:

- Prompt Engineering
- LangChain Runnables (LCEL)
- OpenAI API Integration
- PDF Processing
- Streamlit Development
- Cloud Deployment
- Production Debugging

---

## 🔮 Future Improvements

- Support DOCX files
- Export quizzes to PDF
- Difficulty-level classification
- User authentication
- Question bank storage
- Multi-language support

---

## 👨‍💻 Author

**Pranam Jain**

M.Sc. Applied Research in Computer Science  
Hof University, Germany

LinkedIn: https://www.linkedin.com/in/pranamjain/

---
