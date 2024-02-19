from tkinter import *
from functools import partial # To prevent unwanted windows

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

        # Other action buttons
        self.to_history_export_button = Button(self.button_frame,
                                                text="History/Export",
                                                bg="#004C99",
                                                fg=button_fg,
                                                font=button_font, width=12,
                                                state=DISABLED,
                                                command=self.to_history)
        self.to_history_export_button.grid(row=1, column=1, padx=5, pady=5)
        

    def to_history(self):
        DisplayHistory(self)

class DisplayHistory:
    
    def __init__(self, partner):
        background = "#ffe6cc"
        self.history_box = Toplevel()

        # Disable the history button in the partner Converter instance
        partner.to_history_export_button.config(state=DISABLED)

        # If users press cross at top, closes history and
        # 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                    partial(self.close_history,partner))
        self.history_frame = Frame(self.history_box, width=300, height=200,
                                bg=background)
        self.history_frame.grid()

        
        self.history_heading_label = Label(self.history_frame, bg=background,
                                        text="History / Export",
                                        font=("Arial", "14", "bold"))
        self.history_heading_label.grid(row=0)
        history_text = """This section will display the calculation history
and provide options for exporting it to a text file."""
        self.history_text_label = Label(self.history_frame, bg=background, 
                                    text=history_text, wrap=350,
                                    justify="left")
        self.history_text_label.grid(row=1, padx=10)

        
        self.dismiss_button = Button(self.history_frame,
                                    font=("Arial", "12", "bold"),
                                    text="Dismiss", bg="#004C99",
                                    fg="#FFFFFF",
                                    command=partial(self.close_history,
                                                    partner))
        self.dismiss_button.grid(row=2, padx=18, pady=18)
        
    # closes history dialog (used by button and x at top of dialog)
    def close_history(self, partner):
        # Enable the history button when the history dialog is closed
        partner.to_history_export_button.config(state=NORMAL)
        self.history_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()