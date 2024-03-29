"""sattva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from events import views as event_views
from accounts import views as accounts_views
from dashboard import views as dash_views
from results import views as result_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', result_views.point_lists, name='home'),
    path('dash/', dash_views.dashviews, name='dashboard'),
    path('dash/new', event_views.ParticipantCreateView.as_view(), name='newregistration'),
    path('dash/captians/list/all', dash_views.ParticipantListView.as_view(), name='list'),
    path('dash/captians/list/export', dash_views.ParticipantListExportView.as_view(), name='exportlist'),
    path('dash/captians/list/upcoming', dash_views.participant_list, name='caplist'),
    path('dash/participants/list', event_views.participant_list, name='plist'),
    #path('dash/list/', dash_views.person_list, name='list'),
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/update/account', accounts_views.update_profile, name='update_profile'),
    path('profile/update/password', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='change_password'),
    path('profile/update/password/done', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('reset/',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    path('reset/done',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    path('reset/complete',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    #path('', event_views.homeviews, name='home'),
    path('dash/ajax/load-events/', event_views.load_events, name='ajax_load_events'),
    re_path(r'^dash/(?P<pk>\d+)/delete/$', event_views.participant_delete, name='participant_delete'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]
