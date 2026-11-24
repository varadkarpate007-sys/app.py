def process_email_archive(input_filename="email_archive.txt", output_filename="email_preview.txt"):
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        total_emails = len(lines)
        first_two = lines[:2]

        preview_content = f"Total Emails Count: {total_emails}\n\nFirst Two Emails:\n"
        for i, email_line in enumerate(first_two, 1):
            preview_content += f"{i}. {email_line.strip()}\n"

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(preview_content)

        print(f"Successfully processed {total_emails} emails and saved the preview to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")

if __name__ == "__main__":
    process_email_archive()
