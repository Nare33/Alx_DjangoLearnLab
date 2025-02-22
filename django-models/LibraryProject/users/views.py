from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def role_check(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.userprofile.role != role:
                return HttpResponseForbidden("Access denied.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

@login_required
@role_check('Admin')
def admin_view(request):
    return render(request, 'admin_view.html')

@login_required
@role_check('Librarian')
def librarian_view(request):
    return render(request, 'librarian_view.html')

@login_required
@role_check('Member')
def member_view(request):
    return render(request, 'member_view.html')

