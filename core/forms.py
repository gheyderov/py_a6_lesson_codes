from typing import Any
from core.models import Contact
from django import forms


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message'
        )
        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Name'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Email'
            }),
            'subject' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Subject'
            }),
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Message',
                'rows' : 7,
                'cols' : 30
            })
        }
    
    # def clean_email(self):
    #     value = self.cleaned_data['email']
    #     if not value.endswith('gmail.com'):
    #         raise forms.ValidationError('Email must be gmail.com')
    #     return value
        
    def clean(self) -> dict[str, Any]:
        value = self.cleaned_data['email']
        if not value.endswith('gmail.com'):
            raise forms.ValidationError('Email must be gmail.com')
        return super().clean()
    
    def clean_name(self):
        value = self.cleaned_data['name']
        return value.upper()