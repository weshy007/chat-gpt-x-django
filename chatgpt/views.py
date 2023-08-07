import openai
from django.shortcuts import render

from core import settings

openai.api_key = settings.API_KEY


# Create your views here.
def quiz(request):
    if request.method == 'GET':
        # Render the quiz template
        return render(request, 'quiz.html')
    elif request.method == 'POST':
        user_response = request.POST.get('user_response')

        # Call the ChatGPT model
        response = openai.Completion.create(
            engine='gpt-3.5-turbo',
            prompt=user_response,
            max_tokens=50,
            temperature=0.7,
            n=1,
            stop=None,
        )

        answer = response.choices[0].text.strip()

        # Process the user's quiz response and return the appropriate response
        # Return the answer to the user or redirect to the next question
        return render(request, 'quiz_result.html', {'answer': answer})