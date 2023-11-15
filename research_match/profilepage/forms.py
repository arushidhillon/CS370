from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentProfile



# class SkillForm(forms.ModelForm):
#     # skill = forms.TextInput()
#     class Meta:
#     # your_skill = forms.CharField(label="Skill_input", max_length=100)
#         model = StudentProfile
#         fields = ['skill','course','biography']

# class SkillForm(forms.Form):
#     skill_input = forms.CharField(max_length=100)
                                  
# class SkillForm(forms.Form):
#     Skill_input = forms.CharField(label="Your skill", max_length=100)

class UserUpdateForm(forms.ModelForm):
   # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['profile_pic', 'gpa', 'skill', 'course', 'biography','documents']

class Picform(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['profile_pic']
    
class LabUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['profile_pic', 'skill', 'course', 'biography','documents']
        help_texts = {
            'skill': ('Separate skills with a comma.'),
            'course': ('Separate courses with a comma.'),
        }
    