FACTOR_C_TO_F = 9 / 5
FACTOR_F_TO_C = 5 / 9

def celsius_to_fahrenheit(celsius):
    return celsius * FACTOR_C_TO_F + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FACTOR_F_TO_C

def main():
    print("Temperature Conversion Tool")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        choice = int(input("Choose conversion (1 or 2): "))
        if choice == 1:
            temp = float(input("Enter temperature in Celsius: "))
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {result:.2f}°F")
        elif choice == 2:
            temp = float(input("Enter temperature in Fahrenheit: "))
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {result:.2f}°C")
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    main()
