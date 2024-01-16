from products.models import RecipeComment
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = RecipeComment
        fields = (
            'message',
        )
        widgets = {
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Message',
                'rows' : 7,
                'cols' : 30
            })
        }
  