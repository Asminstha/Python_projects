def save_note():
    note = input("Enter your note: ")
    with open("my_notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved successfully.")

def view_notes():
    try:
        with open("my_notes.txt", "r") as file:
            notes = file.readlines()
            print("\nYour Notes:")
            for i, line in enumerate(notes, start=1):
                print(f"{i}. {line.strip()}")
    except FileNotFoundError:
        print("No notes found. Start by adding one!")

while True:
    print("\nOptions: add | view | exit")
    choice = input("Choose an option: ").lower()
    if choice == "add":
        save_note()
    elif choice == "view":
        view_notes()
    elif choice == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
