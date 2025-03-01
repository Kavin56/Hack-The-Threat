# Hack The Threat - Cybersecurity & AI Hackathon

## Project Overview

This project is built as part of the "Hack The Threat" cybersecurity hackathon, focusing on AI-driven threat detection and security analysis. It consists of two main components:

1. **Demo Website (Testing Environment)**
   - Developed using HTML, CSS, JavaScript, and React.
   - Hosted on Netlify for easy deployment.
   - Used for testing various security vulnerabilities and resilience against cyber threats.
     ![Demo Website](images/demo.png)

2. **Threat Classification System (Streamlit App)**
   - Built with Streamlit to analyze log files for security threats.
   - Implements Generative AI techniques to classify and visualize threats.
   - Allows users to upload log files for real-time analysis.

## Features

- **Honeypots:** Deceptive systems designed to lure and analyze potential attacks.
- **Threat Classification:** Uses AI to detect and classify security threats in log files.
- **Real-time Monitoring:** Tracks website uptime and potential security breaches.
- **Automated Testing & Analysis:** Utilizes various tools to assess security.

## Security Testing Frameworks Used

### 1. Locust (Load Testing)
- Locust is used to simulate multiple users accessing the website to test for performance and vulnerabilities under heavy traffic.
- **How to Run:**
  ```bash
  pip install locust
  locust -f tests/locustfile.py --host https://taupe-tanuki-66c44a.netlify.app/
  ```
- **Sample Output:**
  ![Locust Test Results](tests/sample_output/1_1.png)
  ![Locust Test Results](tests/sample_output/1_2.png)

### 2. Loguru (Logging & Monitoring)
- Loguru is used to log website activity, errors, and uptime monitoring.
- **How to Run:**
  ```bash
  python tests/monitor.py
  ```
- **Sample Output:**
  ![Loguru Logs](tests/sample_output/2.png)

### 3. Uptime Kuma (Website Monitoring)
- Uptime Kuma is a self-hosted monitoring tool that continuously tracks the availability and response time of the website.
- **How to Run:**
  ```bash
  docker run -d --restart always -p 3001:3001 louislam/uptime-kuma
  ```
- **Access Dashboard:**
  Open [http://localhost:3001](http://localhost:3001) in your browser to view monitoring statistics.
- **Sample Output:**
  ![Uptime Kuma Dashboard](tests/sample_output/3.png)

### 4. SQLMap (SQL Injection Testing)
- SQLMap automates the detection and exploitation of SQL injection vulnerabilities.
- **How to Run:**
  ```bash
  git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap
  cd sqlmap
  python sqlmap.py -u "https://taupe-tanuki-66c44a.netlify.app/?id=1" --dbs
  ```
- **Sample Output:**
  ![SQLMap Injection Results](tests/sample_output/4.png)

### 5. Pytest (Automated Security Testing)
- Pytest is used for automated functional and security test cases.
- **How to Run:**
  ```bash
  pytest tests/pytest_tests/test_security.py --html=security_report.html --self-contained-html
  ```
- **Sample Output:**
  ![Pytest Test Results](tests/sample_output/5_1.png)
  ![Pytest Test Results](tests/sample_output/5_2.png)
  ![Pytest Test Results](tests/sample_output/5_3.png)

## Setup and Deployment

### Prerequisites
- Python 3.8+
- Node.js (for frontend testing)
- Docker (for Uptime Kuma)

### Installation
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

## Future Enhancements
- Implement more AI models for threat detection.
- Integrate real-time alerts for detected threats.
- Expand honeypot functionalities to log attacker behavior in detail.

## Contributors
- **[Your Name]** - AI & Security Engineering
- **[Team Members]** - Development & Security Analysis

