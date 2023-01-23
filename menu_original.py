from classes import PolicyDatabase, Policyholder

db = PolicyDatabase()

class NameError(ValueError):
    pass

def has_numbers(input):
    return any(char.isdigit() for char in input)

def get_inputs():

    try:
        name = input("Please enter the holder's name: ")
        surname = input("Please enter the holder's surname: ")
        if has_numbers(surname):
            raise NameError("Surname may contain only alphabetic characters")
        age = int(input("Please enter the holder's age: "))
        phone = int(input("Please enter the holder's phone number: "))
        return (name, surname, age, phone)
    except NameError as err:
        print(err)
        return None
    except ValueError:
        print("Phone and age need to provide a valid number!")
        return None



def print_holders(holders):
    if holders:
        for holder in holders:
            print(holder)

def search():
    name = input("Please enter the name which you wish to find: ")
    surname = input("Please enter the surname which you wish to find: ")
    if (not name) and (not surname):
        return False
    elif name and surname:
        return db.find_policy_holder_by_complete_name(name, surname)
    elif name:
        return db.find_policy_holder_by_name(name)
    elif surname:
        return db.find_policy_holder_by_surname(surname)

def menu_search():
    holders = search()
    if holders:
        print_holders(holders)
    else:
        print("Invalid Search Input!")

def menu_new_holder():
    new_holder_data = get_inputs()
    if new_holder_data:
        new_holder = Policyholder(*new_holder_data)
        if new_holder:
            db.add_policy_holder(new_holder)
    else:
        print("Invalid Holder Entry!")

def menu_database():
    holders = db.get_policy_holders()
    if holders:
        print_holders(holders)
    else:
        print("No Data in the Database! Add new policy holder first!\n")
        menu_new_holder()

def menu():
    print()
    print("________Welcome to your insurance application________\n")
    print("What would you like to do? \n")
    commands = ["New Holder", "Database", "Search", "Exit"]
    command = ""
    while True:
        print(f"Commands: {commands}")

        command = input("Enter command: ")
        command = " ".join(command.split()).lower()
        if command not in [x.lower() for x in commands]:
            print("Command Not Found!")
            continue
        elif command == "New Holder".lower():
            menu_new_holder()
        elif command == "Database".lower():
            menu_database()
        elif command == "Search".lower():
            menu_search()
        elif command == "Exit".lower():
            exit()