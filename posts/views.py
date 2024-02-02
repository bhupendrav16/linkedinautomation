import pandas as pd

from django.shortcuts import render
from posts.models import File, Posts
# Create your views here.

def create_db(file_path):
    df = pd.read_csv(file_path)
    list_csv = [list(row) for row in df.values]
    for l in list_csv:
        Posts.objects.create(
            name=l[0],
            example= l[1],
            description=l[2]
        )
        
        
def home(request):
    return render(request, 'home.html')
    
def show(request):
    if request.method == "POST":
        file =request.FILES['file']
        obj = File.objects.create(file= file)
        create_db(obj.file)
        obj1 = Posts.objects.all()
        return render( request, 'show.html',{"obj":obj1} )
    obj1 = Posts.objects.all()
    return render( request, 'show.html',{"obj":obj1} )
 