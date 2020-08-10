from django import forms
from .models import DjangoBoard

class DjangoBoardForm(forms.ModelForm):
    class Meta:
        model = DjangoBoard
        fields = ['subject','content','file']

        widgets = {
            'subject' : forms.TextInput(attrs={'class':'board_form'}),
            'content' : forms.Textarea(attrs={'class':'board_form', 'rows':10}),
            'file' : forms.FileInput(attrs={'class':'board_form', }),
        }
