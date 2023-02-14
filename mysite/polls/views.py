from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Request, Output 
from datetime import timedelta, datetime
import openai 
#import requests
import sys

# Create your views here.

def index(request):
    request_list = Request.objects.order_by('request_date')
    context = {
            'request_list':request_list,
    }
    return render(request, 'polls/index.html', context)

def output(request):
    if request.method == 'POST':
        form_data = request.POST
        
        #Save data to DB
        new_row = Request(request_date = datetime.now() , shade = form_data["skin_type"], age = form_data["age"], request_text =form_data["comments"], model_run_time = timedelta(seconds = 3600))
        new_row.save()
        
        #Run OpenAI completion prompt
        openai.api_key = "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"
        new_prompt = "I am a woman with " + new_row.shade + " complexion and combination skin. I am " + new_row.age + " years old. I'd like you to recommend specific products that I should try for a makeup look to or for a " + new_row.request_text + "Please recommend the steps I should put the makeup on, and what specific products and brands I should use. For example, don't just tell me to use a concealer but instead recommend that I use NARS Radiant Creamy Concealer in a specific shade, like Caramel. Please separate each recommendation step with: [NEW_STEP]"
        response_convert = openai.Completion.create(
            engine="text-davinci-003",
            prompt=new_prompt,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        #Format output for HTML
        formatted_output = response_convert['choices'][0]['text'].replace('[NEW_STEP]', '<br>')

        #Write output in DB
        new_row_output = Output(output_text = formatted_output, request = new_row)
        new_row_output.save()

        context = {
            'output_test':formatted_output,
        }
        return render(request, 'polls/output.html', context)

    else:
        return render(request, 'polls/request.html')


def request(request):
    return render(request, 'polls/request.html')

def all(request):
    return HttpResponse("Hello, you're at the home page")

