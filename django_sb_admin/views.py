from django.shortcuts import render
from access.models import InitialForm, FormtwoResponses
from django.contrib.admin.views.decorators import staff_member_required

def start(request):
    """Start page with a documentation.
    """
    return render(request, "django_sb_admin/start.html",
                  {"nav_active":"start"})

@staff_member_required
def dashboard(request):
    """Dashboard page.
    """
    applicants = InitialForm.objects.all()
    stage2 = FormtwoResponses.objects.all()
    return render(request, "django_sb_admin/sb_admin_dashboard.html",
                  {"nav_active":"dashboard", "applicants": applicants, "stage2":stage2})


def charts(request):
    """Charts page.
    """
    applicants = InitialForm.objects.filter
    return render(request, "django_sb_admin/sb_admin_charts.html",
                  {"nav_active":"charts"})


def tables(request):
    """Tables page.
    """
    return render(request, "django_sb_admin/sb_admin_tables.html",
                  {"nav_active":"tables"})


def dropdown(request):
    """Dropdown  page.
    """
    return render(request, "django_sb_admin/sb_admin_dropdown.html",
                  {"nav_active":"dropdown"})


def forms(request):
    """Forms page.
    """
    return render(request, "django_sb_admin/sb_admin_forms.html",
                  {"nav_active":"forms"})


def bootstrap_elements(request):
    """Bootstrap elements page.
    """
    return render(request, "django_sb_admin/sb_admin_bootstrap_elements.html",
                  {"nav_active":"bootstrap_elements"})


def bootstrap_grid(request):
    """Bootstrap grid page.
    """
    return render(request, "django_sb_admin/sb_admin_bootstrap_grid.html",
                  {"nav_active":"bootstrap_grid"})

# def rtl_dashboard(request):
#     """RTL Dashboard page.
#     """
#     return render(request, "django_sb_admin/sb_admin_rtl_dashboard.html",
#                   {"nav_active":"rtl_dashboard"})

def blank(request):
    """Blank page.
    """
    return render(request, "django_sb_admin/sb_admin_blank.html",
                  {"nav_active":"blank"})
