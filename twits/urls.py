"""
Jordyn Kuhn
CIS 218
4-7-2024
"""
from django.urls import path

from .views import (
    TwitListView,
    TwitDetailView,
    TwitCreateView,
    TwitUpdateView,
    TwitDeleteView,
    TwitLikeView,
    AccountView,
) 

urlpatterns=[
    path("<int:pk>/", TwitDetailView.as_view(), name="twit_detail"),
    path("<int:pk>/edit/", TwitUpdateView.as_view(), name="twit_edit"),
    path("<int:pk>/delete/", TwitDeleteView.as_view(), name="twit_delete"),
    path("<int:pk>/like/", TwitLikeView.as_view(), name="twit_like"),
    path("<int:pk>/account/", AccountView.as_view(), name="account_view"),
    path("new/", TwitCreateView.as_view(), name="twit_create"),
    path("", TwitListView.as_view(), name="twit_list"),
]