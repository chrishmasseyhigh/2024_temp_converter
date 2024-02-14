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
    