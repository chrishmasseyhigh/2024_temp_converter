def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def main():
    print("Welcome to the temperature converter!")
    print("You can convert temperatures between Celsius, Fahrenheit, and Kelvin.")
    print("To convert, enter the temperature followed by 'c' for Celsius, 'f' for Fahrenheit, or 'k' for Kelvin.")
    print("For example: 32c, 100f, 273.15k\n")

    while True:
        try:
            temperature_input = input("Enter temperature: ").strip().lower()
            temperature = float(temperature_input[:-1])
            unit = temperature_input[-1]

            if unit == 'c':
                print(f"{temperature}°C is:")
                print(f"{celsius_to_fahrenheit(temperature)}°F")
                print(f"{celsius_to_kelvin(temperature)}K")
            elif unit == 'f':
                print(f"{temperature}°F is:")
                print(f"{fahrenheit_to_celsius(temperature)}°C")
                print(f"{fahrenheit_to_kelvin(temperature)}K")
            elif unit == 'k':
                print(f"{temperature}K is:")
                print(f"{temperature - 273.15}°C")
                print(f"{(temperature - 273.15) * 9/5 + 32}°F")
            else:
                print("Invalid input. Please enter 'c' for Celsius, 'f' for Fahrenheit, or 'k' for Kelvin.")
        except ValueError:
            print("Invalid input. Please enter a valid temperature followed by 'c' for Celsius, 'f' for Fahrenheit, or 'k' for Kelvin.")
        except IndexError:
            print("Invalid input. Please enter a valid temperature followed by 'c' for Celsius, 'f' for Fahrenheit, or 'k' for Kelvin.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()




