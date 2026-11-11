# RESISTOR COMBINATION CALCULATOR
# CTE213 Python Mini Project

# This function collects a valid positive resistor value.
def get_resistor_value():
    while True:
        try:
            value = float(input("Enter resistor value (Ohms): "))

            if value > 0:
                return value
            else:
                print("Please enter a value greater than zero.")

        except ValueError:
            print("Invalid input! Enter a number.")


# Calculate total resistance in series.
def calculate_series(resistors):
    total = 0

    for resistor in resistors:
        total += resistor

    return total


# Calculate total resistance in parallel.
def calculate_parallel(resistors):
    reciprocal_sum = 0

    for resistor in resistors:
        reciprocal_sum += 1 / resistor

    return 1 / reciprocal_sum


# This list stores previous calculations.
history = []

# Main program
while True:
    print("\n===== RESISTOR CALCULATOR =====")
    print("1. Calculate resistance")
    print("2. View calculation history")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        try:
            number = int(input("How many resistors do you have? "))

            if number <= 0:
                print("Enter at least one resistor.")

            else:
                resistors = []

                # Collect resistor values.
                for i in range(number):
                    print(f"\nResistor {i + 1}")
                    value = get_resistor_value()
                    resistors.append(value)

                # Perform calculations.
                series = calculate_series(resistors)
                parallel = calculate_parallel(resistors)

                print("\n===== RESULTS =====")
                print(f"Series resistance: {series:.2f} Ohms")
                print(f"Parallel resistance: {parallel:.2f} Ohms")

                # Save results in history.
                history.append(
                    f"Resistors: {resistors}, "
                    f"Series: {series:.2f} Ohms, "
                    f"Parallel: {parallel:.2f} Ohms"
                )

        except ValueError:
            print("Invalid input! Enter a whole number.")

    elif choice == "2":

        if len(history) == 0:
            print("No calculation history yet.")

        else:
            print("\n===== CALCULATION HISTORY =====")

            for record in history:
                print(record)

    elif choice == "3":
        print("Thank you for using the calculator!")
        break

    else:
        print("Invalid choice! Select 1, 2 or 3.")