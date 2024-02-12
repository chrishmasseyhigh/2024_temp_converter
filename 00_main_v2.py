from tkinter import *


class Converter:
    
    def __init__(self):
        
        # Initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")
        # common format for all buttons
        # Arial size 14 bold with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"
        
        # Set up GUI Frame()
        self.temp_frame = Frame()
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, 
                                  text="Temperature Convertor",
                                  font=("Arial", 16, "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and"\
                        "then press one of the buttons to convert " \
                        "it from centigrade to Fahrenheit."
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wrap=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)
        
        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame, 
                                text="",
                                fg="#9C0000"
                                )
        self.temp_error.grid(row=3)

        # Conversion, help and history / export buttons self.button_frame = Frame(self.temp_frame)
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame,
                                        text="To Celsius",
                                        bg="#990099",
                                        fg=button_fg,
                                        font=button_font, width=12,
                                        command=self.to_celsius)
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)
        
        self.to_fahrenheit_button = Button(self.button_frame,
                                            text="To Fahrenheit",
                                            bg="#009900",
                                            fg=button_fg,
                                            font=button_font, width=12)
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_help_info_button = Button(self.button_frame,
                                          text="Help/Info",
                                          bg="#CC6600",
                                          fg=button_fg,
                                          font=button_font, width=12)
        self.to_help_info_button.grid(row=1, column=0, padx=5, pady=5)
        
        self.to_history_export_button = Button(self.button_frame,
                                                text="History/Export",
                                                bg="#004C99",
                                                fg=button_fg,
                                                font=button_font, width=12,
                                                state=DISABLED)
        self.to_history_export_button.grid(row=1, column=1, padx=5, pady=5)

    def num_check_v2(self, low_val):
        has_error = False
        error = f"Please enter a number higher than or equal to {low_val}."

        # Check if the number is valid
        try:
            response = float(self.temp_entry.get())
            if response <= low_val - 0.000001:
                has_error = True
        
        except ValueError:
            has_error = True

        # If there is an error, display the error message
        if has_error:
            self.temp_error.config(text=error, fg="#9C0000")
        else:
            # If there is no error, indicate valid input and enable the history button
            self.temp_error.config(text="Valid input", fg="green")
            self.to_history_export_button.config(state=NORMAL)

    # Check if the temperature is more than -459 and convert it
    def to_celsius(self):
        self.num_check_v2(-459)

# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
