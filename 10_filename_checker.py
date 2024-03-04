from datetime import date 
import re

def filename_maker(filename):
    if filename =="":
        filename_ok = ""
        date_part = get_date()
        filename = "{}_temperature_calculations".format(date_part)
    else:
        filename_ok = check_filename(filename)

    if filename_ok == "":
        filename += ".txt"
    else:
        filename = filename_ok

    return filename

def get_date():
    today = date.today()
    date_string = today.strftime("%Y_%m_%d")
    return date_string

def check_filename(filename):
    problem =""
    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue
        else:
            problem = ("Sorry, no '{}'s allowed".format(letter))
            break

    if problem != "":
        problem = "{}. Use letters, numbers, or underscores only.".format(problem)
    return problem

# Main routine
test_filenames = ["", "test.txt", "Test It", "test"]

for item in test_filenames:
    checked = filename_maker(item)
    print(checked)
    print()
