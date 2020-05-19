from django import forms

from .models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        widgets ={
            'name': forms.TextInput(attrs={'placeholder':'Character Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'This is the description of your character'}),
            'description': forms.Textarea(attrs={'rows':10,'cols':100,'style':'resize:none;'})

        }
        fields = ('name', 'sex', 'specie', 'description')


