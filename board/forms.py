#-*- coding: utf-8 -*-
from board.models import Board
from django import forms

class BoardEditForm(forms.ModelForm):
    class Meta:
        model = Board
        exclude = ('table', 'user', 'datetime', 'ip', 'viewcount', 'likecount', 'likeusers',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(BoardEditForm, self).__init__(*args, **kwargs)
