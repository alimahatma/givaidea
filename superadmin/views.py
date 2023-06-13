# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required, user_passes_test
# from .models import CustomerUser

# def is_admin(user):
#     return user.role == CustomerUser.ADMIN or user.role == CustomerUser.SUPERADMIN

# def is_superadmin(user):
#     return user.role == CustomerUser.SUPERADMIN

# @login_required
# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, 'admin.html')

# @login_required
# @user_passes_test(is_superadmin)
# def superadmin_view(request):
#     return render(request, 'superadmin.html')

# @login_required
# def home_view(request):
#     return render(request, 'home.html')
