from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'MAIN/home.html')

def request(request):
  return render(request, 'MAIN/request.html')