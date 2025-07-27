from django import forms
from .models import Contact

class Myform(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    email = forms.EmailField()
    branch = forms.CharField(max_length=100)
    
    
    
# ----------------------------------- Model Form ------------------------------
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
    