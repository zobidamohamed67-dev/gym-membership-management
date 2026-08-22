import os 
import time

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

class Member:
    def __init__(self, first, last, id, status='inactive'):
        self.first = first
        self.last = last
        self.id = id
        self.status = status if status != "" else "inactive"
        

    def info(self):
        return f"""
Name: {self.first} {self.last}
Membership ID: {self.id}
Status: {self.status}"""


members = []

while True:
    print("Welcome to GYM membership management...")
    print("""Choose an action:
    1-Add new member
    2-Display all members
    3-Search for a member
    4-Exit """)


    choice = int(input("Enter your choice: "))
    clear()


    if choice == 1:
        first = input("Enter your first name: ")
        last = input("Enter your last name: ")
        id = int(input("Enter your membership ID: "))
        status = input("Enter the status, OR click ENTER: ")
        print("Member added successfully!")
        input("Press enter to go to the main List...")
        clear()

        new_member = Member(first, last, id, status)
        members.append(new_member)



    elif choice == 2:
        if not members:
            print("There is no members yet!")
        else:
            print("Displaying all members:")
            for u in members:
                print(u.info())
                print("----------------")
            time.sleep(5)
            clear()


    elif choice == 3:
        if not members:
            print("There is no members yet")
            input("Press Enter to go to the main list")
            clear()

        else:
            print("Search by:")
            print("""
1-Membership ID
2-First name
3-Status """)
            search_choice = int(input("Enter your choice: "))
            clear()


            if search_choice == 1:
                print("Searching by ID")
                search = int(input("Enter the ID: "))

                found = False
                for member in members:
                    if member.id == search:
                        print("Member found:")
                        print(f"""
            Name: {member.first} {member.last}
            ID: {member.id}
            Status: {member.status}""")
                        print("-----------------")
                        found = True

                        
                if not found:
                    print("Member not found!")
                time.sleep(5)
                clear()


            elif search_choice == 2:
                print("Searching by First name")
                search = input("Enter the First name: ")

                
                found = False
                for member in members:
                    if member.first == search:
                        print("Member found:")
                        print(f"""
            Name: {member.first} {member.last}
            ID: {member.id}
            Status: {member.status}""")
                        print("-----------------")
                        found = True

                    
                if not found:
                    print("Member not found!")
                time.sleep(5)
                clear()


            elif search_choice == 3:
                print("Searching by Status")
                search = input("Enter the Status: ")
                
                found = False
                for member in members:
                    if member.status == search:
                        print("Member found:")
                        print(f"""
            Name: {member.first} {member.last}
            ID: {member.id}
            Status: {member.status}""")
                        print("-----------------")
                        found = True

                    
                if not found:
                    print("Member not found!")
                time.sleep(5)
                clear()
            else:
                print("Invalid choice, please try again...")
                time.sleep(3)
                clear()


    elif choice == 4:
        clear()
        print("Exiting...")
        time.sleep(3)
        clear()
        break   


    else:
        print("Invalid choice, please try again...")
        time.sleep(3)
        clear()