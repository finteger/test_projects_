import pytest

#this is a decorator
@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_list(sample_list):
    assert 3 in sample_list