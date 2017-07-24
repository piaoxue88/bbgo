# -*- coding: utf-8 -*-

from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Board, Reply


class BoardEditForm(forms.ModelForm):
    """Form for board"""

    class Meta:
        """Meta for ModelForm"""

        CATEGORY = (
        )
        model = Board
        exclude = (
            'table', 'user', 'created_at', 'modified_at', 'ip',
            'view_count', 'like_count', 'dislike_count', 'reply_count',
            'like_users', 'dislike_users'
        )
        widgets = {
            'subject': forms.TextInput(
                attrs={'placeholder': u'제목을 입력해 주세요.'}
            ),
            'reference': forms.TextInput(
                attrs={'placeholder': u'출처가 있으면 입력해 주세요.'}
            ),
            'category': forms.Select(choices=CATEGORY),
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        """Init"""
        self.user = kwargs.pop('user', None)
        super(BoardEditForm, self).__init__(*args, **kwargs)


class ReplyEditForm(forms.ModelForm):
    """Form for reply"""

    class Meta:
        """MEta for ModelForm"""

        model = Reply
        exclude = (
            'reply_id', 'reply_to', 'status', 'user',
            'created_at', 'modified_at', 'ip',
            'like_count', 'dislike_count', 'like_users', 'dislike_users'
        )

    def __init__(self, *args, **kwargs):
        """Init"""
        self.user = kwargs.pop('user', None)
        super(ReplyEditForm, self).__init__(*args, **kwargs)
