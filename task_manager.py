import datetime

def load_users(file_path):
    """
    Load user data from the file into a dictionary.

    Args:
        file_path (str): Path to the user file.

    Returns:
        dict: Dictionary with usernames as keys and passwords as values.
    """
    users_info = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users_info[username] = password.strip()  # Remove spaces around password
    except FileNotFoundError:
        print("User file not found.")
    return users_info


# function to load the task
def load_tasks(file_path):
    tasks = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        print("Task file not found.")
    return tasks

def authenticate_user(users_info):
    """
    Authenticate the user.

    Args:
        users_info (dict): Dictionary with usernames and passwords.

    Returns:
        str: Username of the authenticated user.
    """
    while True:
        username = input("Please enter username: ")
        password = input("Please enter password: ")
        if username in users_info and users_info[username] == password:
            print("Login successful!")
            return username
        else:
            print("Invalid username or password. Please try again.")

def register_user():
    """
    Register a new user by appending their username and password to the user file.
    """
    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")
    confirm_password = input("Confirm password: ")
    if new_password == confirm_password:
        try:
            with open("user.txt", "a") as file:
                file.write(f"{new_username},{new_password}\n")
            print("User registered successfully!")
        except Exception as e:
            print(f"Error registering user: {e}")
    else:
        print("Passwords do not match. Registration failed.")

def add_task(username=None):
    """
    Add a new task to the tasks file.

    Args:
        username (str, optional): Username of the person the task is assigned to.
    """
    task_username = username if username else input("Enter username of the person the task is assigned to: ")
    task_title = input("Enter task title: ")
    task_description = input("Enter task description: ")
    task_due_date = input("Enter task due date (e.g., 22 June 2023): ")
    try:
        # Validate date format
        datetime.datetime.strptime(task_due_date, '%d %B %Y')
        creation_date = datetime.datetime.now().strftime('%d %b %Y')
        with open("tasks.txt", "a") as file:
            file.write(f"{task_username}, {task_title}, {task_description}, {creation_date}, {task_due_date}, No\n")
        print("Task added successfully!")
    except ValueError:
        print("Invalid date format. Please use 'DD Month YYYY' (e.g., 22 June 2023).")
    except Exception as e:
        print(f"Error adding task: {e}")

def view_all_tasks():
    """
    View all tasks from the tasks file.
    """
    try:
        with open("tasks.txt", "r") as file:
            print("All Tasks:")
            for line in file:
                task_username, task_title, task_description, creation_date, task_due_date, task_completed = line.strip().split(", ")
                print(f"Assigned to: {task_username}\n"
                      f"Title: {task_title}\n"
                      f"Description: {task_description}\n"
                      f"Creation Date: {creation_date}\n"
                      f"Due Date: {task_due_date}\n"
                      f"Completed: {task_completed}\n")
    except FileNotFoundError:
        print("Tasks file not found.")

def view_my_tasks(username):
    """
    View tasks assigned to the specific user.

    Args:
        username (str): Username of the person whose tasks are to be viewed.
    """
    try:
        with open("tasks.txt", "r") as file:
            print("Your Tasks:")
            for line in file:
                task_username, task_title, task_description, creation_date, task_due_date, task_completed = line.strip().split(", ")
                if task_username == username:
                    print(f"Title: {task_title}\n"
                          f"Description: {task_description}\n"
                          f"Creation Date: {creation_date}\n"
                          f"Due Date: {task_due_date}\n"
                          f"Completed: {task_completed}\n")
    except FileNotFoundError:
        print("Tasks file not found.")

def display_statistics():
    """
    Display statistics about the number of users and tasks.
    """
    try:
        with open("user.txt", "r") as user_file:
            total_users = sum(1 for _ in user_file)
        with open("tasks.txt", "r") as task_file:
            total_tasks = sum(1 for _ in task_file)
        print(f"Total number of users: {total_users}")
        print(f"Total number of tasks: {total_tasks}")
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")

def admin_menu(username):
    """
    Display the admin menu and handle user choices.

    Args:
        username (str): Username of the authenticated admin user.
    """
    while True:
        choice = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - display statistics
e - exit
: ''').lower()
        if choice == 'r':
            register_user()
        elif choice == 'a':
            add_task()
        elif choice == 'va':
            view_all_tasks()
        elif choice == 'vm':
            view_my_tasks(username)
        elif choice == 's':
            display_statistics()
        elif choice == 'e':
            print('Goodbye!!!')
            break
        else:
            print("You have entered an invalid input. Please try again.")

def user_menu(username):
    """
    Display the user menu and handle user choices.

    Args:
        username (str): Username of the authenticated user.
    """
    while True:
        choice = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
        if choice == 'a':
            add_task(username)
        elif choice == 'va':
            view_all_tasks()
        elif choice == 'vm':
            view_my_tasks(username)
        elif choice == 'e':
            print('Goodbye!!!')
            break
        else:
            print("You have entered an invalid input. Please try again.")

def main():
    """
    Main function to run the application.
    """
    users_info = load_users("user.txt")
    username = authenticate_user(users_info)
    if username == 'admin':
        admin_menu(username)
    else:
        user_menu(username)

if __name__ == "__main__":
    main()
