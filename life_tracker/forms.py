from django import forms

class ProgressForm(forms.Form):
    # Example fields for tracking progress
    spiritual = forms.IntegerField(label='Spiritual', min_value=0, max_value=10)
    relationships = forms.IntegerField(label='Relationships', min_value=0, max_value=10)
    network = forms.IntegerField(label='Network', min_value=0, max_value=10)
    financial = forms.IntegerField(label='Financial', min_value=0, max_value=10)
    physical = forms.IntegerField(label='Physical', min_value=0, max_value=10)
    nature = forms.IntegerField(label='Nature', min_value=0, max_value=10)
    body = forms.IntegerField(label='Body', min_value=0, max_value=10)
    self = forms.IntegerField(label='Self', min_value=0, max_value=10)