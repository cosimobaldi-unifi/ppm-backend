from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)

from .models import Event
from .forms import EventForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Registration


class EventListView(ListView):

    model = Event

    template_name = "events/event_list.html"

    context_object_name = "events"


class EventDetailView(DetailView):
    model = Event
    template_name = "events/event_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["registrations"] = self.object.registrations.all()

        context["already_registered"] = False

        if self.request.user.is_authenticated:
            context["already_registered"] = self.object.registrations.filter(
                user=self.request.user
            ).exists()

        return context


class EventCreateView(
    LoginRequiredMixin,
    CreateView
):

    model = Event

    form_class = EventForm

    template_name = "events/event_form.html"

    success_url = reverse_lazy("event_list")

    def form_valid(self, form):

        form.instance.organizer = self.request.user

        return super().form_valid(form)

class OrganizerRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and self.request.user.role == "organizer"
        )


class EventUpdateView(
    LoginRequiredMixin,
    OrganizerRequiredMixin,
    UpdateView,
):

    model = Event

    form_class = EventForm

    template_name = "events/event_form.html"

    success_url = reverse_lazy("event_list")

    def test_func(self):

        event = self.get_object()

        return (
            self.request.user.role == "organizer"
            and event.organizer == self.request.user
        )


class EventDeleteView(
    LoginRequiredMixin,
    OrganizerRequiredMixin,
    DeleteView,
):

    model = Event

    template_name = "events/event_confirm_delete.html"

    success_url = reverse_lazy("event_list")

    def test_func(self):

        event = self.get_object()

        return event.organizer == self.request.user

@login_required
def register_event(request, pk):

    if request.user.role != "attendee":
        return redirect("event_list")

    event = get_object_or_404(Event, pk=pk)

    Registration.objects.get_or_create(
        user=request.user,
        event=event,
    )

    return redirect("event_detail", pk=pk)


@login_required
def unregister_event(request, pk):

    event = get_object_or_404(Event, pk=pk)

    Registration.objects.filter(
        user=request.user,
        event=event,
    ).delete()

    return redirect("event_detail", pk=pk)