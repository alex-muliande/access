from django.shortcuts import render
from access.models import InitialForm
from application3.models import  FormtwoResponses
from django.contrib.admin.views.decorators import staff_member_required

# def start(request):
#     """Start page with a documentation.
#     """
#     return render(request, "django_sb_admin/start.html",
#                   {"nav_active":"start"})

@staff_member_required
def dashboard(request):
    """Dashboard page.
    """
    applicants = InitialForm.objects.all()
    stageone = interestModel.objects.all()
    stagetwo = scoreModel.objects.all()
    return render(request, "django_sb_admin/sb_admin_dashboard.html",locals())

def applicants(request):
    print('**********************')
    return render(request, "django_sb_admin/applicants.html")


def sample(request):
    return render(request, "sample.html")


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
