contacts = {}

while True:
    name = input("Enter contact name (or 'done' to stop): ")
    if name.lower() == "done":
        break
    phone = input(f"Enter phone number for {name}: ")
    contacts[name] = phone

print("\n--- Contact Book ---")
for name, phone in contacts.items():
    print(f"{name}: {phone}")

# Use set to find unique phone numbers
unique_numbers = set(contacts.values())
print("\nUnique phone numbers:", unique_numbers)
