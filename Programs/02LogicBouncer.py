# Logic Bouncer Program

# Get user input
age = int(input("Enter your age: "))
membership = input("Do you have a membership card? (yes/no): ").strip().lower()

# Check conditions
if age < 18:
    print("Denied.")
elif 18 <= age <= 20:
    print("Cannot buy drinks.")
elif age >= 21:
    if membership == "yes":
        print("Welcome, Gold Member!")
    else:
        print("Standard entry granted.")