import re
import os
import sys
from email import policy
from email.parser import BytesParser
from optparse import OptionParser

# Regular expression for extracting URLs
url_regex = re.compile(r'https?://[^\s/$.?#].[^\s]*', re.IGNORECASE)

# Known malicious domains and phishing keywords (extend as needed)
malicious_domains = {"examplemalicious.com", "phishingsite.org"}
phishing_keywords = {"urgent", "immediately", "password", "verify", "account", "suspended"}

def file_to_bytes(filename):
    """Returns the contents of filename as bytes."""
    with open(filename, 'rb') as f:
        return f.read()

def extract_urls(s):
    """Returns a list of URLs found in string s."""
    return re.findall(url_regex, s)

def check_url(url):
    """Checks if a URL is potentially malicious by checking its domain."""
    domain = url.split('/')[2]
    if domain in malicious_domains:
        return True
    return False

def check_content(content):
    """Checks if the content contains suspicious patterns or keywords."""
    for keyword in phishing_keywords:
        if keyword.lower() in content.lower():
            return True
    return False

def extract_attachments(msg):
    """Extracts and lists attachments from an email message."""
    attachments = []
    for part in msg.iter_attachments():
        filename = part.get_filename()
        if filename:
            attachments.append(filename)
    return attachments

def analyze_email(filename):
    """Analyzes the email for malicious links, attachments, and social engineering tactics."""
    content = file_to_bytes(filename)
    msg = BytesParser(policy=policy.default).parsebytes(content)
    body = msg.get_body(preferencelist=('plain', 'html')).get_content()

    is_malicious = False

    # Analyze links
    urls = extract_urls(body)
    for url in urls:
        if check_url(url):
            print(f"Malicious URL detected: {url}")
            is_malicious = True
        else:
            print(f"URL: {url} seems safe.")

    # Analyze attachments
    attachments = extract_attachments(msg)
    if attachments:
        print("Attachments detected:")
        for attachment in attachments:
            print(f"- {attachment}")
            is_malicious = True
    else:
        print("No attachments found.")

    # Analyze content for phishing keywords
    if check_content(body):
        print("The email content contains suspicious keywords or patterns.")
        is_malicious = True
    else:
        print("The email content seems safe.")

    if is_malicious:
        print("The email is potentially malicious.")
    else:
        print("The email seems safe.")

if __name__ == '__main__':
    parser = OptionParser(usage="Usage: python %prog [FILE]...")
    options, args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    for arg in args:
        if os.path.isfile(arg):
            analyze_email(arg)
        else:
            print(f'"{arg}" is not a file.')
            parser.print_usage()
            sys.exit(1)
