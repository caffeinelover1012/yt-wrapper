from django import forms

class VideoForm(forms.Form):
    video_title = forms.CharField(max_length=100)
    video_description = forms.CharField(widget=forms.Textarea)
    word_limit = forms.IntegerField()
