from typing import Any

from django.shortcuts import render
import json
import requests

# Create your views here.
def home(request):

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request=requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+"&distance=25&API_KEY=28D23F92-AB8C-44FD-94E5-B0A2EC8E4A86")

        try :
            api=json.loads(api_request.text)
        except Exception as e :
            api="Error...."

        if api[0]['Category']['Name'] == "Good" :
            category_color="good"
            category_description="(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."

        if api[0]['Category']['Name'] == "Moderate" :
            category_color="moderate"
            category_description="(51 - 100) Air quality is acceptable;however, or some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution)"

        if api[0]['Category']['Name'] == "Unhealthy Sensitive Group" :
            category_color=""
            category_description="(100 - 150)Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."

        if api[0]['Category']['Name'] == "Unhealthy" :
            category_color="unhealthy"
            category_description="(151 - 250) Health alert: everyone may experience more serious health effects.)"

        if api[0]['Category']['Name'] == "Very Unhealthy" :
            category_color="very unhealthy"
            category_description="(201 - 300) Health alert: everyone may experience more serious health effects.)"

        if api[0]['Category']['Name'] == "Hazardous" :
            category_color="hazardeous"
            category_description="(301 - 500)Health warnings of emergency conditions.The entire population is more likely to be affected.)"

        return render(request, 'home.html',
                      {'api' : api, 'category_description' : category_description, 'category_color' : category_color})


    else:
        api_request=requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=28D23F92-AB8C-44FD-94E5-B0A2EC8E4A86")

        try :
            api=json.loads(api_request.text)
        except Exception as e :
            api="Error...."

        if api[0]['Category']['Name'] == "Good" :
            category_color="good"
            category_description="(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."

        if api[0]['Category']['Name'] == "Moderate" :
            category_color="moderate"
            category_description="(51 - 100) Air quality is acceptable;however, or some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution)"

        if api[0]['Category']['Name'] == "Unhealthy Sensitive Group" :
            category_color=""
            category_description="(100 - 150)Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."

        if api[0]['Category']['Name'] == "Unhealthy" :
            category_color="unhealthy"
            category_description="(151 - 250) Health alert: everyone may experience more serious health effects.)"

        if api[0]['Category']['Name'] == "Very Unhealthy" :
            category_color="very unhealthy"
            category_description="(201 - 300) Health alert: everyone may experience more serious health effects.)"

        if api[0]['Category']['Name'] == "Hazardous" :
            category_color="hazardeous"
            category_description="(301 - 500)Health warnings of emergency conditions.The entire population is more likely to be affected.)"

        return render(request, 'home.html',
                      {'api' : api, 'category_description' : category_description, 'category_color' : category_color})


def about(request):
    return render(request, 'about.html',{})
