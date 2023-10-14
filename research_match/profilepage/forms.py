from django import forms

class SkillForm(forms.Form):
    your_skill = forms.CharField(label="Skill_input", max_length=100)