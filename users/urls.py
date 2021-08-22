from django.urls import path
from django.views.generic import TemplateView

from users import views

urlpatterns = [
    # Posts
    path(route='<str:username>/', view=TemplateView.as_view(template_name='users/detail.html'), name='detail'),

    path('users/login/', views.login_view, name='login'),
    path('users/logout/', views.logout_view, name='logout'),
    path('users/signup/', views.signup, name='signup'),
    path('users/me/profile', views.update_profile, name='update_profile')
]
