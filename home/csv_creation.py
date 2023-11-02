
import csv

data = [
    ["name", "domain", "year founded", "industry", "size range", "locality", "country", "linkedin url", "current employee estimate", "total employee estimate"],
    ["ibm", "ibm.com", 1911, "information technology and services", "10001+", "new york, new york, united states", "united states", "linkedin.com/company/ibm", 274047, 716906],
    ["tata consultancy services", "tcs.com", 1968, "information technology and services", "10001+", "bombay, maharashtra, india", "india", "linkedin.com/company/tata-consultancy-services", 190771, 341369],
    ["accenture", "accenture.com", 1989, "information technology and services", "10001+", "dublin, dublin, ireland", "ireland", "linkedin.com/company/accenture", 190689, 455768],
    # Add the rest of your data here
]

csv_file_path = "files/companies_data.csv"

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_file_path}' has been created.")
