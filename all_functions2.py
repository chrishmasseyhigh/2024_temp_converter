def num_check_v2(self, low_val):
    error = f"Please enter a number higher than {low_val}."

    try:
        response = self.temp_entry.get()
        response = float(response)
        
        if response <= low_val:
            print(error)
        else:
            return response
    except ValueError:
        print(error)

