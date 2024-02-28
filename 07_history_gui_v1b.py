from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:
    def __init__(self):
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
        
    def to_history(self,all_calculations):
        HistoryExport(self, all_calculations)
        self.to_history_export_button.config(state=DISABLED)



class DisplayHistory:
    def __init__(self, partner, calc_list):
        
        # sets max calcs
        max_calcs =5
        self.var_max_calcs = IntVar()
        self.var_max_calcs.set(max_calcs)
        
        # fuctions converts conents of calcuaton list into a string
        calc_string_text = self.get_calc_string(calc_list)
        
        self.to_history_export_button.config(state=DISABLED)

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
        #are dependung on wether all or only some 
        # are shown
        num_calcs = len(calc_list)
        
        if num_calcs > max_calcs:
            calc_baclground = "#FFE6CC" # peach
            showing_all = "Here are your recent calculations" \
                          "({}/{} calculations shown). please export your"\
                          " calculations"
        
        # History text and label
        history_text = "Below are your recent calculations- " \
                       "showing 3/3 calculations. " \
                       "All calculations are shown to the nearest degree"
        
        self.text_instructions_label = Label(self.history_frame,
                                            text=history_text,
                                            width=45, justify="left",
                                            wraplength=300,
                                            padx=10, pady=10)
        self.text_instructions_label.grid(row=1)
        
        # Display calculation history
        all_calcs_text = "\n".join(reversed(self.partner.all_calculations))
        self.all_calcs_label = Label(self.history_frame,
                                     text=all_calcs_text,
                                     padx=10, pady=10, bg="#ffe6cc",
                                     width=40,justify="left")
        self.all_calcs_label.grid(row=2)
        
        # instructions for saving files
        save_text = "Either choose a custom file name (and push " \
                    "<Export>) or simply push <Export> to save your " \
                    "calculations in a text file. If the " \
                    "filename already exists, it will be overwritten!"
        
        self.save_instructions_label = Label (self.history_frame,
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
                                    width=12
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

    def get_calc_string(self,var_calculations):
        # get maximum calculations to display 
        # (was set in __init__ function) 
        max_calcs = self.var_max_calcs.get() 
        calc_string=""
        
        # work out how many times we need to loop
        # to output either the last five calculations 
        # or all the calculations
        if len(var_calculations) >= max_calcs:
            stop =max_calcs
        else:
            stop = len(var_calculations)
        # iterate to all but last item,
        #adding item and line break to calculation string
        for item in range(0, stop -1):
            calc_string += var_calculations[len(var_calculations)
                                            - item -1]
            calc_string +="\n"

        # add final item without an extra linebreak
        # ie: last item on list will be fifth from the end!
        calc_string += var_calculations[-max_calcs]

        return calc_string



    # closes history dialog (used by button and x at top of dialog)
    def close_history(self,partner):
        self.partner.to_history_export_button.config(state=NORMAL)
        self.history_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
