from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


# def video_view(request):
#     if request.method == 'POST':
#         form = VideoForm(request.POST)
#         if form.is_valid():
#             video = form.save(commit=False)
#             video.user = request.user
#             video.save()

#             # Here is where you would call the GPT-3 API
#             # You'll want to replace this with your actual API key and implementation
#             openai.api_key = 'your-api-key'
#             response = openai.Completion.create(
#               engine="text-davinci-002",
#               prompt="Translate the following English text to French: '{}'",
#               max_tokens=60
#             )

#             return render(request, 'response.html', {'response': response.choices[0].text.strip()})
#     else:
#         form = VideoForm()
#     return render(request, 'form.html', {'form': form})
