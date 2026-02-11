guests = []

print("Welcome to the VIP party planner!")
print("Type 'done' when you are finished adding names.")

while True:
    if len(guests) == 5:
        print("The party is full!")
        break

    name = input("Enter a guest's name to add to the party list: ").strip()
    
    if name.lower() == 'done':
        break

    if name in guests:
        print("They're already on the list!")
    else:
        guests.append(name)
        print(f"{name} has been added to the list.")

print("\nThe final guest list is:")
for guest in sorted(guests):
    print(f"- {guest}")