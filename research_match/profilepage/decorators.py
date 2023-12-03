from django.http import Http404, HttpResponse
from django.shortcuts import redirect

# This function pushes unauthenticated users to the home page to log in.
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)
    
    return wrapper_func

#This function allows only students to view student pages and vice versa for labs.
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else: 
                    raise Http404("Page does not exist. You do not have access to this page.")
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator