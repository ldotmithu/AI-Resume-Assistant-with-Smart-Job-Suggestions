# 🧠 AI Resume Assistant with Smart Job Suggestions

A Streamlit-powered web application that analyzes resumes using AI and recommends matching job opportunities from platforms like LinkedIn, Naukri, and Google Jobs.  

---

## 🚀 Features

- 📄 **Resume Text Extraction** (from PDF)
- 🧾 **AI-Powered Resume Summary** (using LLMs)
- 🔍 **Future Improvement Suggestions** for the resume
- 🏷️ **Job Keyword Extraction** for search optimization
- 💼 **Job Fetching** from:
  - LinkedIn (via Apify) # paid
  - Naukri (via Apify) 
  - Google Jobs (via Apify actor and customizable queries)

---

## 🛠️ Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- [Apify SDK](https://docs.apify.com/)
- [Groq API](for LLM calls)

---

## 📦 Installation

```bash
# Create and activate virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

# Install dependencies
```bash
pip install -r requirements.txt
```

# 🔑 Environment Variables (.env)
Create a .env file in the root directory:
```.env
GROQ_API_KEY=your_groq_key_here
APIFY_API_KEY=your_apify_key_here
```

# ▶️ Running the App
```bash
streamlit run main.py
```



