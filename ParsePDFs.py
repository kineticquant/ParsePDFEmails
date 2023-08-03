import re
import os
import PyPDF2

def extract_emails_and_orders(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    order_pattern = r'Order #(\d+)'
    
    emails = re.findall(email_pattern, text)
    orders = re.findall(order_pattern, text)
    
    return list(zip(emails, orders))

def search_emails_and_orders_in_pdf(pdf_path):
    data = []
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            data += extract_emails_and_orders(text)
    return data

pdf_directory = r'ENTER YOUR DIRECTORY HERE'

all_data = []

for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        data = search_emails_and_orders_in_pdf(pdf_path)
        all_data.extend(data)

for email, order in all_data:
    print("Email:", email)
    print("Order:", order)
    print()
