import pytest
from vulnerable import get_user_by_id, calculate_average, read_file

def test_calculate_average():
    """Test average calculation"""
    assert calculate_average([1, 2, 3]) == 2
    # This will fail!
    assert calculate_average([]) == 0

def test_get_user_by_id():
    """Test user lookup - should handle SQL injection"""
    result = get_user_by_id("1")
    # This is vulnerable!
    pass

def test_read_file_missing():
    """Test file reading with missing file"""
    # This will crash!
    read_file("/tmp/nonexistent_file_12345.txt")
