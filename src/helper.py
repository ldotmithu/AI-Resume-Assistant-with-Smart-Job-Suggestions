import fitz 
import os 
from groq import Groq
from apify_client import ApifyClient
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
APIFY_API_KEY = os.getenv('APIFY_API_KEY')

client = Groq(api_key=GROQ_API_KEY
           )

def read_pdf_extract_text(pdf_file):
    file = fitz.open(stream = pdf_file.read(),filetype = "pdf")
    text = ""
    for page in file:
        text += page.get_text()
    return text  

def ask_llm(prompt):
    responce = client.chat.completions.create(
        messages =[{
            'role':'user','content': prompt
        }
        ],
        temperature=0.5,
        max_tokens=500,
        model = 'meta-llama/llama-4-scout-17b-16e-instruct'
    )
    return responce.choices[0].message.content

def getdata_from_GoogleJob(keywords,location='SriLanka',row=10):
    client = ApifyClient(APIFY_API_KEY)
    
    run_input = {
        "startUrls": [
            "https://www.google.com/search?q=Software+Engineer+jobs+in+Sri+Lanka&ibp=htl;jobs"
        ],
        "maxItems": 5,
        "endPage": 1,
        "queries": [keywords],  # Can customize based on your input
        "countryCode": "lk",  # ISO 3166-1 Alpha-2 for Sri Lanka
        "languageCode": "en",
        "locationUule": "w+CAIQICIZU2lyaSBMYW5rYSwgU3JpIExhbmth",  # uule for "Sri Lanka"
        "radius": 100,
        "includeUnfilteredResults": False,
        "csvFriendlyOutput": True,
        "extendOutputFunction": "($) => { return {} }",
        "customMapFunction": "(object) => { return {...object} }",
        "proxy": { "useApifyProxy": True },
    }

    run = client.actor("nopnOEWIYjLQfBqEO").call(run_input=run_input)
    jobs = client.dataset(run["defaultDatasetId"]).iterate_items()
    return jobs

def getdata_from_JobScan_AI(keywords,max_jobs = 60,location="Colombo, Sri Lanka"):
    client = ApifyClient(APIFY_API_KEY)
    
    run_input = {
    "optional_keywords": [keywords],
    "mandatory_keywords": [
        "Remote",
        "Full-time",
    ],
    "search_sites": [
        "boards.greenhouse.io",
        "jobs.lever.co",
        "myworkdayjobs.com",
        "careers.smartrecruiters.com",
        "jobs.jobvite.com",
        "careers.icims.com",
        "angel.co",
        "stackoverflow.com/jobs",
        "weworkremotely.com",
        "remotive.io",
        "bamboohr.com",
        "https://www.linkedin.com/jobs",
    ],
    "days_to_search": 30,
    "result_limit": 10,
}
    run = client.actor("VHwSS0ICULitPHsUh").call(run_input=run_input)
    jobs = client.dataset(run["defaultDatasetId"]).iterate_items()
    return jobs
    
  