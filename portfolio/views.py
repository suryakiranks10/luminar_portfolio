from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class AboutView(View):

    def get(self,request):

                    response_data= {
                "institution": "Luminartechnolab",
                "service": "software development training"
            }

                    return JsonResponse(response_data)

class CoursesView(View):

        def get(self,request):
                response_data= [
                {
                    "id": 1,
                    "title": "Python Full Stack Development",
                    "duration": "5 Months",
                    "technologies": ["Python", "Django", "React", "MySQL"]
                },
                {
                    "id": 2,
                    "title": "Data Science & AI",
                    "duration": "4 Months",
                    "technologies": ["Python", "Machine Learning", "Generative AI"]
                }
            ]
                return JsonResponse(response_data,safe=False) #safe needs to be added when adding list of dictionary

class TrainersView(View):

        def get(self,request):

                response_data= [    {"id": 1,
        "name": "Faculty Lead",
        "expertise": "Python, Django, Full-Stack",
        "campus": "Kakkanad & Thrissur"
    }]
                return JsonResponse(response_data,safe=False)


class BranchesView(View):

        def get(self,request):

                response_data=[{
        "id": 1,
        "city": "Kakkanad",
        "region": "Ernakulam"
    },
    {
        "id": 2,
        "city": "Thrissur",
        "region": "Thrissur Round"
    }]
                return JsonResponse(response_data,safe=False)
