# Phishing Email Analysis and Remediation

## Introduction

Phishing is a cyber attack that involves tricking email recipients into believing that a message is legitimate, often to steal sensitive information. This project focuses on analyzing phishing emails and developing a remediation strategy for a Security Operations Center (SOC).

## Project Objectives

- Analyze phishing emails to identify malicious elements.
- Develop a remediation strategy to respond to phishing incidents.
- Provide a step-by-step guide for SOC analysts to handle phishing incidents effectively.

## Project Structure
- **data/**: Contains sample phishing emails for analysis.
- **scripts/**: Includes scripts for email analysis and automation.
- **README.md**: Project documentation and instructions.

## Repository Structure

- **data/**: Contains sample phishing emails for analysis.
- **scripts/**: Includes scripts for email analysis and automation.
- **reports/**: Generated reports from the analysis.
- **images/**: Visual representations and diagrams.

## Analysis of Malicious Emails

### Step 1: Collecting and Identifying Phishing Emails

SOC analysts collect suspected phishing emails from various sources like user reports, email gateways, and threat intelligence feeds.

### Step 2: Email Header Analysis

Examine email headers to identify suspicious elements such as spoofed addresses, unusual sending patterns, and anomalous metadata.

```bash
# Example script to extract email headers
python3 scripts/extract-email-headers.py data/sample-emails/email1.eml
```
The Python scripts will be in the Scripts repository (File name: extract-email-headers.py)

### Step 3: Email Body Analysis including URL and Attachment Analysis
Analyze the content of the email body for malicious links, attachments, and social engineering tactics for malware and phishing pages.

```bash
# Example script to extract email body Analysis
python3 scripts/analyse-email.py data/sample-emails/cotsco.eml
```
The Python scripts will be in the Scripts repository (File name: analyse-email.py)

# Incident Response/ Remediation Steps 

## Step-by-Step Incident Response

### Identification:

* Detect the phishing email through monitoring and user reports.
* Confirm the phishing nature by analyzing headers, body, URLs, and attachments.

### Containment:

* Isolate the affected systems.
* Block malicious domains and URLs on the network.

### Eradication:

* Remove phishing emails from user mailboxes.
* Delete malicious files and clean affected systems.

### Recovery:

* Restore systems to operational status.
* Monitor for any signs of persistence.

### Lessons Learned:

* Conduct a post-incident review.
* Update security measures and training based on findings.

# Summary

This project provides a comprehensive approach to phishing email analysis and remediation for SOC analysts. By following the detailed steps and utilizing provided scripts, SOC analysts can effectively respond to and mitigate phishing incidents.

# How to use this project
## Prerequisites
- Python 3.x
- Required Python libraries

## Installation
 1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Phishing-Email-Analysis.git
    ```
2. Navigate to the project directory:
   ```bash
    cd Phishing-Email-Analysis
    ```
3. Install dependencies:
   ```bash
    pip install -r requirements.txt
    # Create a text file with all the dependencies and run it or do it separately like the below line
   pip install requests beautifulsoup4
    ```
## Running the Analysis Script

To analyze an email file:
```bash
    python3 scripts/analyze_email.py (Path of the Python file) path/to/email.eml (Path of the email file which must be saved .eml)


