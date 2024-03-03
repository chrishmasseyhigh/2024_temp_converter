from datetime import date 
import re

#if filename is blank, returns default name 
# otherwise checks filename and either returns
# an error or retuns the filename ( with .txt extension)
def filename_maker():
    # loops if there is an error
    while True:
        # gets input
        filename = input("Enter filename (leave blank for default): ").strip()
        #sets error
        error = "Filename can only contain letters, numbers, and underscores. Please try again."
        
        # if filename is blank
        if not filename:
            today = date.today()
            date_string = today.strftime("%Y_%m_%d")
            return f"Temperature_Conversions_{date_string}.txt"
        
        # If filename is not blank
        else:
            # if it fits
            if re.match(r'^[a-zA-Z0-9_]+$', filename):
                return f"{filename}.txt"
            # if there is a formating error
            else:
                print(error)

filename = filename_maker()
print(filename)