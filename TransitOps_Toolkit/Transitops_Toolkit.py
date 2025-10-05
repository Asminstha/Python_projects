"""


This single Python 3 file implements 10 independent programming tasks
(as console functions behind a simple menu) using only concepts
 (variables, input/output, conditionals,
loops, lists/tuples, and basic functions).

"""


# Utility helpers (basic only)


CURRENT_YEAR = 2025
CURRENT_MONTH = 10
CURRENT_DAY = 3


def read_int(prompt):
    """Read an integer with retry until valid."""
    while True:
        raw = input(prompt).strip()
        if raw.startswith("+") or raw.startswith("-"):
            sign = 1 if raw[0] == "+" else -1
            rest = raw[1:]
        else:
            sign = 1
            rest = raw
        if rest.isdigit() and rest != "":
            try:
                return sign * int(rest)
            except Exception:
                pass
        print("  Invalid integer. Please try again.")


def read_float(prompt):
    """Read a float with retry until valid (simple checker)."""
    while True:
        raw = input(prompt).strip()
        try:
            # float() accepts scientific notation; allowed here.
            return float(raw)
        except Exception:
            print("  Invalid number. Please try again.")


def read_nonempty(prompt):
    """Non-empty text input."""
    while True:
        s = input(prompt).strip()
        if s != "":
            return s
        print("  This cannot be empty. Try again.")


def confirm_yes_no(prompt):
    """Return True for yes, False for no."""
    while True:
        s = input(prompt + " (y/n): ").strip().lower()
        if s in ("y", "yes"):
            return True
        if s in ("n", "no"):
            return False
        print("  Please enter 'y' or 'n'.")


def basic_email_ok(email):
    """Very basic email check: contains '@' and '.' and no spaces."""
    return ("@" in email) and ("." in email) and (" " not in email)


def basic_mobile_ok(mobile):
    """Mobile: exactly 10 digits."""
    return mobile.isdigit() and len(mobile) == 10


def calc_age_from_dob(y, m, d):
    """Compute age in years relative to CURRENT_* (no datetime import)."""
    age = CURRENT_YEAR - y
    before_birthday = (m, d) > (CURRENT_MONTH, CURRENT_DAY)
    if before_birthday:
        age -= 1
    return age


def kg_from_pounds(lb):
    return lb * 0.453592


def round_to_nearest_positive(value):
    """Round to nearest whole number and ensure positive."""
    # If user accidentally enters negative, make it positive as per note.
    return abs(int(round(value)))


# Global "storage" for tasks 1 and 10
# (parallel lists per brief for Task 10)

user_names = []          # index-aligned
user_emails = []         # index-aligned
user_passwords = []      # index-aligned
user_prefs = []          # index-aligned: dictionary-like strings, e.g. {'newsletter': True, 'promos': False}


# Some seed tracking data for Task 7 (Delivery Tracking)
tracking_numbers = ["A00001D", "A00002D", "A99999D"]
tracking_statuses = ["In transit", "Out for delivery", "Delivered"]



# Task 1: Customer Details


def task1_customer_details():
    print("\n--- Task 1: Customer Details ---")
    name = read_nonempty("Enter full name: ")
    mobile = read_nonempty("Enter 10-digit mobile number: ")
    address = read_nonempty("Enter address: ")
    email = read_nonempty("Enter email address: ")
    print("Enter Date of Birth:")
    dob_year = read_int("  Year (YYYY): ")
    dob_month = read_int("  Month (1-12): ")
    dob_day = read_int("  Day (1-31): ")

    # Validations
    valid = True
    errors = []

    if not basic_mobile_ok(mobile):
        valid = False
        errors.append("- Mobile number must be exactly 10 digits.")

    if not basic_email_ok(email):
        valid = False
        errors.append("- Email address format seems invalid.")

    # Validate simple month/day ranges
    if not (1 <= dob_month <= 12):
        valid = False
        errors.append("- Month must be between 1 and 12.")
    if not (1 <= dob_day <= 31):
        valid = False
        errors.append("- Day must be between 1 and 31.")

    age = calc_age_from_dob(dob_year, dob_month, dob_day)

    if age <= 21:
        valid = False
        errors.append("- Registration requires age greater than 21.")

    if valid:
        print("\nRegistration successful! Details:")
        print("  Name   :", name)
        print("  Mobile :", mobile)
        print("  Address:", address)
        print("  Email  :", email)
        print("  DOB    : %04d-%02d-%02d (Age: %d)" % (dob_year, dob_month, dob_day, age))

        # Also store into Task 10 parallel lists (if unique email)
        if email in user_emails:
            print("\nNote: Email already exists in account store; skipping auto-add to accounts.")
        else:
            # Create a simple initial password (user can change in Task 10)
            default_pw = "Temp@123"
            user_names.append(name)
            user_emails.append(email)
            user_passwords.append(default_pw)
            user_prefs.append({"newsletter": False, "promos": False})
            print("An account has been created for you (Task 10 store). Temporary password:", default_pw)
    else:
        print("\nRegistration failed due to:")
        for e in errors:
            print(e)



