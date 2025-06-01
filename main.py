import streamlit as st 
from src.helper import extract_text_from_pdf, ask_llm, fetch_linkedin_jobs, fetch_naukri_jobs

# Page configuration
st.set_page_config('AI Resume Analyzier + Job Finder',layout="wide")
st.title('AI Resume Assistant with Smart Job Suggestions 🚀')
st.markdown("Upload your Resume and get career insights + live job recommendations")

# File uploader
file = st.file_uploader('Upload your resume (PDF)', type=['pdf'])

if file:
    with st.spinner('📚 Extracting text from resume...'):
        text = extract_text_from_pdf(uploaded_file=file)
    
    with st.spinner('✍️ Summarizing the resume...'):
        summary = ask_llm(prompt=f"Summarize this resume highlighting skills, education, and experience:\n\n{text}")
        
    with st.spinner('🔎 Identifying future improvement areas...'):
        gaps = ask_llm(prompt=f"Based on this resume, suggest a future roadmap to improve this person's career prospects (skills to learn, certifications needed, industry exposure):\n\n{text}")
    
    st.markdown("----")
    st.subheader("📄 Resume Summary")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{summary}</div>", unsafe_allow_html=True)

    st.markdown("----")
    st.subheader("🔍 Suggested Future Improvements")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{gaps}</div>", unsafe_allow_html=True)

    
    st.success('Resume analysis completed successfully!')

    if st.button('🔎🎯 Find Matching Jobs'):
        with st.spinner('Generating job keywords...'):
            keywords = ask_llm(
                prompt=f"Based on the resume summary, suggest the best job titles/keywords for job searching. Provide a comma-separated list only, no explanation:\n\n{summary}"
            )
            clean_keywords = keywords.replace("\n", "").strip()
        
        st.success(f'✅ Extracted Job Keywords: `{clean_keywords}`')

        with st.spinner('Fetching jobs from Google Job Agent...'):
            GoogleJobAgent_jobs = fetch_linkedin_jobs(keywords=clean_keywords)
            googleAI_jobs = fetch_naukri_jobs(keywords=clean_keywords)

        #Display LinkedIn Jobs
        st.markdown("----")
        st.header("💼 Top Google Jobs in Sri Lanka")
        if GoogleJobAgent_jobs:
            for job in GoogleJobAgent_jobs:
                st.markdown(f"**{job.get('title')}** at *{job.get('companyname')}*")
                st.markdown(f"📍 Location: {job.get('location')}")
                st.markdown(f"[🔗 Job Link]({job.get('link')})")
                st.markdown("---")
        else:
            st.warning('No Google jobs found.')

        # Display Naukri Jobs
        st.markdown("----")
        st.header("💼 Top Google Agent Jobs")
        if googleAI_jobs:
            for job in googleAI_jobs:
                st.markdown(f"**{job.get('title')}** at *{job.get('companyname')}*")
                st.markdown(f"📍 Location: {job.get('location')}")
                st.markdown(f"[🔗 Job Link]({job.get('link')})")
                st.markdown("---")
        else:
            st.warning('No Google Agent jobs found.')