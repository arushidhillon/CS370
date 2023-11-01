
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('studentlogin', views.studentlogin, name="studentlogin"),
    path('signout', views.signout, name ="signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
    path('studenthomepage/', views.studenthomepage, name='studenthomepage'),

    path('reset_password', auth_views.PasswordResetView.as_view(
        template_name="password-reset/password_reset.html"
        ), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(
        template_name="password-reset/password_reset_sent.html"
        ), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name="password-reset/ChangePassword.html"
        ), name ="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name="password-reset/password_reset_done.html"
        ), name="password_reset_complete"),

    path('studentedit/', views.studentedit, name='studentedit'),
    path('opportunities/', views.opportunities, name='opportunities'),
    path('settings/', views.settings, name='settings'),
    path('matches/', views.matches, name='matches'),
    path('skill/', views.skill, name='skill'),
    path('skillsview/', views.skillsview, name='skillsview'),
    path('skillsdisplay/', views.skillsdisplay, name='skillsdisplay'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)