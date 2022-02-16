from django.forms import ModelForm
from users.models import User


class EditForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'avatar', 'birthdate', 'country', 'fb_account')

