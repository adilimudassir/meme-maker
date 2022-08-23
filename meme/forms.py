from django import forms

class MemeForm(forms.ModelForm):
    name = forms.CharField(required=True)
    tags = forms.TextField(required=True)
    image = forms.TextField(required=True)
    topText = forms.TextField(required=False)
    bottomText = forms.TextField(required=False)
    detail = forms.TextField(required=False)
    thumb = forms.TextField(required=False)
    rank = forms.TextField(required=False)

class SubmissionForm(forms.ModelForm):
    topText = forms.TextField(required=False)
    bottomText = forms.TextField(required=False)