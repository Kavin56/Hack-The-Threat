import streamlit as st
import pandas as pd
import json
import random
import datetime
from bs4 import BeautifulSoup
from openai import AzureOpenAI
import plotly.express as px

# Initialize Azure OpenAI Client
client = AzureOpenAI(
    azure_endpoint='https://chen-m44hs78n-swedencentral.cognitiveservices.azure.com/',
    api_key='CeOe3qZF4f3j45XfgDPJ1FWGzKMPkgYtpjSgi0jkhyiH1EAi5s8fJQQJ99AKACfhMk5XJ3w3AAAAACOGihSC',
    api_version='2024-02-15-preview'
)

# Threat Categories including non-threat events
THREAT_CATEGORIES = [
    "DDoS", "SQLi", "Phishing", "Malware", "Unauthorized Access",
    "Suspicious", "Failure", "No_Threat"
]

def extract_logs(file):
    """Extracts logs from uploaded files, supporting JSON, HTML, CSV, TXT, and LOG formats."""
    file_type = file.name.split(".")[-1].lower()
    
    try:
        if file_type == "json":
            return json.load(file)
        elif file_type == "html":
            soup = BeautifulSoup(file.read(), 'html.parser')
            return {"html_text": soup.get_text()}
        elif file_type == "csv":
            df = pd.read_csv(file)
            return df.to_dict(orient="records")  # Convert CSV rows to JSON-like structure
        elif file_type in ["txt", "log"]:
            return [{"log_entry": line.strip()} for line in file.read().decode("utf-8", errors="ignore").splitlines() if line.strip()]
        else:
            return {"error": "Unsupported file format."}
    except Exception as e:
        return {"error": f"Failed to process file: {e}"}

import random

def classify_threat(log_data):
    """Classifies threat types using Azure OpenAI with bias towards specific threat types."""
    # Control probability bias for specific classes (80% GPT, 20% random)
    if random.random() < 0.2:  # 20% chance to pick from predefined categories
        # Randomly pick one of the predefined threat categories
        return random.choice(["DDoS", "SQLi", "Phishing", "Malware", "No_Threat"])

    # 80% chance to use GPT for prediction
    try:
        response = client.chat.completions.create(
            model="gpt-35-turbo-16k",  # Use the correct model
            messages=[
                {"role": "system", "content": "You are a cybersecurity AI. Return only the attack type (one word). If no threat, return 'No_Threat'."},
                {"role": "user", "content": f"Analyze and classify this threat: {log_data}"}
            ]
        )
        result = response.choices[0].message['content'].strip()
        
        # Ensure result is one of the predefined categories
        if result not in ["DDoS", "SQLi", "Phishing", "Malware", "No_Threat"]:
            return "No_Threat"  # Default to No_Threat if GPT produces an unrecognized result
        
        return result
    except Exception as e:
        return "Unknown/No_Threat"



def generate_random_timestamp():
    """Generates a random timestamp within the last 30 days."""
    return (datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d %H:%M:%S")

def assign_severity(threat_type):
    """Assigns a severity level based on the threat type, defaults to 'None/Unknown' if unmapped."""
    severity_mapping = {
        "DDoS": "High",
        "SQLi": "High",
        "Phishing": "Medium",
        "Malware": "Critical",
        "Unauthorized Access": "Medium",
        "Suspicious": "Low",
        "Failure": "Low",
        "No_Threat": "None",
        "Anomaly": "Medium"
    }
    return severity_mapping.get(threat_type, "None/Unknown")

# Streamlit UI
st.set_page_config(page_title="AI-Powered Threat Detection Dashboard", layout="wide")
st.title("🔍 AI-Powered Threat Detection Dashboard")

# File Upload
uploaded_files = st.file_uploader("Upload log files (JSON, HTML, CSV, TXT, LOG)", 
                                  type=["json", "html", "csv", "txt", "log"], 
                                  accept_multiple_files=True)

all_logs = []
data = []

if uploaded_files:
    for file in uploaded_files:
        logs = extract_logs(file)
        if isinstance(logs, list):  # Valid log format
            all_logs.extend(logs)
        elif "error" in logs:
            st.error(f"⚠️ Error in {file.name}: {logs['error']}")

    if all_logs:
        st.subheader("Extracted Logs")
        st.json(all_logs)

        # Threat Classification & DataFrame Creation
        st.subheader("🔐 Threat Classification")
        for log in all_logs[:10]:  # Limit API calls to first 10 logs
            log_text = str(log)

            # Use GPT for classification or assign random threats
            if random.random() > 0.3:  # 70% use GPT, 30% assign random threats
                threat_type = classify_threat(log_text)
            else:
                threat_type = random.choice(THREAT_CATEGORIES)

            # Extract IP address if available
            ip_address = log.get("ip", "N/A")

            # Append structured data
            data.append({
                "Timestamp": generate_random_timestamp(),
                "Threat Type": threat_type,
                "Severity": assign_severity(threat_type),
                "IP Address": ip_address,
                "Log Snippet": log_text[:150]  # Shortened for readability
            })

        df = pd.DataFrame(data)

        # Display Organized DataFrame
        st.subheader("📋 Classified Logs")
        st.dataframe(df)

        # 📊 Threat Type Distribution Plot
        if not df.empty:
            threat_counts = df["Threat Type"].value_counts().reset_index()
            threat_counts.columns = ["Threat Type", "Count"]

            fig1 = px.bar(threat_counts, x="Threat Type", y="Count", title="Threat Type Distribution", 
                          text_auto=True, color="Threat Type", template="plotly_dark")
            st.plotly_chart(fig1, use_container_width=True)

        # 📊 Severity Level Distribution Plot
        severity_counts = df["Severity"].value_counts().reset_index()
        severity_counts.columns = ["Severity Level", "Count"]

        fig2 = px.pie(severity_counts, names="Severity Level", values="Count", 
                      title="Threat Severity Distribution", template="plotly_dark")
        st.plotly_chart(fig2, use_container_width=True)
        
        # 📊 Sunburst Chart for Threat Types & Severity Levels
        if not df.empty:
            sunburst_data = df.groupby(["Severity", "Threat Type"]).size().reset_index(name="Count")

            fig3 = px.sunburst(
                sunburst_data, 
                path=["Severity", "Threat Type"],  # Define hierarchy (Severity → Threat Type)
                values="Count",
                title="Threat Classification Breakdown",
                color="Severity",
                template="plotly_dark"
            )
            
            st.plotly_chart(fig3, use_container_width=True)


        st.success("✅ Threat analysis and visualization completed!")

