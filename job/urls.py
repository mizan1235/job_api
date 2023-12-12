from django.contrib import admin
from django.urls import path
from job import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('create_user',views.create_user,name='create_user'),
    path('create_employee',views.create_employee,name='create_employee'),
    path('login_user',views.login_user,name='login_user'),
    path('login_employee',views.login_employee,name='login_employee'),
    path('create_job',views.create_job,name='create_job'),
    path('get_job',views.get_job,name='get_job'),
    path('get_emp_job',views.get_emp_job,name='get_emp_job'),
    path('get_job_comp',views.get_job_comp,name=' get_job_comp'),
    path('get_job_location',views.get_job_location,name='get_job_location'),
    path('update_job',views.update_job,name='update_job'),
    path('get_user',views.get_user,name='get_user'),
    path('update_user',views.update_user,name='update_user'),
    path('update_user_pass',views.update_user_pass,name='update_user_pass')
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)