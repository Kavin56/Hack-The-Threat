---

# Hack The Threat - Cybersecurity & AI Hackathon 🛡️🤖

## Project Overview 🌐🔍


1. **Demo Website (Testing Environment)** 🌍🖥️

   - Developed using HTML, CSS, and JavaScript.
   - Hosted on Netlify for easy deployment.
   - Used for testing various security vulnerabilities and resilience against cyber threats.&#x20;

2. **Threat Classification System (Streamlit App)** 📊🔐

   - Built with Streamlit to analyze log files for security threats.
   - Implements Generative AI techniques to classify and visualize threats.
   - Allows users to upload log files for real-time analysis.
   - **AI Model:** Leveraging **Azure AI Studio** and OpenAI's **GPT-3.5-turbo-16k** for advanced threat classification and structuring of log data.

## Features ⚡️

- **Threat Classification:** Uses AI to detect and classify security threats in log files with OpenAI's GPT-3.5-turbo-16k.
- **Real-time Monitoring:** Tracks website uptime and potential security breaches.
- **Automated Testing & Analysis:** Utilizes various tools to assess security.
- **Mitigation Strategy Report:** Provides AI-generated recommendations for fixing detected security threats.

## Security Testing Frameworks Used 🛠️

### 1. Locust (Load Testing) 🏃‍♂️💨

- Simulates multiple users accessing the website to test for performance and vulnerabilities under heavy traffic.

### 2. Loguru (Logging & Monitoring) 📝🔎

- Logs website activity, errors, and uptime monitoring.

### 3. Uptime Kuma (Website Monitoring) 🌐⏱️

- Self-hosted monitoring tool that continuously tracks website availability and response time.

### 4. SQLMap (SQL Injection Testing) 💥🔒

- Automates the detection and exploitation of SQL injection vulnerabilities.

### 5. Pytest (Automated Security Testing) 🧪✅

- Used for automated functional and security test cases.

## Mitigation Strategy Report 🛡️🔒

- **AI-generated remediation suggestions** for detected threats.
- **Severity classification** to prioritize security risks.
- **Best security practices** tailored to each vulnerability type.

## Setup and Deployment ⚙️🚀

### Installation 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/hack-the-threat.git
   cd hack-the-threat
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit Threat Classification App:
   ```bash
   streamlit run app.py
   ```

## Azure OpenAI Integration for Threat Classification 🤖🔒

The **Threat Classification System** uses **Azure OpenAI** to classify and analyze security threats with the **GPT-3.5-turbo-16k** model.

### Securely Store Credentials

```bash
export AZURE_API_KEY="your-api-key-here"
export AZURE_ENDPOINT="https://your-azure-endpoint.openai.azure.com/"
```

---

## Future Enhancements 🔮

- Implement more AI models for threat detection.
- Integrate real-time alerts for detected threats.
- Expand honeypot functionalities to log attacker behavior in detail.

## Contributors 🤝

- **[KAVINKUMAR VS]** - AI & Security Engineering
- **[RAKSHAN A]** - Development & Security Analysis
- **[MANI SHANKAR SG]** - Demo Website & Deployment
- **[JAGAADHEP U K]** - Streamlit page & Visualization

---

## Sample Screenshots 🎨


---

