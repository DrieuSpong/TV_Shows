from django.shortcuts import render, redirect
from .models import Show

def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release = request.POST['release_date'],
        description = request.POST['description']
    )
    return redirect('/shows')

def edit(request, show_id):
    the_show = Show.objects.get(id=show_id)
    context = {
        'show': the_show
    }
    return render(request, 'edit.html', context)

def update(request, show_id):
    this_update = Show.objects.get(id=show_id)
    this_update.title = request.POST['title']
    this_update.network = request.POST['network']
    this_update.release = request.POST['release_date']
    this_update.description = request.POST['description']
    this_update.save()

    return redirect('/shows')

def show(request, show_id):
    the_show = Show.objects.get(id=show_id)
    context = {
        'show': the_show
    }
    return render(request, 'show.html', context)

def delete(request, show_id):
    the_show = Show.objects.get(id=show_id)
    the_show.delete()
    return redirect('/shows')



