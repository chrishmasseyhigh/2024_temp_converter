# Checks that input is float or int that is more than 0 (custom error message)           
def num_check_v2(low_val):

    error ="please enter a number higher than {}.".format(low_val)
    # Loops unit right input is entered
    valid= False
    while not valid:
        
        # Gets input
        try:
            response = float(input("Chose a number: "))
            
            if response <= low_val:
                print(error)
            else:
                return response

        # tells user if they have entered the wrong thing    
        except ValueError:
            print(error)