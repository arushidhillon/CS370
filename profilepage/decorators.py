from django.http import Http404, HttpResponse
from django.shortcuts import redirect

# This function allows pages to only be viewed by allowed groups. Only students can see a student page, and only labs can see a labs page. 
# Otherwise, they will only see a pre-made Django 404 Error Page.

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


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)

    return wrapper_func