from django.shortcuts import render
from django.http import FileResponse
from gtts import gTTS
import os
from uuid import uuid4

def text_to_speech(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text.strip():
            tts = gTTS(text)
            filename = f"{uuid4()}.mp3"
            filepath = os.path.join('media', filename)
            tts.save(filepath)
            return FileResponse(open(filepath, 'rb'), as_attachment=True, filename=filename)
    return render(request, 'tts/index.html')
