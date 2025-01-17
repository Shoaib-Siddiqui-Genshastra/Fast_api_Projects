import re          # Importing re module to use Regex
from datetime import datetime    # Importing dattime module to handle date and time over the data set

# for Capitalizing the 1st letter of Name
def normalize_names(data):

    for item in data:
        item['name'] = item['name'].title()
    return data


# Fixing default age equals 25 if age will be less than of equals to zero
def fix_age(data, default_age=25):

    for item in data:
        if item['age'] is None or item['age'] <= 0:
            item['age'] = default_age
    return data


# Fixing mail id with regex and setting up invalid@example.com as default mail id
def validate_email(data, default_email="invalid@example.com"):

    email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")   #something@something.something
    for item in data:
        if not email_pattern.match(item['email']):
            item['email'] = default_email
    return data


# Fixing salary and setting up 0.0 floating value as default salry
def normalize_salary(data):

# Extracting valid salaries(non-negative and not None)
    valid_salaries = [item['salary']
    for item in data if item['salary'] is not None and item['salary'] >= 0]
# Determining the max salary and setting up 1 if no valid salary exist
    max_salary = max(valid_salaries, default=1)
    for item in data:
# set salary to 0 if  it is None or negative
        if item['salary'] is None or item['salary'] < 0:
            item['salary'] = 0
#Normalize salary as a percentage of the maximum salary
        item['salary'] = (item['salary'] / max_salary) * 100
    return data




# Fixing joining date and setting up the default_date="2023-01-01" and handling the ValueError with try and catch block
def parse_join_date(data, default_date="2023-01-01"):

    for item in data:
        try:
            item['join_date'] = datetime.strptime(item['join_date'], "%Y-%m-%d").date()
        except ValueError:
            try:
                item['join_date'] = datetime.strptime(item['join_date'], "%d-%m-%Y").date()
            except ValueError:
                item['join_date'] = datetime.strptime(default_date, "%Y-%m-%d").date()
      #  item['join_date'] = ['join_date'].strftime("%Y-%m-%d")
    return data


# getting each processed data in return at one place
def process_data(data):

    data = normalize_names(data)
    data = fix_age(data)
    data = validate_email(data)
    data = normalize_salary(data)
    data = parse_join_date(data)
    return data

# Defining the root data set/Frame on which have to process
data = [
    {"name": "alice smith", "age": 30, "email": "alice@example.com", "salary": 50000.00, "join_date": "2022-03-15"},
    {"name": "bob gray", "age": 17, "email": "bob@not-an-email", "salary": 60000.00, "join_date": "invalid-date"},
    {"name": "charlie brown", "age": None, "email": "charlie@example.com", "salary": -1500.00, "join_date": "15-09-2022"},
    {"name": "dave davis", "age": 45, "email": "dave@example.com", "salary": 70000.00, "join_date": "2021-07-01"},
    {"name": "eve green", "age": 25, "email": "eve@example.com", "salary": None, "join_date": "2023-12-31"},

]

processed_data = process_data(data)

# Iterating each date line by line over Processed data with "for" and "in" keywords
for entry in processed_data:
 print(entry)
