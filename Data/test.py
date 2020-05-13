import csv

with open('/home/chetan/Documents/Data_files/District_wise_report.csv', 'r') as file:
    reader = csv.reader(file)
    lines = len(list(reader))
    print(lines)