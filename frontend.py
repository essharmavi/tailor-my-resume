import streamlit as st
from document_load import get_resume
from build_resume import (
    get_flaws,
    tailor_resume,
    create_cover_letter,
    benchmark_resume
)
from fpdf import FPDF


# PDF Utility
def text_to_pdf_bytes(text, title="Document"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, txt=title, ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Helvetica", size=11)
    for line in text.split('\n'):
        pdf.multi_cell(0, 8, line.strip())

    return pdf.output(dest='S').encode('latin1')


# Page Configuration
st.set_page_config(page_title="TailorMyCV", page_icon="🧠", layout="centered")

# Header
st.title("🧠 TailorMyCV")
st.markdown(
    "Welcome to **TailorMyCV** – your personal assistant to help fine-tune your resume and stand out for your dream job. "
    "Upload your resume, choose what you'd like to improve, and get tailored, AI-assisted feedback in seconds!"
)

# Upload Resume
st.header("📄 Upload Your Resume")
uploaded_file = st.file_uploader("Upload your **PDF resume** here", type="pdf")

resume_text = None
if uploaded_file:
    with st.spinner("Extracting text from your resume..."):
        resume_text = get_resume(uploaded_file)
    st.success("Resume uploaded and processed successfully! 🎉")

# Job Information
st.header("🎯 Tell Us About the Role")
job_role = st.text_input("Job Title", placeholder="e.g., Data Analyst")
industry = st.text_input("Industry", placeholder="e.g., Financial Services")
job_description = st.text_area(
    "Job Description",
    placeholder="Paste the job description here to get the most relevant feedback...",
    height=150
)

# Tool Selection
tool_usage = st.selectbox(
    "🔧 What would you like to do?",
    ["Get Flaws in My Resume", "Tailor My Resume", "Create a Cover Letter", "Benchmark My Resume"]
)

# Action Button
if st.button("🚀 Get Started"):
    if not all([resume_text, job_role, job_description, industry]):
        st.warning("Please complete all fields and upload your resume.")
    else:
        with st.spinner("Processing your request..."):
            if tool_usage == "Get Flaws in My Resume":
                result = get_flaws(resume_text, job_role, industry, job_description)
            elif tool_usage == "Tailor My Resume":
                result = tailor_resume(resume_text, job_description)
            elif tool_usage == "Create a Cover Letter":
                result = create_cover_letter(resume_text, job_description)
            elif tool_usage == "Benchmark My Resume":
                result = benchmark_resume(resume_text, job_description)
            else:
                result = "Invalid option."

        # Show Result
        st.subheader("✅ Here's what we came up with:")
        st.markdown(result)

        # PDF Option
        if tool_usage in ["Tailor My Resume", "Create a Cover Letter"]:
            st.markdown("---")
            st.info("Would you like to download this as a polished PDF?")
            if st.checkbox("Yes, generate PDF"):
                pdf_bytes = text_to_pdf_bytes(result, title=tool_usage)
                filename = tool_usage.lower().replace(" ", "_") + ".pdf"
                st.download_button(
                    label="📥 Download PDF",
                    data=pdf_bytes,
                    file_name=filename,
                    mime="application/pdf"
                )
