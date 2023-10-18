from django import forms

# class SkillForm(forms.Form):
#     skill_input = forms.CharField(max_length=100)
                                  
class SkillForm(forms.Form):
    Skill_input = forms.CharField(label="Your skill", max_length=100)