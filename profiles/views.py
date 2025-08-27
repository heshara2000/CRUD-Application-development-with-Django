from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages



class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    context_object_name = 'profiles'
    paginate_by = 5


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile_form.html'
    success_url = reverse_lazy('profiles:profile-list')

    def form_valid(self, form):
        messages.success(self.request, 'Profile created successfully.')
        return super().form_valid(form)


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile_form.html'
    success_url = reverse_lazy('profiles:profile-list')

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully.')
        return super().form_valid(form)


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profiles/profile_confirm_delete.html'
    success_url = reverse_lazy('profiles:profile-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Profile deleted successfully.')
        return super().delete(request, *args, **kwargs)