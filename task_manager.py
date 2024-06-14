import datetime

# Function to load user data from the file into a dictionary
def load_users(file_path):
    users_info = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users_info[username] = password
    except FileNotFoundError:
        print("User file not found.")
    return users_info

# Function to authenticate the user
def authenticate_user(users_info):
    while True:
        username = input("Please enter username: ")
        password = input("Please enter password: ")
        if username in users_info and users_info[username] == password:
            print("Login successful!")
            return username
        else:
            print("Invalid username or password. Please try again.")

# Function to register a new user
def register_user():
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

# Function to add a new task
def add_task(username=None):
    task_username = username if username else input("Enter username of the person the task is assigned to: ")
    task_title = input("Enter task title: ")
    task_description = input("Enter task description: ")
    task_due_date = input("Enter task due date (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(task_due_date, '%Y-%m-%d')  # Validate date format
        with open("tasks.txt", "a") as file:
            file.write(f"{task_username}, {task_title}, {task_description}, {task_due_date}, No\n")
        print("Task added successfully!")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
    except Exception as e:
        print(f"Error adding task: {e}")

# Function to view all tasks
def view_all_tasks():
    try:
        with open("tasks.txt", "r") as file:
            print("All Tasks:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Tasks file not found.")

# Function to view tasks assigned to a specific user
def view_my_tasks(username):
    try:
        with open("tasks.txt", "r") as file:
            print("Your Tasks:")
            for line in file:
                task_username, *_ = line.strip().split(", ")
                if task_username == username:
                    print(line.strip())
    except FileNotFoundError:
        print("Tasks file not found.")

# Function to display statistics (for admin)
def display_statistics():
    try:
        with open("user.txt", "r") as user_file:
            total_users = sum(1 for _ in user_file)
        with open("tasks.txt", "r") as task_file:
            total_tasks = sum(1 for _ in task_file)
        print(f"Total number of users: {total_users}")
        print(f"Total number of tasks: {total_tasks}")
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")

# Function to display the admin menu and handle choices
def admin_menu(username):
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

# Function to display the user menu and handle choices
def user_menu(username):
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

# Main function to run the application
def main():
    users_info = load_users("user.txt")
    username = authenticate_user(users_info)
    if username == 'admin':
        admin_menu(username)
    else:
        user_menu(username)

if __name__ == "__main__":
    main()
