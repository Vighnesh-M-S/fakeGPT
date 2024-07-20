from django.shortcuts import render, redirect
from django.contrib import messages
from openai import OpenAI
import re

# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
# from .forms import SignUpForm
# from .models import Code

# client = OpenAI()
def home(request):
	lang_list = ['c','c++','python']

	if request.method == "POST":
		code = request.POST['code']
		lang = request.POST['lang']

		# Check to make sure they picked a lang
		if lang == "Select Programming Language":
			messages.success(request, "Hey! You Forgot To Pick A Programming Language...")
			return render(request, 'home.html', {'lang_list':lang_list, 'response':code, 'code':code, 'lang':lang})			
		else:
			# OpenAI Key
			client = OpenAI(api_key='sk-None-GDz9vpyuNwbKdMSXuq41T3BlbkFJogt4DxDA2wQyvRZd0Lk5')
			# Make an OpenAI Request
			try:
                
				response = client.chat.completions.create(
					model = 'gpt-4o-mini',
					messages = [
                        {"role": "system", "content": "You are a helpful assistant that only responds with code."},
                        {"role": "user", "content": f"Fix this {lang} code: {code}"}
                    ]
					
					)
				response = response.choices[0].message.content.strip()

				code_snippet = re.sub(r'```(?:\w+)?\n(.+?)\n```', r'\1', response, flags=re.DOTALL).strip()
				
				# return render(request, 'home.html', {'lang_list':lang_list})
				# # Parse the response
				# message = response.choices[0].message.content
				# # Save To Database
				# record = Code(question=code, code_answer=response, language=lang, user=request.user)
				# record.save()

				return render(request, 'home.html', {'lang_list':lang_list, 'response':code_snippet, 'lang':lang})
							
			except Exception as e:
				return render(request, 'home.html', {'lang_list':lang_list, 'response':e, 'lang':lang})


	return render(request, 'home.html', {'lang_list':lang_list})
