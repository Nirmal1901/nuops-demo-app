"""
Vulnerable code for testing NuOps auto-healing
"""

import sqlite3

# SQL INJECTION VULNERABILITY
def get_user_by_id(user_id):
    """Get user from database - VULNERABLE to SQL injection"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # DANGER: Direct string concatenation - SQL injection!
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    
    return cursor.fetchone()

# DIVISION BY ZERO BUG
def calculate_average(numbers):
    """Calculate average - has division by zero bug"""
    total = sum(numbers)
    # BUG: No check for empty list
    return total / len(numbers)

# UNUSED VARIABLE (code smell)
unused_config = {
    'debug': True,
    'secret': 'key'
}

# POOR ERROR HANDLING
def read_file(filename):
    """Read file - no error handling"""
    with open(filename, 'r') as f:
        return f.read()
