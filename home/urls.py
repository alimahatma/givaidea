from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("skill_track/", views.skill_track, name="skill_track"),
    path("affiliate/", views.affiliate, name="affiliate"),
    path("register/", views.register, name="register"),
    path('login/', views.login_view, name='login'),
    # path("heroes/", views.hero_list, name="hero_list"),

]