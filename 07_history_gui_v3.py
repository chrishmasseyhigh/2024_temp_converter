from tkinter import *
from functools import partial  # To prevent unwanted windows
from datetime import date 
import re

class Converter:
    def __init__(self):
        # set filename variable
        self.var_filename = StringVar()
        self.var_todays_date = StringVar()
        # Initialize variables
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        self.all_calculations = []

        # Common format for all buttons
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # Six item list
        self.all_calculations = ['0 F° is -18 C°', '0 C° is 32 F°',
                                '30 F is -1 C°', '30 C° is 86 F°',
                                '40 F is 4 C', '100 C° is 212 F°']

        # Set up GUI Frame
        self.temp_frame = Frame()
        self.temp_frame.grid()

        # Header label
        self.temp_heading = Label(
            self.temp_frame, text="Temperature Converter", font=("Arial", 16, "bold")
        )
        self.temp_heading.grid(row=0)

        # Instructions label
        instructions = (
            "Please enter a temperature below and"
            " then press one of the buttons to convert "
            "it from centigrade to Fahrenheit."
        )
        self.temp_instructions = Label(
            self.temp_frame,
            text=instructions,
            wrap=250,
            width=40,
            justify="left",
        )
        self.temp_instructions.grid(row=1)

        # Entry widget for user input
        self.temp_entry = Entry(self.temp_frame, font=("Arial", "14"))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        # Error message label
        self.output_label = Label(self.temp_frame, text="", fg="#9C0000")
        self.output_label.grid(row=3)

        # Button frame for conversion and other actions
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # Other action buttons
        self.to_history_export_button = Button(
            self.button_frame,
            text="History/Export",
            bg="#004C99",
            fg=button_fg,
            font=button_font,
            width=12,
            state=NORMAL,
            command=lambda: self.to_history(self.all_calculations),
        )
        self.to_history_export_button.grid(row=1, column=1, padx=5, pady=5)

        # *** !! remove when integrating !! ***
        self.to_history_export_button.config(state=NORMAL)

    def to_history(self, all_calculations):
        self.to_history_export_button.config(state=DISABLED)
        DisplayHistory(self, all_calculations, self.to_history_export_button)


