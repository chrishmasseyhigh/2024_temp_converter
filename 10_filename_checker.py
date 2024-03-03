from datetime import date 
import re

#if filename is blank, returns default name 
# otherwise checks filename and either returns
# an error or retuns the filename ( with .txt extension)
def filename_maker(filename):

    # creates defult filename
    # (YYYY_MM_DD_temprature calculation)
    if filename =="":

        # set filename to defult if blank for testing purposes
        filename_ok = ""
        date_part = get_date()
        filename = "{}_tempertaure_calculations".format(date_part)

        #checks filename only has a-z / A-Z / undrscores
        else:
            filename_ok = check_filename(filename)
        if filename_ok == "":
            filename += ".txt"

        else:
            filename = filename_ok

# retrives date and creates YYY_MM_DD string
def get_date():
    today = date.today()
    date_string = today.strftime("%Y_%m_%d")

    return date_string
# checks that filename only conatins letters,
# numbers and underscores. Returns either "" if
# ok or the problem if there is an error
def check_filename(filename):
    problem =""
# *** Main routine goes here ****
test_filenames = ["", "test.txt", "Test It", "test"]

for item in test_filenames:
    checked = filenmae_maker(item)
    print(checked)
    print()