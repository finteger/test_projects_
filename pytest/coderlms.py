# ==============================================================================
# ALL COLLECTED CODE - COMPLETED CHALLENGES ONLY
# Generated: 2026-01-21 16:38:08
# Total Completed Challenges: 7
# Note: Only challenges that passed all tests are included
# ==============================================================================


# ==============================================================================
# Challenge 1: First Pytest Test ✅ COMPLETED
# Difficulty: Beginner
# Language: Pytest
# Learning Path: Pytest Fundamentals
# Status: All tests passed
# ==============================================================================

def add(a, b):
   return a + b

def test_add():
   assert add(2,3) == 5
 


# ==============================================================================
# Challenge 2: Multiple Assertions ✅ COMPLETED
# Difficulty: Beginner
# Language: Pytest
# Learning Path: Pytest Fundamentals
# Status: All tests passed
# ==============================================================================

def multiply(a, b):
   return a * b

def test_multiply():
   # TODO: Test multiply(2, 3) == 6
   # TODO: Test multiply(5, 0) == 0
   # TODO: Test multiply(-1, 5) == -5
   assert multiply(2,3) == 6
   assert multiply(5,0) == 0
   assert multiply(-1, 5) == -5


# ==============================================================================
# Challenge 3: Testing Exceptions ✅ COMPLETED
# Difficulty: Beginner
# Language: Pytest
# Learning Path: Pytest Fundamentals
# Status: All tests passed
# ==============================================================================

import pytest

def divide(a, b):
   # TODO: Implement division, raise ValueError if b is 0
   if b == 0:
      raise ValueError("Not divisible by 0")
   return a / b

def test_divide_by_zero():
   with pytest.raises(ValueError):
      divide(10,0)


# ==============================================================================
# Challenge 4: Parametrized Tests ✅ COMPLETED
# Difficulty: Beginner
# Language: Pytest
# Learning Path: Pytest Fundamentals
# Status: All tests passed
# ==============================================================================

import pytest

def is_even(n):
   if (n % 2 == 0);
      return True
   else:
      return False

# TODO: Add @pytest.mark.parametrize decorator
# Test with: (2, True), (3, False), (0, True), (-4, True)
@pytest.mark.parametrize("input_value, expected_result", [(2,True), (3,False), (0,True),(-4,True)])
def test_is_even(input_value, expected_result):
   assert is_even(input_value);


# ==============================================================================
# Challenge 5: Basic Fixtures ✅ COMPLETED
# Difficulty: Beginner
# Language: Pytest
# Learning Path: Pytest Fundamentals
# Status: All tests passed
# ==============================================================================

import pytest

# TODO: Create a fixture named 'sample_list' that returns [1, 2, 3, 4, 5]

def test_list_length(sample_list):
    assert len(sample_list) == 5

def test_list_sum(sample_list):
   assert sum(sample_list) == 15


# ==============================================================================
# Challenge 6: Testing Calculator Module ✅ COMPLETED
# Difficulty: Beginner
# Language: Pytest
# Learning Path: Pytest Fundamentals
# Status: All tests passed
# Type: Multi-File Project
# ==============================================================================

# --- File: calculator.py ---
def add(a, b):
   a + b

def subtract(a, b):
   a - b

def multiply(a, b):
   a * b

# --- File: test_calculator.py ---
import pytest
from calculator import add, subtract, multiply

def test_add():
    # TODO: Test addition (5 + 3 should equal 8)
    assert add(5, 3) == 8

def test_subtract():
    # TODO: Test subtraction (10 - 4 should equal 6)
    assert subtract(10, 4) == 6

def test_multiply():
    # TODO: Test multiplication (3 * 7 should equal 21)
    assert multiply(3, 7) == 21



# ==============================================================================
# Challenge 7: Testing with Approximate Values ✅ COMPLETED
# Difficulty: Beginner
# Language: Pytest
# Learning Path: Pytest Fundamentals
# Status: All tests passed
# ==============================================================================

import pytest

def calculate_average(numbers):
   return sum(numbers) / len(numbers)

def test_average():
   # TODO: Test that average of [1, 2, 3] is approximately 2.0
   # TODO: Test that average of [1.5, 2.5, 3.0] is approximately 2.333
   # Use pytest.approx for floating point comparison
   assert calculate_average([1,2,3]) == 2
