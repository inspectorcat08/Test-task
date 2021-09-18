from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import ShortLink
from .forms import ShortForm


def home_view(request):
    template = 'shortlinks/home.html'

    context = {}

    context['form'] = ShortForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':

        used_form = ShortForm(request.POST)

        if used_form.is_valid():
            shortened_object = used_form.save()

            new_url = request.build_absolute_uri('/') + shortened_object.shorter_url

            longer_url = shortened_object.longer_url

            context['new_url'] = new_url
            context['longer_url'] = longer_url

            return render(request, template, context)

        context['errors'] = used_form.errors

        return render(request, template, context)


def redirect_url_view(request, shortened_part):

    try:
        shortener = ShortLink.objects.get(shorter_url=shortened_part)

        shortener.count_url += 1

        shortener.save()

        return HttpResponseRedirect(shortener.longer_url)

    except:
        raise Http404('Sorry, page not found')

