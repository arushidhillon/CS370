from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from inbox import views as views_inbox
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('studentlogin', views.studentlogin, name="studentlogin"),
    path('lablogin', views.lablogin, name="lablogin"),
    path('signout', views.signout, name ="signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
    path('studenthomepage/', views.studenthomepage, name='studenthomepage'),
    path('labhomepage/',views.labhomepage, name='labhomepage'),

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

    path('opportunities/', views.opportunities, name='opportunities'),
    path('students/', views.students, name='students'),
    path('settings/', views.settings, name='settings'),
    path('matches/<str:pk>', views.matches, name='matches'),
    path('matchedstudents/<str:pk>', views.matchedstudents, name='matchedstudents'),
    path('labprofile', views.labprofile, name='labprofile'),
    path('studentprofile', views.studentprofile, name='studentprofile'),
    path('inbox/', views_inbox.inbox_view, name='inbox'),
    path('labpictureupdate', views.labpictureupdate, name='labpictureupdate'),
    path('labskillsupdate', views.labskillsupdate, name='labskillsupdate'),
    path('labcourseupdate', views.labcourseupdate, name='labcourseupdate'),
    path('labbioupdate', views.labbioupdate, name='labbioupdate'),
    path('labdocupdate', views.labdocupdate, name='labdocupdate'),
    path('studentpictureupdate', views.studentpictureupdate, name='studentpictureupdate'),
    path('studentskillsupdate', views.studentskillsupdate, name='studentskillsupdate'),
    path('studentcourseupdate', views.studentcourseupdate, name='studentcourseupdate'),
    path('studentbioupdate', views.studentbioupdate, name='studentbioupdate'),
    path('studentdocupdate', views.studentdocupdate, name='studentdocupdate'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('match', views.match, name='match')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # path('skill/', views.skill, name='skill'),
    # path('skillsview/', views.skillsview, name='skillsview'),
    #path('skillsdisplay/', views.skillsdisplay, name='skillsdisplay'),
