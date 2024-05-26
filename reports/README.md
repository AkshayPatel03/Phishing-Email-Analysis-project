This is a detailed report template for a phishing email attack, based on the scenario involving a fraudulent Costco gift voucher email:

---

# Phishing Email Attack Report

## Executive Summary

**Objective**: This report investigates a phishing email attack involving a fraudulent Costco gift voucher of $1000, identified and analyzed to determine its impact and provide recommendations for future prevention.

**Key Findings**:

- The phishing email spoofed a legitimate Costco offer.
- The email header analysis revealed unsafe origins.
- The email contained malicious links aiming to collect personal information.

**Recommendations**:

- Enhance email security filters.
- Implement multi-factor authentication (MFA).
- Conduct regular phishing awareness training for employees.

## Incident Overview

**Incident Description**: A phishing email purporting to offer a $1000 Costco gift voucher was received by several employees. The email was designed to trick recipients into clicking on a malicious link.

**Timeline of Events**:

- **Discovery**: May 20, 2024 - The email was reported by an employee to the IT security team.
- **Analysis Initiated**: May 21, 2024 - The IT security team began analyzing the email header and body.
- **Containment**: May 22, 2024 - Containment measures were implemented to block the malicious sender and links.
- **Completion**: May 23, 2024 - The investigation was concluded, and recommendations were formulated.

## Technical Analysis

**Email Details**:

- **Sender Address**: 1gc9f3ej3oqul@i2nvnwp29.yolwcyfk.com
- **Subject Line**: "Re: Akkip Second Attempt for #Akkip's $1000 Costco Gift Card"
- **Email Body**:

  ```
  Congratulations! You have been selected to receive a $1000 Costco gift voucher. Click the link below to claim your reward.

  [Confirm Here](https://storage.googleapis.com/dfg153erh35ef1gdr/dfgremjflmgr.html#idf2myzxq24u.wBnQbTVBgtjE?d9WJQVccW7rDcxKFkcdcWYc8cHC09dFq7cbbb5z)
  ```
![Email Header Analysis](https://github.com/AkshayPatel03/Phishing-Email-Analysis-project/blob/b24bacf241cab1203afd72b48f54b6e6c9cf274b/images/body-cotsco.PNG)

**Indicators of Compromise (IoCs)**:

- **Malicious URL**: Multiple Advertisments and malicious URLs
- **Sender IP Address**: 185.222.162.71 (identified as unsafe)

**Header Analysis**:

- Utilized tools: MXToolbox, custom Python scripts.
- Findings: The email originated from an IP address known for malicious activities. SPF, DKIM, and DMARC checks failed.

![Email Health Analysis](images\costco-email-health.PNG)

**Phishing Technique**: The email used social engineering tactics, leveraging the allure of a high-value reward to entice recipients to click on a malicious link.

## Impact Assessment

**Affected Systems and Users**:

- **Users**: 5 employees reported receiving the email.
- **Systems**: No systems were directly compromised, but there was a risk of credential harvesting if the link was clicked.

**Data Compromised**: No confirmed data breaches, but personal information was at risk if users followed the phishing link.

**Business Impact**: Potential for reputational damage and financial loss if user credentials were harvested and misused.

## Response Actions

**Initial Response**:

- The IT security team was alerted by an employee.
- Immediate instructions were sent out to employees to ignore and delete the email.

**Containment Measures**:

- Blocked the sender's email address and IP.
- Added the malicious URL to the email filter blacklist.

**Eradication Steps**:

- Scanned all systems for any signs of compromise.
- Verified that no users clicked on the malicious link.

**Recovery Efforts**:

- Conducted a company-wide password reset as a precaution.
- Updated security awareness materials to include details of this phishing attempt.

## Root Cause Analysis

**Root Cause**: The phishing email bypassed the existing email filters due to lack of advanced threat detection mechanisms.

**Contributing Factors**:

- Lack of employee awareness about identifying phishing emails.
- Inadequate email filtering and monitoring systems.

## Recommendations

**Preventive Measures**:

- **Email Security**: Enhance email filters to detect and block phishing attempts more effectively.
- **User Training**: Conduct regular phishing awareness training sessions for all employees.

**Detection Improvements**:

- Deploy advanced threat detection tools with machine learning capabilities.
- Improve monitoring practices to detect and respond to phishing attempts promptly.

**Incident Response Enhancements**:

- Update incident response protocols to include more detailed steps for handling phishing attacks.
- Conduct regular incident response drills.

## Conclusion

**Summary**: A phishing email attack involving a fake Costco gift voucher was successfully identified and contained. No systems were compromised, but the incident highlighted areas for improvement in email security and employee training.

**Next Steps**:

- Implement recommended preventive measures and improvements.
- Schedule a follow-up review to assess the effectiveness of the new measures.

## Appendices

**Raw Data**:

- Email headers and body content.
- Analysis results from MXToolbox and Python scripts.

**Supporting Documents**:

- Screenshots of the phishing email.
- Detailed malware analysis report (if applicable).
- User training materials.

---

This template provides a structured and comprehensive approach to documenting and analyzing a phishing email attack, ensuring that all relevant aspects are covered and actionable recommendations are provided.
