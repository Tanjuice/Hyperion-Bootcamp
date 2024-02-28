

                        # ---------- FUNCTIONS LECTURE ----------
                    


def add_friend(friends_dict):
    while True:
        name = input("Please enter the name of your friend: ")
        email = input("Please enter the email of your friend: ")
        friends_dict.update({email:name})
        user_choice = input("Would you like to add another friend? (y/n): ")
        if user_choice == "n":
            break

def remove_friend(friends_dict):
    if friends_dict:
        print("Please select a friend to remove:\n")
        print("\tName\t\tEmail\n")
        for i, (email, name) in enumerate(friends_dict.items(), 1):
            print(f"{i}\t{name}\t\t{email}")

        while True:
            user_option = input(": ")
            if user_option.isnumeric() and 0 < int(user_option) <= len(friends_dict):
                emails = list(friends_dict.keys())
                friend_email = emails[int(user_option) - 1]
                del friends_dict[friend_email]
                break
            else:
                print("Invalid option!")
                continue
    else:
        print("No friends in list")


def create_invites():
    date = input(" Please enter the date for your party: ")
    location = input(" Please enter the location for your party: ")
    rsvp = input(" Please enter the RSVP date for your party: ")
    username = input(" Please enter your name: ")

    invites = '''Hello {name},

I would like to invite you to my party on {date}
the party will take place at {location}
please RSVP by {rsvp}

Hope to see you there!

Regards,

{username}'''
    
    return invites.format(name="{name}", date=date,
                          location = location, rsvp=rsvp, username=username)


def send_invites(friends_dict, invites):
    if invites != "":
        user_email = input("Please enter your email: ")
        for email, name in friends_dict.items():
            email_str = f"From:\t{user_email}\n"
            email_str += f"To:\t{email}\n"
            email_str += "-"*80
            email_str += "\nSubject: Birthday party invite\n"
            email_str += "-"*80 + "\n"
            email_str += invites.format(name=name)
            email_str += "\n" + "-" * 80 + "\n\n"
            print(email_str)    
    else:
        print("You haven't set up your invite details")

MENU = '''Please select an option below:
1. Add Friend
2. Remove friend from list
3. Create invites
4. Send invites

0. Quit
'''


# ===== MAIN =====

friends = {"James@gmail.com":"James", "Sam@gmail.com":"Sam", "Jan@gmail.com": "Jan"}

invite = ""

while True:
    print("~~~~~~~~~~ Party Planner ~~~~~~~~~~")
    user_option = input(MENU)
    if user_option == "0":
        exit()
    elif user_option == "1":
        add_friend(friends)
    
    elif user_option == "2":
        remove_friend(friends)

    elif user_option == "3":
        invite = create_invites()
    elif user_option == "4":
        send_invites(friends, invite)
    