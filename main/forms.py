from django import forms
from django.core import validators
from .models import ContactProfile


class ContactForm(forms.ModelForm):
    """Định nghĩa Contact form sẽ được render lên template như thế nào"""
    name = forms.CharField(max_length=100, required=True,
                           widget=forms.TextInput(attrs={
                               'placeholder': 'Full name..',
                           }))
    email = forms.EmailField(max_length=254, required=True, validators=[validators.EmailValidator(message="Invalid Email")],
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'Email..',
                             }))
    message = forms.CharField(max_length=1000, required=True,
                              widget=forms.Textarea(attrs={
                                  'placeholder': 'Message..',
                                  'rows': 6,
                              }))

    class Meta:
        """Metadata của form"""
        model = ContactProfile
        fields = ('name', 'email', 'message',)
