from django.shortcuts import render, redirect
from .forms import VideoForm
from .models import Video
import openai

openai.api_key = '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'


# you can now use response.choices[0].text to get the generated text

# Create your views here.
def index(request):
    return render(request, 'index.html')



def generate_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['video_title']
            description = form.cleaned_data['video_description']
            word_limit = form.cleaned_data['word_limit']

            # TODO: call to GPT-3 API to generate script, tags, etc.
            response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Generate a 200 word informative youtube script about the topic "+ title+ ": '{}'",
            max_tokens=word_limit
            )['text']

            video = Video(
                user=request.user, 
                title=title,
                description=description,
                generated_script=response,
                tags="test, test2"
            )
            video.save()

            return redirect('user_videos')
    else:
        form = VideoForm()

    return render(request, 'generate_video.html', {'form': form})


def user_videos(request):
    videos = Video.objects.filter(user=request.user)
    return render(request, 'user_videos.html', {'videos': videos})