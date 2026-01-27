import pytest
from login_form import LoginForm


# classes in this sense operate as test suites
# add a description just by using a comment
class TestEmailValidation:

    # each test case is going to have a fresh form
    @pytest.fixture
    def form(self):
        return LoginForm()

    #positive test case
    def test_valid_email(self, form):
           assert LoginForm.validate_email(form, "user@example.com") == True 
           
    #negative test case
    def test_invalid_email(self, form):
           assert LoginForm.validate_email(form, "userexample.com") == False