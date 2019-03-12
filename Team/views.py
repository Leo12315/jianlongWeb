from django.shortcuts import render

# Create your views here.

def show_team(request):
    return render(request,'team/team.html')