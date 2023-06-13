from django.shortcuts import redirect
from django.urls import reverse

class RoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return self.process_request(request, response)

    def process_request(self, request, response):
        if request.path == reverse('admin:index') and request.user.role != 'superadmin':
            return redirect('home')
        return response