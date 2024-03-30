from django.forms import ModelForm, CharField, TextInput
from .models import QuoteRegField, AuthorReg


class QuoteForm(ModelForm):
    description = CharField(min_length=20, max_length=2000, required=True, widget=TextInput())
    author = CharField(max_length=60, min_length=10, required=True, widget=TextInput())

    class Meta:
        model = QuoteRegField
        fields = ['description', 'author']

class AuthorForm(ModelForm):
    fullname = CharField(max_length=60, min_length=10, required=True, widget=TextInput())
    born_date = CharField(max_length=60, min_length=10, required=True, widget=TextInput())
    born_location = CharField(max_length=100, min_length=10, required=True, widget=TextInput())
    description = CharField(max_length=5000, min_length=50, required=True, widget=TextInput())

    class Meta:
        model = AuthorReg
        fields = ['fullname', 'born_date', 'born_location', 'description']