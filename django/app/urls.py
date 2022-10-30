from django.urls import path
from graphene_django.views import GraphQLView
from . import views
from .schema import schema

urlpatterns = [
    path('endpoint', views.receiver),
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
    ]