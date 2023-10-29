from django.urls import path
from . import views




urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('studentlogin', views.studentlogin, name="studentlogin"),
    path('signout', views.signout, name ="signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
    path('studenthomepage/', views.studenthomepage, name='studenthomepage'),
    path('studentedit/', views.studentedit, name='studentedit'),
    path('opportunities/', views.opportunities, name='opportunities'),
    path('settings/', views.settings, name='settings'),
    path('matches/', views.matches, name='matches'),
    path('skill/', views.skill, name='skill'),
    path('skillsview/', views.skillsview, name='skillsview'),
    path('skillsdisplay/', views.skillsdisplay, name='skillsdisplay'),

=======
    path('profilepage/', views.hi, name='profilepage'),
    path('skill/', views.get_skill, name='skill')
>>>>>>> 1d91ccb14ba3b661f77659dcf7ff672f718cbb44
]