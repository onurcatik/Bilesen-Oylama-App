"""voting_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
    path('admin/', admin.site.urls),
    # path('custom-admin/', user_views.custom_admin_view, name='custom_admin'),  # Custom admin URL
    path('register/', user_views.register, name='register'),
    path('login/', user_views.user_login, name='login'),
    path('logout/', user_views.user_logout, name='logout'),
    path('', user_views.home, name='home'),
    path('about/', user_views.about, name="about"),
    path('profile', user_views.about, name="profile"),
    path('custom-admin/', user_views.custom_admin, name='custom_admin'),
    path('admin-edit-user/<int:user_id>/', user_views.admin_edit_user, name='admin_edit_user'),
    path('admin-delete-user/<int:user_id>/', user_views.admin_delete_user, name='admin_delete_user'),
    path('admin-add-user/', user_views.admin_add_user, name='admin_add_user'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)