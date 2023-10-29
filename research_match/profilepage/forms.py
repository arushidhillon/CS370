from django import forms
from .models import Skill

<<<<<<< HEAD
class SkillForm(forms.ModelForm):
    skill = forms.TextInput()
    class Meta:
    # your_skill = forms.CharField(label="Skill_input", max_length=100)
        model = Skill
        fields = ['skill']
=======
# class SkillForm(forms.Form):
#     skill_input = forms.CharField(max_length=100)
                                  
class SkillForm(forms.Form):
    Skill_input = forms.CharField(label="Your skill", max_length=100)
>>>>>>> 1d91ccb14ba3b661f77659dcf7ff672f718cbb44
