from products.models import RecipeComment, Recipe
from django import forms


class RecipeCreateForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = (
            'title',
            'small_description',
            'description',
            'image',
            'cover_image',
            'category',
            'tags'
        )
        widgets = {
            'title' : forms.TextInput(attrs= {
                'class' : 'form-control',
                'placeholder' : 'Title'
            }),
            'small_description' : forms.TextInput(attrs= {
                'class' : 'form-control',
                'placeholder' : 'Small Description'
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Description',
                'rows' : 7,
                'cols' : 30
            }),
            'image' : forms.FileInput,
            'cover_image' : forms.FileInput,
            'category' : forms.Select(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'tags' : forms.SelectMultiple(
                attrs={
                    'class' : 'form-control'
                }
            ),
        }


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
  

class SubCommentForm(forms.ModelForm):

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