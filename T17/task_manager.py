# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"
username_password = {}

#====Get Tasks Section====
''' Initialises a dictionary based on data inside 
    tasks.txt or creates a blank file '''
def get_tasks():
# Create tasks.txt if it doesn't exist
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w") as default_file:
            pass

    # Open tasks.txt if already exists
    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    # Define task_list as an empty list
    task_list = []

    for task_string in task_data:
        curr_t = {}
        # Split by semicolon and manually add each component
        task_components = task_string.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[5] == "Yes" else False

        task_list.append(curr_t)
    return task_list

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.'''
def login():
    global username_password
    global curr_user

    # If no user.txt file, write one with a default account
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")
    else:
    # Read in user_data
        with open("user.txt", 'r') as user_file:
            user_data = user_file.read().split("\n")

# Convert to a dictionary
    username_password = {}
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password

    logged_in = False
    while not logged_in:
        
        print("LOGIN")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")
        if curr_user not in username_password.keys():
            print("User does not exist")
            continue
        elif username_password[curr_user] != curr_pass:
            print("Wrong password")
            continue
        else:
            print("Login Successful!")
            logged_in = True
            return logged_in, username_password

#====Menu Options====
menu_list = '''Select one of the following options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit'''

#====Registering New Users====
def reg_user():
    # Get user input for username and password    
    while True:
        new_username = input("New Username: ")
        if new_username in username_password:
            print("Duplicate user. Please create a unique user:")
            continue
        else:
            pass
            
            # - Request input of a new password
        new_password = input("New Password: ")

            # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

            # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
                
            with open("user.txt", "w") as out_file:
                user_data = [f"{k};{username_password[k]}" for k in username_password] # 
                out_file.write("\n".join(user_data))
            break

            # - Otherwise you present a relevant message.
        else:
                print("Passwords do no match")
    
#====Add Task Function====
''' Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
         - A username of the person whom the task is assigned to,
         - A title of a task,
         - A description of the task and 
         - the due date of the task. '''
def add_task():
        while True:
            # Get username to assign task 
            task_username = input("Name of person assigned to task: ")
            if task_username not in username_password.keys(): # Check if in user.txt
                print("User does not exist. Please enter a valid username")
                continue

            # Title, Description & Due date values
            task_title = input("Title of Task: ")
            task_description = input("Description of Task: ")

            # Check if date is formatted correctly
            while True:
                try:
                    task_due_date = input("Due date of task (YYYY-MM-DD): ")
                    due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                    break

                except ValueError:
                    print("Invalid datetime format. Please use the format specified")

            # Get the current date and assign to assigned_date
            curr_date = date.today()
            
            # Build new task as dictionary
            new_task = {
                "username": task_username,
                "title": task_title,
                "description": task_description,
                "due_date": due_date_time,
                "assigned_date": curr_date,
                "completed": False
            }

            # Add to task list
            task_list.append(new_task)
            with open("tasks.txt", "w") as task_file:
                # Create new list with all of the previous tasks and the new one
                task_list_to_write = []
                for t in task_list:
                    str_attrs = [
                        t['username'],
                        t['title'],
                        t['description'],
                        t['due_date'].strftime(DATETIME_STRING_FORMAT),
                        t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if t['completed'] else "No"
                    ]
                    # Seperate values with ; to parse later and rewrite tasks.txt
                    task_list_to_write.append(";".join(str_attrs))
                task_file.write("\n".join(task_list_to_write))
            print("Task successfully added.")
            break

#====View All function====
''' Reads the task from task.txt file and prints to the console 
    in the format of Output 2 presented in the task pdf 
    (i.e. includes spacing and labelling) '''
def view_all():

        for t in task_list:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)

#====View Mine function====
''' Reads the tasks from task.txt file and returns tasks assigned 
    to the current user logged in and allow user to edit values
    (Completed?/Username/Due date) '''
def view_mine():
        # Create list of tasks with the same username that is logged in
        my_tasks = [task for task in task_list if task['username'] == curr_user]
        if not my_tasks:
            print("You dont have any tasks assigned.")
            return
        
        # Enumerate list and print it
        for i, task in enumerate(my_tasks, start=1):
            disp_str = f"{i}. Task: \t {task['title']}\n"
            disp_str += f"Assigned to: \t {task['username']}\n"
            disp_str += f"Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n--{task['description']}\n"
            print(disp_str)
        
        # Call function to edit selected task
        get_task_input(my_tasks)
        return my_tasks
        
#====Users choice====
''' For selecting individual tasks and editing them'''
def get_task_input(my_tasks):
    # Task menu for user to select a task and interact with it
    while True:
        choice = input("\nSelect a task number or -1 to go back: ")
        if choice == "-1":
            break
        try:
            choice = int(choice) - 1  # Convert to int and adjust for indexing
            if 0 <= choice < len(my_tasks):
                selected_task = my_tasks[choice] # Users choice relating to enumerated list
                
                print("Selected task:\n",selected_task['title'],"\n",selected_task['description'],"\n")
                
                # Option to mark as complete
                selection = input(f"Would you like to mark \"{selected_task['title']}\" as complete? (yes/no): ").lower()
                if selection == "yes": # Change value to True and update tasks.txt file
                    selected_task['completed'] = True
                    print(f"\nTask set to: {selected_task['completed']}\n")
                    update_tasks_file()
                    break
                elif selection == "no":
                    selection = input("Ok, would you like to edit the task? (yes/no): ").lower()
                # Option to edit task values using the edit_task() function
                if selection == "yes":
                    edit_task(selected_task) # Run edit task function
                elif selection == "no":
                    print("No changes made...\n")
                    view_mine() # Print tasks and return to the start
                    break
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number or -1.")

#====Edit Task function====
''' Options to edit tasks '''
def edit_task(task):
    # Option to change the username
    print(f"\nCurrent assigned user: {task['username']}")
    username = input("Enter new username or leave blank to skip: ")
    if username:
        task['username'] = username

    # Option to change the title
    print(f"Current title: {task['title']}")
    title = input("Enter new title or leave blank to skip: ")
    if title:
        task['title'] = title

    # Option to change the due date
    print(f"Current Due Date: {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
    new_due_date = input("Enter new due date (YYYY-MM-DD) or leave blank to skip: ")
    
    # Check if correct date format
    if new_due_date:
        try:
            task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                # Update task file and print confirmation
            update_tasks_file()
            print("Task updated successfully.\n")
        except ValueError:
            print("Invalid date format. No changes made to due date.")

#====Update Task File====
''' Rewrite task.txt with updated/new task''' 
def update_tasks_file():
    with open("tasks.txt", "w") as task_file:
        for t in task_list:
            task_line = f"{t['username']};{t['title']};{t['description']};{t['due_date'].strftime(DATETIME_STRING_FORMAT)};{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)};{'Yes' if t['completed'] else 'No'}"

            task_file.write(task_line + "\n")
    print("Tasks file updated.\n")

#========== MAIN ==========

task_list = get_tasks()
login()

# presenting the menu to the user and 
# making sure that the user input is converted to lower case.
while True:
    print()
    print(menu_list)
    menu = input("Enter Choice: ").lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()


    elif menu == 'va':
        view_all()
            

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        print("\nWe are working on thisd....\n")
        
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    
    
    elif menu == 'ds' and curr_user != 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        

        print("-----------------------------------")
        print(f"You do not have permission to access \"Display Statistics\"")
        print("-----------------------------------")    
    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")