# Task 2: Vehicle Capacity


def task2_vehicle_capacity():
    print("\n--- Task 2: Vehicle Capacity ---")
    length_m = read_float("Enter vehicle length (m): ")
    width_m = read_float("Enter vehicle width (m): ")
    height_m = read_float("Enter vehicle height (m): ")

    volume_m3 = length_m * width_m * height_m
    capacity_kg = volume_m3 * 100.0  # 1 m3 holds 100 kg

    if capacity_kg > 5000.0:
        print("Calculated weight capacity is %.2f kg, but maximum allowed is 5000 kg." % capacity_kg)
        capacity_kg = 5000.0

    print("Maximum weight capacity: %.2f kg" % capacity_kg)



# Task 3: Delivery Time Estimation


def task3_delivery_time():
    print("\n--- Task 3: Delivery Time Estimation ---")
    distance = read_float("Enter route distance (km): ")
    speed = read_float("Enter average speed (km/h): ")

    if speed <= 0:
        print("  Speed must be greater than 0.")
        return

    hours = distance / speed
    total_hours = hours
    if hours > 15:
        total_hours += 8  # add rest time
        print("Base time: %.2f h. Added 8 h rest for long trip." % hours)

    print("Estimated delivery time: %.2f hours" % total_hours)



# Task 4: Calculate Total Cost


def task4_total_cost():
    print("\n--- Task 4: Calculate Total Cost ---")
    weight_kg = read_float("Enter goods weight (kg): ")
    distance_km = read_float("Enter delivery distance (km): ")

    weight_kg_rounded = round_to_nearest_positive(weight_kg)
    cost_per_km_per_kg = 0.10
    base_cost = weight_kg_rounded * distance_km * cost_per_km_per_kg

    if distance_km > 100:
        discount = 0.05 * base_cost
    else:
        discount = 0.0

    total = base_cost - discount
    if total < 30.0:
        total = 30.0

    print("Rounded weight (kg):", weight_kg_rounded)
    print("Base cost: $%.2f" % base_cost)
    print("Discount:  $%.2f" % discount)
    print("Total due: $%.2f" % total)



# Task 5: Route Optimization


def task5_route_optimization():
    print("\n--- Task 5: Route Optimization ---")
    destinations = []
    distances = []
    for i in range(3):
        name = read_nonempty("Enter destination %d name: " % (i + 1))
        dist = read_float("Enter distance to '%s' from warehouse (km): " % name)
        destinations.append(name)
        distances.append(dist)

    # Create list of (index, name, distance). Sort by distance desc.
    # Stable sort ensures earlier-entered stays first when distances tie.
    items = []
    for i in range(3):
        items.append((i, destinations[i], distances[i]))

    # Sort by distance descending using simple bubble sort (to stick to basics)
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][2] < items[j + 1][2]:
                items[j], items[j + 1] = items[j + 1], items[j]

    print("Optimized visit order (longest first), then return to warehouse:")
    for i, it in enumerate(items):
        print("  %d) %s (%.2f km)" % (i + 1, it[1], it[2]))
    print("  Return to warehouse at the end.")



# Task 6: Goods Classification


def task6_goods_classification():
    print("\n--- Task 6: Goods Classification ---")
    lb = read_float("Enter item weight (pounds): ")
    kg = kg_from_pounds(lb)

    if kg < 10:
        cat = "Lightweight"
    elif kg <= 50:
        cat = "Mediumweight"
    elif kg <= 120:
        cat = "Heavyweight"
    else:
        cat = "Must be divided in small sizes"

    print("Weight in kg: %.2f -> Category: %s" % (kg, cat))



# Task 7: Delivery Tracking


def task7_delivery_tracking():
    print("\n--- Task 7: Delivery Tracking ---")
    print("Example acceptable tracking number formats like: A00001D, A00002D, A99999D")
    tnum = read_nonempty("Enter tracking number to check: ").upper().strip()

    # Basic format check: start with 'A', end with 'D', length between 5 and 10
    if not (tnum.startswith("A") and tnum.endswith("D") and 5 <= len(tnum) <= 10):
        print("Invalid format. It should start with 'A', end with 'D', e.g., A00001D")
        return

    # Search in sample data
    found = False
    for i in range(len(tracking_numbers)):
        if tracking_numbers[i] == tnum:
            print("Status for %s: %s" % (tnum, tracking_statuses[i]))
            found = True
            break

    if not found:
        print("Tracking number not found in our records.")



# Task 8: Delivery Statistics


def task8_delivery_statistics():
    print("\n--- Task 8: Delivery Statistics ---")
    dests = []
    times = []
    for i in range(3):
        d = read_nonempty("Enter destination %d: " % (i + 1))
        t = read_float("Enter delivery time for '%s' (hours): " % d)
        dests.append(d)
        times.append(t)

    # Compute average, fastest, slowest
    total = 0.0
    for t in times:
        total += t
    avg = total / 3.0

    # Find min/max with indices
    min_i = 0
    max_i = 0
    for i in range(1, 3):
        if times[i] < times[min_i]:
            min_i = i
        if times[i] > times[max_i]:
            max_i = i

    print("Average delivery time: %.2f h" % avg)
    print("Fastest: %.2f h (%s)" % (times[min_i], dests[min_i]))
    print("Slowest: %.2f h (%s)" % (times[max_i], dests[max_i]))



