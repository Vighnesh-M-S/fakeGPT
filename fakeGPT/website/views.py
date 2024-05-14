from django.shortcuts import render
from django.contrib import messages
import openai


def home(request):
    lang_list = ['c', 'cpp', 'css', 'html',
                 'java', 'javascript', 'php', 'python']

    if request.method == "POST":
        code = request.POST['code']
        if (request.POST['lang']) == "Select Programming Language":
            messages.success(request, "Hey! You forgot")
            return render(request, 'home.html', {'lang_list': lang_list, 'code': code, 'lang': request.POST['lang']})
        else:

            openai.api_key = ""
            openai.Model.list()

            try:
                response = openai.Completion.create(
                    engine='text-davinci-003',
                    prompt="Respond only with code. Fix this " +
                    {lang} + " code: " + {code},

                    temperature=0,
                    max_tokens=1000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                )
                return render(request, 'home.html', {'lang_list': lang_list, 'response': response, 'lang': request.POST['lang']})

            except Exception as e:
                return render(request, 'home.html', {'lang_list': lang_list, 'code': e, 'lang': request.POST['lang']})

    return render(request, 'home.html', {'lang_list': lang_list})
