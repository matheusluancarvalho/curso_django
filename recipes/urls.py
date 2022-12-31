from django.urls import path

from recipes.views import contato, home, sobre

#  Cliente faz uma HTTP Request e recebe um HTTP Response
#  HTTP Request


urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
]