from .models import Comment
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets ={
            'body' : SummernoteWidget(),
        }
# Contacts form
def should_be_empty(value):
    if value:
        raise forms.ValidationError('Feild is not empty')

class ContactForm(forms.Form):
    name = forms.CharField(required = True)
    email =  forms.EmailField(required = True)
    message = forms.CharField(required = True, widget= forms.Textarea(attrs={'rows': 4}))
    forcefield = forms.CharField(
        required=False, widget=forms.HiddenInput, label="Leave empty", validators=[should_be_empty]
    )
