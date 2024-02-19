from tkinter import *
from functools import partial

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
        
        # Set up GUI Frame
        self.temp_frame = Frame()
        self.temp_frame.grid()

        # Header label
        self.temp_heading = Label(self.temp_frame, 
                                  text="Temperature Converter",
                                  font=("Arial", 16, "bold")
                                  )
        self.temp_heading.grid(row=0)

        # Instructions label
        instructions = "Please enter a temperature below and"\
                        " then press one of the buttons to convert " \
                        "it from centigrade to Fahrenheit."
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wrap=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)
        
        # Entry widget for user input
        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        # Error message label
        self.output_label = Label(self.temp_frame, 
                                  text="",
                                  fg="#9C0000"
                                  )
        self.output_label.grid(row=3)

        # Button frame for conversion and other actions
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # Conversion buttons
        self.to_celsius_button = Button(self.button_frame,
                                        text="To Celsius",
                                        bg="#990099",
                                        fg=button_fg,
                                        font=button_font, width=12,
                                        command=lambda: self.temp_convert(-459))
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)
        
        self.to_fahrenheit_button = Button(self.button_frame,
                                            text="To Fahrenheit",
                                            bg="#009900",
                                            fg=button_fg,
                                            font=button_font, width=12,
                                            command=lambda: self.temp_convert(-273))
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5, pady=5)

        # Other action buttons
        self.to_help_info_button = Button(self.button_frame,
                                          text="Help/Info",
                                          bg="#CC6600",
                                          fg=button_fg,
                                          font=button_font, width=12,
                                          command=self.to_help)
        self.to_help_info_button.grid(row=1, column=0, padx=5, pady=5)
        
        self.to_history_export_button = Button(self.button_frame,
                                                text="History/Export",
                                                bg="#004C99",
                                                fg=button_fg,
                                                font=button_font, width=12,
                                                state=DISABLED)
        self.to_history_export_button.grid(row=1, column=1, padx=5, pady=5)

    def to_help(self):
        # Disable the help button when the help dialog is opened
        self.to_help_info_button.config(state=DISABLED)
        # Open the help dialog
        DisplayHelp(self)

    # Function to check the validity of the entered temperature
    def check_temp(self, low_val):
        has_error = False
        error = f"Please enter a number higher than or equal to {low_val}."

        response = self.temp_entry.get()
        
        try:
            temp = float(response)
            if temp <= low_val - 0.000001:
                has_error = True 
        
        except ValueError:
            has_error = True  

        if has_error:
            self.var_has_error.set("yes") 
            self.var_feedback.set(error)  
            return "invalid"
        else:
            self.var_has_error.set("no")  
            self.to_history_export_button.config(state=NORMAL)  
            return temp  
    
    # Function to round the result to the nearest whole number
    @staticmethod
    def round_ans(val):
        var_rounded = (val * 2 + 1) // 2 
        return "{:.0f}".format(var_rounded)
    
    # Function to convert temperature and display the result
    def temp_convert(self, low_val):
        to_convert = self.check_temp(low_val)
        deg_sign = u'\N{DEGREE SIGN}'
        set_feedback = "yes"
        answer =""
        from_to=""
                    
        if to_convert == "invalid":
            set_feedback = "no"
        
        elif low_val == -459:
            answer = (to_convert - 32) * 5 / 9
            from_to = "{} F{} is {} C{}" 
        
        else:
            answer = to_convert * 1.8 + 32  
            from_to = "{} C{} is {} F{}"
        
        if set_feedback == "yes":
            to_convert = self.round_ans(to_convert)
            answer = self.round_ans(answer)
            
            feedback = from_to.format(to_convert, deg_sign, answer, deg_sign)
            self.var_feedback.set(feedback)
            
            self.all_calculations.append(feedback)

            # Delete code below when history component is working!
            print(self.all_calculations)
        
        self.output_answer()
    
    # Function to display the output and handle formatting
    def output_answer(self):
        output = self.var_feedback.get() 
        has_errors = self.var_has_error.get()  

        if has_errors == "yes":
            self.output_label.config(fg="#9C0000") 
            self.temp_entry.config(bg="#F8CECC")  
        else:
            self.output_label.config(fg="#004C00")  
            self.temp_entry.config(bg="#FFFFFF")  
        
        self.output_label.config(text=output)


class DisplayHelp:
    
    def __init__(self, partner):
        background = "#ffe6cc"
        self.partner = partner
        self.help_box = Toplevel()

        # If users press cross at top, closes help and
        # 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))
        self.help_frame = Frame(self.help_box, width=300, height=200,
                                bg=background)
        self.help_frame.grid()

        
        self.help_heading_label = Label(self.help_frame, bg=background,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)
        help_text = """To use the program, simply enter the temperature
you wish to convert and then choose to convert 
to either degrees Celsius (centigrade) or 
Fahrenheit.. \n\n

Note that -273 degrees C 
(-459 F) is absolute zero (the coldest possible 
temperature). If you try to convert a 
temperature that is less than -273 degrees C, 
you will get an error message. \n\n

To see your 
calculation history and export it to a text 
file, please click the 'History / Export' button.""" 
        self.help_text_label = Label(self.help_frame, bg=background, 
                                    text=help_text, wrap=350,
                                    justify="left")
        self.help_text_label.grid(row=1, padx=10)

        
        self.dismiss_button = Button(self.help_frame,
                                    font=("Arial", "12", "bold"),
                                    text="Dismiss", bg="#CC6600",
                                    fg="#FFFFFF",
                                    command=partial(self.close_help,
                                                    partner))
        self.dismiss_button.grid(row=2, padx=18, pady=18)
        
    # closes help dialog ( used by button and x at top of dialog)
    def close_help(self, partner):
        # Enable the help button when the help dialog is closed
        self.partner.to_help_info_button.config(state=NORMAL)
        self.help_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
