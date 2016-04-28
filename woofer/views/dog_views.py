""" This module holds the views pertaining to Dogs."""
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from ..forms import DogForm
from ..models import Dog

def dog_view(request, dogid):
    """ This is the view for the dog details. """
    dog = Dog.objects.get(id=dogid)
    return render(request, 'woofer/dog_profile.html', {'dog' : dog})

@login_required
def add_dog(request):
    """ Displays form for adding a dog """
    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            new_dog = form.save(commit=False)
            # assign the new dog to the current user
            new_dog.owner = request.user
            new_dog.save()
            return HttpResponseRedirect(reverse('view-dog', args=[new_dog.id]))
    else:
        form = DogForm()

    return render(request, 'woofer/show_form.html', {
        'form' : form,
        'form_action' : reverse('add-dog'),
        'title' : "Add Dog"
    })

def edit_dog(request, dogid):
    """ Display and handel a form for editing dogs """
    dog = Dog.objects.get(id=dogid)
    # Check that the user can edit this dog
    if not request.user.is_authenticated() or dog.owner.id != request.user.id:
        return HttpResponseRedirect(reverse('view-dog', args=[dogid]))

    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            # for some reason django is not putting the object id in the form
            # so if we don't manually update the id it will insert a new object
            new_dog = form.save(commit=False)
            new_dog.id = dogid
            new_dog.owner = request.user
            new_dog.save()
            return HttpResponseRedirect(reverse('view-dog', args=[dogid]))
    else:
        form = DogForm(instance=dog)

    return render(request, 'woofer/show_form.html', {
        'form' : form,
        'message' : None,
        'form_action' : reverse('edit-dog', args=[dogid]),
        'title' : "Edit Dog"
    })

def delete_dog(request, dogid):
    """ Delete dog from database """
    dog = Dog.objects.get(id=dogid)
    if not request.user.is_authenticated() or dog.owner.id != request.user.id:
        return HttpResponseRedirect(reverse('view-dog', args=[dogid]))

    dog.delete()
    return HttpResponseRedirect(reverse('view-profile'))
