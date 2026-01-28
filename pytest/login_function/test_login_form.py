import pytest
from login_form import LoginForm


# classes in this sense operate as test suites
# add a description just by using a comment
class TestEmailValidation:

    # each test case is going to have a fresh form
    @pytest.fixture
    def form(self):
        return LoginForm()
    
    
    @pytest.mark.parametrize(
        "email",
        [
            "user@example.com",
            "2342Sharo@example.com",
            "user@crypto.co",
            "user@domain.ai",
            "user@test.org"
        ]
    ) 
    

    #positive test case
    def test_valid_email(self, form, email):
           assert LoginForm.validate_email(form, email) is True 
           
           
    @pytest.mark.parametrize(
        "email",
        [
            "user@.com",
            "$$$$.com",
            "user@com",
            "user@domain.c",
            "user@domain..@@@.com"
        ]
    )       
           
    #negative test case
    def test_invalid_email(self, form, email):
           assert LoginForm.validate_email(form, email) is False