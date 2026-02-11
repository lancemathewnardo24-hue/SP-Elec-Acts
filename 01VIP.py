# Initialize an empty list to store guest names
guests = []

print("Welcome to the VIP party planner!")
print("Type 'done' when you are finished adding names.")

# Use a while loop to continuously ask for user input
while True:
    # Check if the list has reached 5 names
    if len(guests) == 5:
        print("The party is full!")
        break

    name = input("Enter a guest's name to add to the party list: ").strip()
    
    # Stop the loop if the user types 'done'
    if name.lower() == 'done':
        break

    # Check if the name is already in the list
    if name in guests:
        print("They're already on the list!")
    else:
        # Add the name to the guest list
        guests.append(name)
        print(f"{name} has been added to the list.")

# Print the final guest list alphabetically
print("\nThe final guest list is:")
for guest in sorted(guests):
    print(f"- {guest}")