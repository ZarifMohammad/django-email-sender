from django import forms

class Subscribe(forms.Form):
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Subject = forms.CharField(max_length=200 , widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))
