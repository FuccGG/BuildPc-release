from django import forms
from .models import *


class CaseForm(forms.ModelForm):

    class Meta:
        model = PlayerAction
        fields = ('video_card', 'cpu', 'ram', 'hdd', 'ssd', 'mother_board', 'cooling', 'power_supply',
                  'budget',  'case_level', 'user_id')
        widgets = {'user_id': forms.HiddenInput(), 'budget': forms.HiddenInput(), 'case_level': forms.HiddenInput()}

    def save(self, commit=True):
        player_action = super(CaseForm, self).save(commit=False)
        if commit:
            player_action.save()
        return player_action