# Task 9: Delivery Schedule


def license_ok(s):
    """Simple license check: alphanumeric and length 6-10 (example format)."""
    if len(s) < 6 or len(s) > 10:
        return False
    return s.isalnum()


def task9_delivery_schedule():
    print("\n--- Task 9: Delivery Schedule ---")
    drivers = []
    licenses = []

    print("License number example: AB123456 (alphanumeric, 6–10 chars)")

    for i in range(3):
        name = read_nonempty("Enter driver %d name: " % (i + 1))
        lic = read_nonempty("Enter %s's license number: " % name)
        while not license_ok(lic):
            print("  Invalid license format. Try again (alphanumeric, 6–10 chars).")
            lic = read_nonempty("Enter %s's license number: " % name)
        drivers.append(name)
        licenses.append(lic)

    num_deliveries = read_int("Enter total number of deliveries available: ")
    if num_deliveries < 0:
        print("  Number of deliveries cannot be negative.")
        return

    base = num_deliveries // 3
    remainder = num_deliveries % 3

    assigned = [base, base, base]
    # The last one can have more if needed (as per brief), so dump all remainder on the last driver
    assigned[2] += remainder

    print("\nAssigned deliveries:")
    for i in range(3):
        print("  %s (License %s): %d deliveries" % (drivers[i], licenses[i], assigned[i]))



# Task 10: Account Settings


def find_user_index_by_email(email):
    for i in range(len(user_emails)):
        if user_emails[i].lower() == email.lower():
            return i
    return -1


def task10_account_settings():
    print("\n--- Task 10: Account Settings ---")
    print("Login required to manage account (email + password).")
    email = read_nonempty("Email: ")
    password = read_nonempty("Password: ")

    idx = find_user_index_by_email(email)
    if idx == -1 or user_passwords[idx] != password:
        print("  Invalid email or password.")
        return

    print("\nWelcome,", user_names[idx])
    while True:
        print("\nAccount Menu:")
        print("  1) Update name")
        print("  2) Update email (must be unique)")
        print("  3) Update password")
        print("  4) Set communication preferences")
        print("  5) View current details")
        print("  0) Exit to main menu")

        choice = read_nonempty("Choose an option: ")
        if choice == "1":
            new_name = read_nonempty("Enter new name: ")
            user_names[idx] = new_name
            print("  Name updated.")
        elif choice == "2":
            new_email = read_nonempty("Enter new email: ")
            if not basic_email_ok(new_email):
                print("  Invalid email format.")
            elif find_user_index_by_email(new_email) != -1:
                print("  This email is already taken by another user.")
            else:
                user_emails[idx] = new_email
                print("  Email updated.")
        elif choice == "3":
            new_pw = read_nonempty("Enter new password: ")
            user_passwords[idx] = new_pw
            print("  Password updated.")
        elif choice == "4":
            print("  Current preferences:", user_prefs[idx])
            news = confirm_yes_no("Subscribe to newsletters?")
            promos = confirm_yes_no("Receive promotional emails?")
            user_prefs[idx] = {"newsletter": news, "promos": promos}
            print("  Preferences saved.")
        elif choice == "5":
            print("\nCurrent Details")
            print("  Name :", user_names[idx])
            print("  Email:", user_emails[idx])
            print("  Prefs:", user_prefs[idx])
        elif choice == "0":
            print("Exiting account settings.")
            break
        else:
            print("  Invalid option.")



# Menu / Main Program


def show_menu():
    print("\n==============================")
    print(" B2B Transport –  ")
    print("==============================")
    print("1) Customer Details (Register)")
    print("2) Vehicle Capacity")
    print("3) Delivery Time Estimation")
    print("4) Calculate Total Cost")
    print("5) Route Optimization")
    print("6) Goods Classification")
    print("7) Delivery Tracking")
    print("8) Delivery Statistics")
    print("9) Delivery Schedule")
    print("10) Account Settings")
    print("0) Exit")


def main():
    print("Welcome to the Menu!!")
    while True:
        show_menu()
        choice = read_nonempty("Select a task (0-10): ")
        if choice == "1":
            task1_customer_details()
        elif choice == "2":
            task2_vehicle_capacity()
        elif choice == "3":
            task3_delivery_time()
        elif choice == "4":
            task4_total_cost()
        elif choice == "5":
            task5_route_optimization()
        elif choice == "6":
            task6_goods_classification()
        elif choice == "7":
            task7_delivery_tracking()
        elif choice == "8":
            task8_delivery_statistics()
        elif choice == "9":
            task9_delivery_schedule()
        elif choice == "10":
            task10_account_settings()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose from 0 to 10.")


if __name__ == "__main__":
    main()