class DisplayHistory:
    def __init__(self, partner, calc_list, to_history_export_button):

        # sets max calcs
        max_calcs = 5
        self.var_max_calcs = IntVar()
        self.var_max_calcs.set(max_calcs)

        # functions converts contents of calculation list into a string
        calc_string_text = self.get_calc_string(calc_list)

        self.to_history_export_button = to_history_export_button

        self.partner = partner
        self.history_box = Toplevel()

        # If users press cross at top, closes history and
        # 'releases' history button
        self.history_box.protocol(
            "WM_DELETE_WINDOW", partial(self.close_history, partner)
        )
        self.history_frame = Frame(
            self.history_box, width=300, height=200
        )
        self.history_frame.grid()

        self.history_heading_label = Label(
            self.history_frame,
            text="History / Export",
            font=("Arial", "16", "bold"),
        )
        self.history_heading_label.grid(row=0)

        # customise text and background colour for calc
        # are depending on whether all or only some
        # are shown
        num_calcs = len(calc_list)

        if num_calcs > max_calcs:
            calc_background = "#FFE6CC"  # peach
            showing_all = "Here are your recent calculations" \
                          "({}/{} calculations shown). please export" \
                          "your"\
                          " calculations".format(max_calcs, num_calcs)

        else:
            calc_background = "#B4FACB"  # pale green
            showing_all = "Below is your calculation history."

        # History text and label
        history_text = "{} \n\nAll calculations are shown to " \
                       "the nearest degree.".format(showing_all)

        self.text_instructions_label = Label(self.history_frame,
                                             text=history_text,
                                             width=45, justify="left",
                                             wraplength=300,
                                             padx=10, pady=10)
        self.text_instructions_label.grid(row=1)

        # Display calculation history
        self.all_calcs_label = Label(self.history_frame,
                                     text=calc_string_text,
                                     padx=10, pady=10, bg=calc_background,
                                     width=40, justify="left")
        self.all_calcs_label.grid(row=2)

        # instructions for saving files
        save_text = "Either choose a custom file name (and push " \
                    "<Export>) or simply push <Export> to save your " \
                    "calculations in a text file. If the " \
                    "filename already exists, it will be overwritten!"

        self.save_instructions_label = Label(self.history_frame,
                                             text=save_text,
                                             wraplength=300,
                                             justify="left", width=40,
                                             padx=10, pady=10)
        self.save_instructions_label.grid(row=3)

        # Filename entry widget, white background to start
        self.filename_entry = Entry(self.history_frame,
                                    font=("Arial", "14"),
                                    bg="#ffffff", width=25)
        self.filename_entry.grid(row=4, padx=10, pady=10)

        self.filename_error_label = Label(self.history_frame,
                                           text="Filename error goes here",
                                           fg="#9C0000",
                                           font=("Arial", "12", "bold"))
        self.filename_error_label.grid(row=5)

        self.button_frame = Frame(self.history_frame)
        self.button_frame.grid(row=6)

        self.export_button = Button(self.button_frame,
                                    font=("Arial", "12", "bold"),
                                    text="Export",
                                    bg="#004C99",
                                    fg="#FFFFFF",
                                    width=12, command=self.make_file
                                    )
        self.export_button.grid(row=0, column=0, padx=10, pady=10)

        self.dismiss_button = Button(self.button_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss",
                                     bg="#666666",
                                     fg="#FFFFFF",
                                     command=partial(self.close_history, partner)
                                     )
        self.dismiss_button.grid(row=0, column=1, padx=10, pady=10)

    def get_calc_string(self, var_calculations):
        # get maximum calculations to display
        # (was set in __init__ function)
        max_calcs = self.var_max_calcs.get()
        calc_string = ""

        # work out how many times we need to loop
        # to output either the last five calculations
        # or all the calculations
        if len(var_calculations) >= max_calcs:
            stop = max_calcs
        else:
            stop = len(var_calculations)
        # iterate to all but last item,
        # adding item and line break to calculation string
        for item in range(0, stop - 1):
            calc_string += var_calculations[len(var_calculations)
                                            - item - 1]
            calc_string += "\n"

        # add final item without an extra line break
        # ie: last item on list will be fifth from the end!
        calc_string += var_calculations[-max_calcs]

        return calc_string

    def make_file(self):
        # retrieve filename
        filename = self.filename_entry.get()

        filename_ok = ""

        if filename == "":
            # get date and create defult filename
            date_part = self.get_date()
            filename = "{}_temperature_calculations".format(date_part)

        else:
            # check that filename is valid
            filename_ok = self.check_filename(filename)

        if filename_ok =="":
            filename += ".txt"
            self.filename_error_label.config(text="You are OK")

        else:
            self.filename_error_label.config(Text=filename_ok)
    def get_date(self):
        today = date.today()
        date_string = today.strftime("%Y_%m_%d")
        self.var_date_string.set(date_string)
        return date_string

    
    # Function to check if a filename contains only letters, numbers, and underscores
    def check_filename(filename):
        problem =""
        # regular expression to check filename is valid
        valid_char = "[A-Za-z0-9_]"

        #iterates though filename and checks each letter
        for letter in filename:
            if re.match(valid_char, letter):
                # If the character is valid, continue checking the next character
                continue
            else:
                # If an invalid character is found, set the problem message
                problem = ("Sorry, no '{}'s allowed".format(letter))
                break

        if problem != "":
            # Format the problem message
            problem = "{}. Use letters, numbers, or underscores only.".format(problem)
        return problem



    # closes history dialog (used by button and x at top of dialog)
    def close_history(self, partner):
        self.partner.to_history_export_button.config(state=NORMAL)
        self.history_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
