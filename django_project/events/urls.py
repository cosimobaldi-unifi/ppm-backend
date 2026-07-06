from django.urls import path

from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    register_event,
    unregister_event,
)

urlpatterns = [

    path(
        "",
        EventListView.as_view(),
        name="event_list",
    ),

    path(
        "event/<int:pk>/",
        EventDetailView.as_view(),
        name="event_detail",
    ),

    path(
        "event/create/",
        EventCreateView.as_view(),
        name="event_create",
    ),

    path(
        "event/<int:pk>/edit/",
        EventUpdateView.as_view(),
        name="event_update",
    ),

    path(
        "event/<int:pk>/delete/",
        EventDeleteView.as_view(),
        name="event_delete",
    ),

    path(
        "event/<int:pk>/register/",
        register_event,
        name="register_event",
    ),

    path(
        "event/<int:pk>/unregister/",
        unregister_event,
        name="unregister_event",
    ),
]