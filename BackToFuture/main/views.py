from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def artists(request):
    return render(request, 'main/artists.html')

def part2(request):
    return render(request, 'main/part2.html')

def part3(request):
    return render(request, 'main/part3.html')