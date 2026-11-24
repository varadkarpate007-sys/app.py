import re

def extract_outreach_emails(filename):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    unique_emails = set()

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = re.findall(email_pattern, content)

            for email in matches:
                unique_emails.add(email.lower())

        return sorted(list(unique_emails))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

if __name__ == "__main__":
    file_name = "web_content.txt"
    extracted_emails = extract_outreach_emails(file_name)

    print(f"Found {len(extracted_emails)} unique outreach email(s):")
    for email in extracted_emails:
        print(email)
