import json
import statistics

def load_users():
    with open('customers.json', 'r') as file:
        return json.load(file)

def calculate_averages(users):
    checking_balances = [details['checking'] for details in users.values()]
    saving_balances = [details['saving'] for details in users.values()]
    avg_checking = statistics.mean(checking_balances)
    avg_saving = statistics.mean(saving_balances)
    return avg_checking, avg_saving

def display_above_average(users, avg_checking, avg_saving):
    print("Customers with checking account balance above average:")
    for username, details in users.items():
        if details['checking'] > avg_checking:
            print(f"Username: {username}, Checking Balance: ${details['checking']}")
    
    print("\nCustomers with saving account balance above average:")
    for username, details in users.items():
        if details['saving'] > avg_saving:
            print(f"Username: {username}, Saving Balance: ${details['saving']}")

users = load_users()
avg_checking, avg_saving = calculate_averages(users)
display_above_average(users, avg_checking, avg_saving)
