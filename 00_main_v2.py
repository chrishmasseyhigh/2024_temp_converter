from tkinter import *


class Converter:
    
    def __init__(self):
        
        # Initialize variables
        self.var_feedback = StringVar()  
        self.var_feedback.set("")        

        self.var_has_error = StringVar()  
        self.var_has_error.set("no")     
        
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
                                        command=self.to_celsius)
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)
        
        self.to_fahrenheit_button = Button(self.button_frame,
                                            text="To Fahrenheit",
                                            bg="#009900",
                                            fg=button_fg,
                                            font=button_font, width=12,
                                            command=self.to_fahrenheit)
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5, pady=5)

        # Other action buttons
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

    # Function to check the validity of the entered temperature
    def check_temp(self, low_val):
        has_error = False  # Initialize error indicator to False
        error = f"Please enter a number higher than or equal to {low_val}."

        # Get the user input
        response = self.temp_entry.get()
        
        try:
            # Try converting the input to float
            temp = float(response)
            # Checks if the temperature is within the valid range
            if temp <= low_val - 0.000001:
                has_error = True 
        
        except ValueError:
            has_error = True  

        # If there's an error, update feedback message and return False
        if has_error:
            self.var_has_error.set("yes") 
            self.var_feedback.set(error)  
            return False
        else:
            self.var_has_error.set("no")  
            self.to_history_export_button.config(state=NORMAL)  
            return temp  
    
    # Function to convert the temperature to Celsius
    def to_celsius(self):
        # Check the validity of the temperature input
        to_convert = self.check_temp(-459)
        if to_convert:
            # If input is valid, update feedback message with conversion information
            self.var_feedback.set("Converting {} to C".format(to_convert))
        
        self.output_answer()
    
    # Function to convert the temperature to Fahrenheit
    def to_fahrenheit(self):
        # Check the validity of the temperature input
        to_convert = self.check_temp(-273)
        if to_convert:
            # If input is valid, update feedback message with conversion information
            self.var_feedback.set("Converting {} to F"
                                .format(to_convert))
        
        self.output_answer()

    # Function to display the output and handle formatting
    def output_answer(self):
        output = self.var_feedback.get() 
        has_errors = self.var_has_error.get()  

        # Format the error message label and entry widget background based on error indicator
        if has_errors == "yes":
            self.output_label.config(fg="#9C0000") 
            self.temp_entry.config(bg="#F8CECC")  
        else:
            self.output_label.config(fg="#004C00")  
            self.temp_entry.config(bg="#FFFFFF")  
        
        # Update the error message label with the feedback message
        self.output_label.config(text=output)

# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
