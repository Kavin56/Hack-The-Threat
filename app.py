import streamlit as st
import pandas as pd
import json
from bs4 import BeautifulSoup
from openai import AzureOpenAI
import matplotlib.pyplot as plt
import plotly.express as px

# Initialize Azure OpenAI Client
client = AzureOpenAI(
    azure_endpoint='https://chen-m44hs78n-swedencentral.cognitiveservices.azure.com/openai/deployments/gpt-35-turbo-16k/chat/completions?api-version=2024-08-01-preview',
    api_key='CeOe3qZF4f3j45XfgDPJ1FWGzKMPkgYtpjSgi0jkhyiH1EAi5s8fJQQJ99AKACfhMk5XJ3w3AAAAACOGihSC',
    api_version='2024-02-15-preview'
)

def extract_logs(file):
    """Extracts logs from uploaded files."""
    file_type = file.name.split(".")[-1]
    
    if file_type == "json":
        return json.load(file)
    elif file_type == "html":
        soup = BeautifulSoup(file.read(), 'html.parser')
        return {"html_text": soup.get_text()}
    else:
        return {"error": "Unsupported file format."}

def classify_threat(log_data):
    """Classifies threat types using Azure OpenAI."""
    response = client.chat.completions.create(
        model="gpt-35-turbo-16k",
        messages=[{"role": "system", "content": "You are a cybersecurity AI that classifies threats from logs."},
                  {"role": "user", "content": f"Analyze and classify this threat: {log_data}"}]
    )
    return response.choices[0].message.content

# Streamlit UI
st.set_page_config(page_title="AI-Powered Threat Detection Dashboard", layout="wide")
st.title("🔍 AI-Powered Threat Detection Dashboard")

# File Upload
uploaded_files = st.file_uploader("Upload log files (JSON, HTML, etc.)", type=["json", "html", "csv"], accept_multiple_files=True)
all_logs = []
if uploaded_files:
    for file in uploaded_files:
        logs = extract_logs(file)
        if "error" not in logs:
            all_logs.append(logs)

    st.subheader("Extracted Logs")
    st.json(all_logs)

    # Threat Classification
    st.subheader("🚨 Threat Classification")
    classified_threats = [classify_threat(log) for log in all_logs]
    df = pd.DataFrame(classified_threats, columns=["Threat Classification"])
    st.dataframe(df)
    
    # Visualization
    st.subheader("📊 Threat Visualization")
    fig = px.histogram(df, x="Threat Classification", title="Threat Type Distribution")
    st.plotly_chart(fig)
    
    st.success("Threat analysis completed!")
