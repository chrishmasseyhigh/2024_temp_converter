# Checks that input is float or int that is more than 0 (custom error message)           
def num_check_v2(question, error, num_type,low_val,High_val):

    # Loops unit right input is entered
    valid= False
    while not valid:
        
        # Gets input
        try:
            response = num_type(input(question))
            
            if response <= low_val:
                print(error)
            elif response >= High_val:
                print(error)   
            else:
                return response

        # tells user if they have entered the wrong thing    
        except ValueError:
            print(error)

# *** Main routine ***

to_check=num_check_v2("temp","error",float,-34,10000000000)