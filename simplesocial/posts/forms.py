from django import forms
from posts.models import Post, Comment


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
