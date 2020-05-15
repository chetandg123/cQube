# import csv
#
# with open('/home/chetan/Documents/Data_files/District_wise_report.csv', 'r') as file:
#     reader = csv.reader(file)
#     lines = len(list(reader))
#     print(
import csv
import re

str = "no of schools : 4500"
res = re.sub("\D", "", str)
print(res)

with open('/home/chetan/Documents/Data_files/District_wise_report.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    lines = len(list(reader))
    print("no of records in file:", lines)


