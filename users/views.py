from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LogoutView
from .forms import CustomUserCreationForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        user = form.instance
        login(self.request, user)

        return response
    
class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        # Log the user out manually if necessary
        if request.method in ['GET', 'POST']:
            logout(request)
            return HttpResponseRedirect(self.get_next_page())  # Redirect to the next page
        return self.http_method_not_allowed(request, *args, **kwargs)

    def get_next_page(self):
        # Redirect to a specific page after logout
        return reverse_lazy('login')  # Replace 'login' with your desired URL name