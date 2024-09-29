from django.urls import path
from .views import (
    login_view,
    logout_view,
    dashboard_view,
    employee_list_view,
    create_employee_view,
    edit_employee_view,
    delete_employee,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('employees/', employee_list_view, name='employee_list'),
    path('employees/create/', create_employee_view, name='create_employee'),
    path('employees/edit/<int:employee_id>/', edit_employee_view, name='edit_employee'),
    path('delete_employee/<int:id>/', delete_employee, name='delete_employee'),
    path('logout/', logout_view, name='logout'),  # Logout route
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
