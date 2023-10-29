from django import forms
from .models import Skill

class SkillForm(forms.ModelForm):
    skill = forms.TextInput()
    class Meta:
    # your_skill = forms.CharField(label="Skill_input", max_length=100)
        model = Skill
        fields = ['skill']