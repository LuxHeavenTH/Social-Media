from django.shortcuts import render

# Create your views here.
def index(request):
  """THE HOMEPAGE FOR INSTAGRAM"""
  return render(request,'instagram/index.html')