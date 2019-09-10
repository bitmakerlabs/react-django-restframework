import os
import logging

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

from rest_framework import viewsets

from .models import Musician, Album
from .serializers import MusicianSerializer

# Buy using ModelViewSet, and just passing the serialzer and model for a given table,
# we are able to import it in our urls.py, and get all the CRUD actions and url routes for free.
class MusicianViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()

# A view that matches any request, and routes it to either the statically built assests, or our
# live-reload local development environment.
class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    run build`).
    """

    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead, or
                run `yarn run build` to test the production version.
                """,
                status=501,
            )