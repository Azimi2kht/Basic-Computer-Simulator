from django import forms


class InputAssembler(forms.Form):
    input = forms.CharField(label = '', widget=forms.Textarea(attrs={
                            'id': "input", 'rows': "10", 'cols': "50", 'unselectable': "off", 'spellcheck': "false"}))
