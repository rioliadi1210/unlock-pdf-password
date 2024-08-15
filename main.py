import pikepdf
import itertools
import string

# Define the PDF file path
pdf_file = r'C:\Users\BLA\Desktop\juni2024.pdf'

def try_password(pdf_file, password):
    try:
        # Open the PDF file with the given password
        pdf = pikepdf.open(pdf_file, password=password)
        return True
    except pikepdf._qpdf.PasswordError:
        return False

# Generate a list of possible passwords
def generate_passwords(length):
    characters = string.ascii_letters + string.digits
    return (''.join(candidate) for candidate in itertools.product(characters, repeat=length))

# Brute-force attack
def brute_force(pdf_file, max_length):
    for length in range(1, max_length + 1):
        for password in generate_passwords(length):
            print(f"Trying password: {password}")
            if try_password(pdf_file, password):
                print(f"Password found: {password}")
                return password
    print("Password not found.")
    return None

# Use the brute force function with a max password length
max_password_length = 4  # Adjust this based on your needs
brute_force(pdf_file, max_password_length)
