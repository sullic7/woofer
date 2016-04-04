from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.template import RequestContext
from django.utils.translation import ugettext as _
from ..forms import DogForm
from ..models import Dog

def dog_view(request, dogid):
    """ This is the view for the dog details. """
    dog = Dog.objects.get(id = dogid)
    return render(request, 'woofer/dog_profile.html', { 'dog' : dog })

@login_required
def edit_dog(request, dogid=None, template_name='woofer/edit_dog.html'):
    """ This edits existing dog information, and creates new dogs. """
    if id:
        dog = get_object_or_404(Dog, pk=dogid)
        if dog.owner != request.user:
            return HttpResponseForbidden()
    else:
        dog = Dog(owner=request.user)
        # template_name='woofer/add_dog.html'
        
    if request.method == 'POST':
        form = DogForm(request.POST, instance=dog)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _('Dog correctly saved.'))
            # If the save was successful, redirect to another page
            return HttpResponseRedirect('/dog_view/%d' % (dogid))
 
    else:
        form = DogForm(instance=dog)
    
    return render_to_response(template_name, {
        'form': form,
    }, context_instance=RequestContext(request))