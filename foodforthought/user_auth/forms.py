from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    """This class represents a the user regisatration form.

    Attributes added to default form:
    - :param email: The email address of the user.
    - :type: email.
    - :param first_name: First name of the registering user.
    - :type: Character text field max length of 50.
    - :param last_name: Last name of the registering user.
    - :type: Character text field max length of 50.
    """
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        """This class represents a user instance inside the register user form
        and specifies the fields included.
        """
        model = User
        fields = ('username', 'first_name',  'email', 'last_name', 'password1', 
                  'password2')