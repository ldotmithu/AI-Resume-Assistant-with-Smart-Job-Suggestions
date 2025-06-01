import streamlit as st
import fitz  # PyMuPDF
import os
from euriai import EuriaiClient
from dotenv import load_dotenv
from apify_client import ApifyClient

# Load environment variables
load_dotenv()

# Initialize clients
euriai_client = EuriaiClient(
    api_key=os.getenv("EURI_API_KEY"),
    model="gpt-4.1-nano"
)

apify_client = ApifyClient(os.getenv("APIFY_API_KEY"))

# Extract text from uploaded PDF
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Ask EURI AI to generate output
def ask_llm(prompt, max_tokens=500):
    response = euriai_client.generate_completion(prompt=prompt, temperature=0.5, max_tokens=max_tokens)
    if isinstance(response, dict) and 'choices' in response:
        return response['choices'][0]['message']['content']
    return response

# Fetch LinkedIn Jobs using Apify
def fetch_linkedin_jobs(keywords, location="SriLanka", rows=60):
    run_input = {
        "title": keywords,
        "location": location,
        "rows": rows,
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"],
        }
    }
    run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs

# Fetch Naukri Jobs using Apify
def fetch_naukri_jobs(keywords, max_jobs=60):
    run_input = {
        "keyword": keywords,
        "maxJobs": 60,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
    }
    run = apify_client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs
