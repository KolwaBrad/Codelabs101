import re
def generate_email(name):
    names = name.split(',')
    first_name = names[0].strip()
    last_name = names[-1].strip()
    full_name = first_name + " " + last_name
    full_name = re.sub(r'[^\w\s]', '', full_name)  # Remove special characters
    email = f"{full_name.replace(' ', '.').lower()}@gmail.com"  # Replace spaces with dots
    return email