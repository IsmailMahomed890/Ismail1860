def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def show_history(conversions):
    print("\n=== Conversion History ===")
    for conv in conversions:
        print(conv)
    print("========================\n")

def main():
    print("=============================")
    print("Temperature Converter v1.2")
    print("Testing GitHub Changes!")
    print("=============================")
    
    conversions = []
    
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    
    while True:
        print("\nOptions:")
        print("1-4: Convert temperature")
        print("h: Show history")
        print("q: Quit")
        
        choice = input("Enter your choice: ")
        
        if choice.lower() == 'q':
            print("Thank you for using the converter!")
            break
        
        if choice.lower() == 'h':
            show_history(conversions)
            continue
            
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please try again.")
            continue

        if choice == "1":
            celsius = get_valid_number("Enter temperature in Celsius: ")
            result = celsius_to_fahrenheit(celsius)
            conversion = f"{celsius}°C = {result:.1f}°F"
            conversions.append(conversion)
            print(conversion)
        elif choice == "2":
            fahrenheit = get_valid_number("Enter temperature in Fahrenheit: ")
            result = fahrenheit_to_celsius(fahrenheit)
            conversion = f"{fahrenheit}°F = {result:.1f}°C"
            conversions.append(conversion)
            print(conversion)
        elif choice == "3":
            celsius = get_valid_number("Enter temperature in Celsius: ")
            result = celsius_to_kelvin(celsius)
            conversion = f"{celsius}°C = {result:.1f}K"
            conversions.append(conversion)
            print(conversion)
        elif choice == "4":
            kelvin = get_valid_number("Enter temperature in Kelvin: ")
            result = kelvin_to_celsius(kelvin)
            conversion = f"{kelvin}K = {result:.1f}°C"
            conversions.append(conversion)
            print(conversion)

if __name__ == "__main__":
    main()
