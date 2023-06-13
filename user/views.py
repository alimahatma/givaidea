# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import CustomUser

# @login_required
# def user_profile(request):
#     user = request.user
#     return render(request, 'profile.html', {'user': user})

# @login_required
# def admin_dashboard(request):
#     if request.user.is_admin:
#         # Logika untuk tampilan admin
#         return render(request, 'admin_dashboard.html')
#     else:
#         # Jika pengguna bukan admin, redirect ke halaman lain
#         return redirect('home')

# @login_required
# def superadmin_dashboard(request):
#     if request.user.is_superadmin:
#         # Logika untuk tampilan superadmin
#         return render(request, 'superadmin_dashboard.html')
#     else:
#         # Jika pengguna bukan superadmin, redirect ke halaman lain
#         return redirect('home')

# @login_required
# def home(request):
#     return render(request, 'home.html')