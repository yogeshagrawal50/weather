from typing import Any

from django.shortcuts import render
import json
import requests

# Create your views here.
def home(request):

    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=28D23F92-AB8C-44FD-94E5-B0A2EC8E4A86")

    try:
        api=json.loads(api_request.text)
    except Exception as e :
        api = "Error...."

    return render(request, 'home.html',{'api': api})

def about(request):
    return render(request, 'about.html',{})
