from django.urls import path

from add.views import SearchList


urlpatterns = [
    path('v1/', SearchList.as_view())
]