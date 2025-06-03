# 🧠 TailorMyCV – Your AI-Powered Resume Wingman

Welcome to **TailorMyCV**, an AI-powered resume optimization tool built to help job seekers stand out in the crowd. Whether you're applying for your first job or aiming for a career pivot, this app transforms your generic resume into a job-specific powerhouse—with a personal cover letter and benchmarking to boot.

🔗 [Live Demo](https://tailormycv.streamlit.app) | 📘 [Read the Story](https://medium.com/...) | ⭐ Star this repo if you like it!

---

## ✨ Features

- ✅ **Get Flaws**: AI reviews your resume like a tough recruiter
- 🎯 **Tailored Resume**: Automatically customizes your resume for a specific role
- 💌 **Cover Letter Generator**: Creates a concise and personal letter in seconds
- 📊 **Benchmark Me**: Compares your resume to top 1% candidates and suggests improvements
- 📄 **Download PDF**: Export your tailored resume or cover letter as a PDF

---

## 💻 Tech Stack

- **Python**
- **Streamlit** – for a clean, interactive UI
- **OpenAI GPT-4.1** – for natural language understanding and generation
- **LangChain** – to manage prompt logic and reuse
- **PyMuPDF** – for reliable PDF text extraction

---

## 🚀 Quick Start

1. **Clone the repo**  
   ```bash
   git clone https://github.com/essharmavi/tailor-my-resume.git
   cd tailor-my-resume
   
2. **Create a virtual environment & install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt

3. **Add your OpenAI API Key**
   ```bash
   OPENAI_API_KEY=your_openai_key_here

4. **Run the app**
   ```bash
   streamlit run frontend.py

## Project Structure
tailor-my-resume/
├── frontend.py              # Streamlit UI logic
├── build_resume.py          # Core AI functionality
├── document_load.py         # PDF resume parser
├── requirements.txt         # Python dependencies
└── .env                     # OpenAI API key (you create this)

## 🧠 How It Works (Simple Version)

Upload your resume PDF → paste a job description → choose what you want (flaws, tailored resume, cover letter, or benchmarking) → get results from GPT-4.1 → download PDF.
It’s like having a recruiter, resume editor, and career coach in one AI assistant.

## 👩‍💻 Why I Built This

Because writing resumes is hard. And making them match every job post is even harder. TailorMyCV saves you hours by helping you craft job-specific, professional documents that actually resonate.

## 🤝 Contributing

Got an idea or want to improve this? PRs are welcome! Start with an issue or fork the repo and go wild. ✨

## 📬 Contact

For questions, ideas, or collaboration: [Linkedin]([url](https://www.linkedin.com/in/essharmavi/))
