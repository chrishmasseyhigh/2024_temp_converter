def num_check_v2(input_value, low_val):
    error = f"Please enter a number higher than {low_val}."

    while True:
        try:
            response = float(input_value)
            if response <= low_val:
                print(error)
                return False
            else:
                return True
        except ValueError:
            print(error)
            return False