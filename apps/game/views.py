from django.shortcuts import render

# Create your views here.
def example_view (request):
    msg = "Hi!!"
    return render (request, 'example.html', locals())