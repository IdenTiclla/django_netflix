from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('profile_list')
        return render(request, 'index.html')

@method_decorator(login_required, name='dispatch')
class ProfileList(View):
    def get(self, request):
        profiles = request.user.profiles.all()
        return render(request, 'profileList.html', {'profiles': profiles})
