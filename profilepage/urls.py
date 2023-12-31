from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from inbox import views as views_inbox
from django.contrib.auth import views as auth_views
from search import views as views_search



urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('studentlogin', views.studentlogin, name="studentlogin"),
    path('lablogin', views.lablogin, name="lablogin"),
    path('signout', views.signout, name ="signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),

    #These urls use Django's built in Reset Password function. Here we only change the templates used.
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

    path('MatchAlgorithm/', views.MatchAlgorithm, name='MatchAlgorithm'),
    path('settings/', views.settings, name='settings'),
    path('matches/<str:pk>', views.matches, name='matches'),
    path('matchedstudents/<str:pk>', views.matchedstudents, name='matchedstudents'),
    path('labprofile', views.labprofile, name='labprofile'),
    path('studentprofile', views.studentprofile, name='studentprofile'),
    path('inbox/', views_inbox.inbox_view, name='inbox'),
    path('new_message_match/<recipient_id>/', views.new_message_match, name="inbox-newmessage-match"),
    path('labpictureupdate', views.labpictureupdate, name='labpictureupdate'),
    path('labskillsupdate', views.labskillsupdate, name='labskillsupdate'),
    path('labgpaupdate', views.labgpaupdate, name='labgpaupdate'),
    path('labcourseupdate', views.labcourseupdate, name='labcourseupdate'),
    path('labbioupdate', views.labbioupdate, name='labbioupdate'),
    path('labdocupdate', views.labdocupdate, name='labdocupdate'),
    path('studentpictureupdate', views.studentpictureupdate, name='studentpictureupdate'),
    path('studentskillsupdate', views.studentskillsupdate, name='studentskillsupdate'),
    path('studentgpaupdate', views.studentgpaupdate, name='studentgpaupdate'),
    path('studentcourseupdate', views.studentcourseupdate, name='studentcourseupdate'),
    path('studentbioupdate', views.studentbioupdate, name='studentbioupdate'),
    path('studentdocupdate', views.studentdocupdate, name='studentdocupdate'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('match/<str:pk>', views.match, name='match'),
    path('unmatch/<str:pk>', views.unmatch, name='unmatch'),
    path('remove', views.remove, name='remove'),
    path('students/',views_search.students, name='students'),
    path('labnameupdate', views.labnameupdate, name='labnameupdate'),
    path('labgpaupdate', views.labgpaupdate, name='labgpaupdate'),
    path('studentnameupdate', views.studentnameupdate, name='studentnameupdate'),
    path('studentgpaupdate', views.studentgpaupdate, name='studentgpaupdate'),
    # URL for processing the search query and returning the results
    path('search-students/',views_search.search_students, name='search_students'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Ths stores the documents/images in a Media file
