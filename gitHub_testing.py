def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def main():
    print("=============================")
    print("Temperature Converter v1.0")
    print("Testing GitHub Changes!")
    print("=============================")
    
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {result:.1f}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {result:.1f}°C")
    elif choice == "3":
        celsius = float(input("Enter temperature in Celsius: "))
        result = celsius_to_kelvin(celsius)
        print(f"{celsius}°C is equal to {result:.1f}K")
    elif choice == "4":
        kelvin = float(input("Enter temperature in Kelvin: "))
        result = kelvin_to_celsius(kelvin)
        print(f"{kelvin}K is equal to {result:.1f}°C")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
