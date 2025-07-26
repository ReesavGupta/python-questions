while True:
    try:
        age = int(input("Enter your age (1-120): "))
        if 1 <= age <= 120:
            print(f"Cool, your age is within range: {age}")
            break 
        else:
            print("Out of range. Please enter a number between 1 and 120.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
