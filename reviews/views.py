from django.shortcuts import render

def index(request):
    name = "Cody"
    return render(request, 'base.html', {'name': name})
 
def search(request):
    title = request.GET.get('title') or 'Please input a valid search request'
    return render(request, 'search.html', {'title': title})