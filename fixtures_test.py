# test_fixtures.py
import pytest

@pytest.fixture
def sample_list():
    """Fixture that provides a sample list"""
    return [1, 2, 3, 4, 5]

@pytest.fixture
def sample_dict():
    """Fixture that provides a sample dictionary"""
    return {"name": "Alice", "age": 30}

def test_list_length(sample_list):
    assert len(sample_list) == 5

def test_list_contains(sample_list):
    assert 3 in sample_list

def test_dict_keys(sample_dict):
    assert "name" in sample_dict
    assert sample_dict["age"] == 30

