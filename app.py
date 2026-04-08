"""
Sample Python app with intentional bugs for CI/CD testing
"""

def divide_numbers(a, b):
    """Division function with no zero check"""
    return a / b  # BUG: No division by zero check

def get_user_data(user_id):
    """SQL injection vulnerability"""
    query = f"SELECT * FROM users WHERE id = {user_id}"  # BUG: SQL Injection
    return query

def process_data(data):
    """Missing error handling"""
    result = data['key']  # BUG: KeyError if 'key' missing
    return result

# Unused variable (code smell)
unused_var = 100

# Bad practice - global variable
counter = 0

def increment_counter():
    global counter
    counter += 1
    return counter

if __name__ == "__main__":
    print(divide_numbers(10, 0))  # This will crash
