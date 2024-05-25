import re
import os
import sys
from optparse import OptionParser

# Regular expression for extracting email addresses
email_regex = re.compile(r"([a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)")

# Known malicious domains and phishing keywords (for demo purposes, extend this list as needed)
malicious_domains = {"examplemalicious.com", "phishingsite.org"}
phishing_keywords = {"urgent", "immediately", "password", "verify", "account", "suspended"}

def file_to_str(filename):
    """Returns the contents of filename as a string."""
    with open(filename, encoding='utf-8', errors='ignore') as f:
        return f.read().lower()

def get_emails(s):
    """Returns a list of matched emails found in string s."""
    return re.findall(email_regex, s)

def check_email(email):
    """Checks if an email is potentially malicious."""
    domain = email.split('@')[-1]
    if domain in malicious_domains:
        return True
    return False

def check_content(content):
    """Checks if the content contains suspicious patterns or keywords."""
    for keyword in phishing_keywords:
        if keyword in content:
            return True
    return False

if __name__ == '__main__':
    parser = OptionParser(usage="Usage: python %prog [FILE]...")
    options, args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    for arg in args:
        if os.path.isfile(arg):
            content = file_to_str(arg)
            emails = get_emails(content)
            for email in emails:
                if check_email(email):
                    print(f"Malicious email detected: {email}")
                else:
                    print(f"Email: {email} seems safe.")
            
            if check_content(content):
                print("The email content contains suspicious keywords or patterns.")
            else:
                print("The email content seems safe.")
        else:
            print(f'"{arg}" is not a file.')
            parser.print_usage()
            sys.exit(1)
