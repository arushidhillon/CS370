from django import forms

class SkillForm(forms.Form):
    skill_input = forms.CharField(label="Skill", max_length=100)