from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("OPENAI_API_KEY not found in environment variables.")

model = ChatOpenAI(model="gpt-4.1", temperature=0.3, api_key=api_key)

def call_llm(filled_prompt):
    chain = model | StrOutputParser()
    return chain.invoke(filled_prompt)


def get_flaws(resume_text, job_role, industry, job_description):
    prompt = """
You are a seasoned recruiter in the {industry} industry.
Your task is to review a resume for the role of **{job_role}**.

Job Description:
{job_description}

Resume:
{resume_text}

---
Please analyze and return:
- Weak areas in the resume
- Overused buzzwords
- Missing metrics or details
- Gaps or mismatches with the job description

Be brutally honest and constructive. Respond professionally.
"""
    template = PromptTemplate(
        template=prompt,
        input_variables=["industry", "job_role", "job_description", "resume_text"]
    )
    filled_prompt = template.format(
        industry=industry,
        job_role=job_role,
        job_description=job_description,
        resume_text=resume_text
    )
    return call_llm(filled_prompt)


def tailor_resume(resume_text, job_description):
    prompt = """
Tailor this resume:
{resume_text}
to fit this specific job description:
{job_description}

Highlight matching experience and reword sections to match the language used.
Also, rephrase the experienc section to highlight impact, results, and transferrable skills uisng action levels and quantifiable outcomes.
Write a powerful 3-line p[rofessional summary that hooks a recruiter in under 10 seconds. Prioritize impact, clarity, and value.
"""
    template = PromptTemplate(
        template=prompt,
        input_variables=["resume_text", "job_role", "industry", "job_description"]
    )
    filled_prompt = template.format(
        resume_text=resume_text,
        job_description=job_description
    )
    return call_llm(filled_prompt)


def create_cover_letter(resume_text, job_description):
    prompt = """
Write a compelling cover letter based on this resume:
{resume_text}
and this job description:
{job_description}

Keep it personal, enthusiastic, and under 200 words.
"""
    template = PromptTemplate(
        template=prompt,
        input_variables=["resume_text", "job_role", "industry", "job_description"]
    )
    filled_prompt = template.format(
        resume_text=resume_text,
        job_description=job_description
    )
    return call_llm(filled_prompt)


def benchmark_resume(resume_text, job_description):
    prompt = """
Act as a hiring manager.
Based on this job description:
{job_description}

Describe what the resume of a top 1% candidate would look like.
Compare it to my resume:
{resume_text}

Suggest what I should add or change to reach that level.

Also, provide estimated annual salary packages I might deserve in these regions: India, Europe, Middle East, Singapore, and USA.
"""
    template = PromptTemplate(
        template=prompt,
        input_variables=["resume_text", "job_role", "industry", "job_description"]
    )
    filled_prompt = template.format(
        resume_text=resume_text,
        job_description=job_description
    )
    return call_llm(filled_prompt)
