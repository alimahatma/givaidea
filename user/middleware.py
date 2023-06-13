from django.contrib.auth.middleware import UserPassesTestMiddleware
from django.urls import reverse

class CustomUserPassesTestMiddleware(UserPassesTestMiddleware):
    def test_func(self, user):
        path = self.request.path_info
        if path == reverse('user_profile'):
            # Tes untuk akses halaman profile
            return True
        elif path == reverse('admin_dashboard'):
            # Tes untuk akses halaman admin_dashboard
            return user.is_admin()
        elif path == reverse('superadmin_dashboard'):
            # Tes untuk akses halaman superadmin_dashboard
            return user.is_superadmin()
        elif path == reverse('home'):
            # Tes untuk akses halaman home
            return True
        return False
