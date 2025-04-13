from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'MAIN/home.html')

def submit(request):
  return render(request, 'MAIN/submit.html')

def review(request):
  return render(request, 'MAIN/review.html')