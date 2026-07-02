while True:
    print("\n===================================")
    print("      Temperature Converter")
    print("===================================")
    print("Choose the input temperature scale:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "4":
        print("\nThank you for using Temperature Converter!")
        break

    if choice in ["1", "2", "3"]:
        temperature = float(input("Enter the temperature: "))

        if choice == "1":
            fahrenheit = (temperature * 9/5) + 32
            kelvin = temperature + 273.15

            print("\nConverted Temperatures:")
            print(f"Fahrenheit: {fahrenheit:.2f}")
            print(f"Kelvin: {kelvin:.2f}")

        elif choice == "2":
            celsius = (temperature - 32) * 5/9
            kelvin = celsius + 273.15

            print("\nConverted Temperatures:")
            print(f"Celsius: {celsius:.2f}")
            print(f"Kelvin: {kelvin:.2f}")

        elif choice == "3":
            celsius = temperature - 273.15
            fahrenheit = (celsius * 9/5) + 32

            print("\nConverted Temperatures:")
            print(f"Celsius: {celsius:.2f}")
            print(f"Fahrenheit: {fahrenheit:.2f}")

        again = input("\nDo you want to convert another temperature? (Y/N): ").upper()

        if again != "Y":
            print("\nThank you for using Temperature Converter!")
            break

    else:
        print("\n❌ Invalid choice! Please enter 1, 2, 3, or 4.")