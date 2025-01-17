import re
from datetime import datetime, date

def correct_name(name):
    if name:
        return name.title()
    else:
        return "Unknown"

def correct_age(age):
    if isinstance(age, int) and 18 <= age <= 65:
        return age
    else:
        return 25

def correct_email(email):
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
        return email
    else:
        return "invalid@example.com"

def correct_salary(salary):
    if isinstance(salary, (int, float)):
        return max(salary, 0)
    else:
        return 0.0

def correct_date(join_date):
    try:
        return datetime.strptime(join_date, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return date(2023, 1, 1)

def process_data(data):
    processed_data = []
    for record in data:
        record = {k.strip().lower(): v for k, v in record.items()}
        processed_entry = {
            "name": correct_name(record.get("name")),
            "age": correct_age(record.get("age")),
            "email": correct_email(record.get("email")),
            "salary": correct_salary(record.get("salary")),
            "join_date": correct_date(record.get("join_date")),
        }
        processed_data.append(processed_entry)
    return processed_data

data = [
    {"name": "alice smith", "age": 30, "email": "alice@example.com", "salary": 50000.00, "join_date": "2022-03-15"},
    {"name": "bob gray", "age": 17, "email": "bob@not-an-email", "salary": 60000.00, "join_date": "invalid-date"},
    {"name": "charlie brown", "age": None, "email": "charlie@example.com", "salary": -1500.00, "join_date": "15-09-2022"},
    {"name": "dave davis", "age": 45, "email": "dave@example.com", "salary": 70000.00, "join_date": "2021-07-01"},
    {"name": "eve green", "age": 25, "email": "eve@example.com", "salary": None, "join_date": "2023-12-31"},
]

processed_data = process_data(data)

for entry in processed_data:
    print(entry)
