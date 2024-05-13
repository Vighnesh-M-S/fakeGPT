from django.shortcuts import render
from django.contrib import messages


def home(request):
    lang_list = ['c', 'cpp', 'css', 'html',
                 'java', 'javascript', 'php', 'python']

    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']
        if lang == "Select Programming Language":
            messages.success(request, "Hey! You forgot")
            return render(request, 'home.html', {'lang_list': lang_list, 'code': code, 'lang': lang})
        return render(request, 'home.html', {'lang_list': lang_list, 'code': code, 'lang': lang})

    return render(request, 'home.html', {'lang_list': lang_list})
