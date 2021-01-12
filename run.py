import gspread
from oauth2client.service_account import ServiceAccountCredentials

# formats data printed to the terminal so it is easier to read
from pprint import pprint

# Need an explanation as to why all 4 scopes are needed
# What are these scopes and how do they work?
scope = [
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Using the data we got from https://console.cloud.google.com/ to set out our credentials
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

# Using credentails to authorise access to our google sheet
client = gspread.authorize(creds)

# opening our python_automation_test_sheet sheet in google sheets and accessing the first tab of data within it (sheet1)
sheet = client.open("python_automation_test_sheet").sheet1

# Getting all records from sheet1 as a dict
data = sheet.get_all_records()

row = sheet.row_values(3)
col = sheet.col_values(2)
cell = sheet.cell(2, 3).value

# Inserting data into sheet

# insert entire row

insertRow = ["Anna", 40, "cyan"]
# sheet.insert_row(insertRow, 4) This doesn't override, it just pushes the other cells down to make room

# sheet.delete_row(4) deletes the selected row, moves other cells up

# sheet.update_cell(2, 2, "CHANGED") updates a specific cell

""" getting number of rows and columns """

# num_rows = sheet.row_count gives the number of rows in the sheet (standard is 1000) even if no data in them

# pprint(len(data)) gives number of data entries (rows)

# pprint(num_rows)

# sheet.append_row(insertRow)  adds a new row to the sheet

# print(dir(sheet))


def calculate_average(nums):
    """
    Function to convert numbers in list into integers 
    and then return the average of the numbers
    """
    int_nums = [int(i) for i in nums] 
    return sum(int_nums) / len(int_nums)


ages = sheet.col_values(2)
ages.pop(0) # removes column heading
average_ages = calculate_average(ages)
print(average_ages)
