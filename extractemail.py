import re

def extract_emails_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        
    # Pola regex untuk mencocokkan email
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Cari semua email yang cocok
    emails = re.findall(email_pattern, text)
    
    return emails

def save_emails_to_file(emails, output_file):
    with open(output_file, 'a', encoding='utf-8') as file:
        for email in emails:
            file.write(email + '\n')

# Input path ke file yang akan diproses melalui console
file_path = input("Masukkan file Contohnya (list.txt): ")

# Path ke file output
output_file = 'extract.txt'

# Panggil fungsi untuk mengekstrak email
emails = extract_emails_from_file(file_path)

# Simpan hasil ekstraksi ke file
if emails:  # Hanya simpan jika ada email yang ditemukan
    save_emails_to_file(emails, output_file)
    print("Email yang berhasil diekstrak:")
    for email in emails:
        print(email)
else:
    print("Tidak ada email yang ditemukan.")
