
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepg),
    path('homepg', views.homepg),
    #path('', views.admin),
    path('dash', views.dash),
    path('custreg',views.custreg),
    path('login',views.login),
    path('registcust',views.registcust),
    path('staffregist',views.staffregist),
    path('registstaff',views.registstaff),
    path('registcat',views.registcat),
    path('registowner',views.registowner),
    path('ownerregist',views.ownerregist),
    path('managecust',views.managecust),
    path('managestaff',views.managestaff),
    path('manageowner',views.manageowner),
    path('catregist',views.catregist),
    path('managecat',views.managecat),
    path('managesubcat',views.managesubcat),
    path('subcatregist',views.subcatregist),
    path('activate_customer/<int:id>/', views.activate_customer, name='activate_customer'),
    path('deactivate_customer/<int:id>/', views.deactivate_customer, name='deactivate_customer'),
    path('activate_staff/<int:id>/', views.activate_staff, name='activate_staff'),
    path('deactivate_staff/<int:id>/', views.deactivate_staff, name='deactivate_staff'),
    path('editstaff_fetch/<int:id>/', views.editstaff_fetch, name='editstaff_fetch'),
    path('editstaff/<int:id>/', views.editstaff, name='editstaff'),
    path('activate_owner/<int:id>/', views.activate_owner, name='activate_owner'),
    path('deactivate_owner/<int:id>/', views.deactivate_owner, name='deactivate_owner'),
    path('editowner_fetch/<int:id>/', views.editowner_fetch, name='editowner_fetch'),
    path('editowner/<int:id>/', views.editowner, name='editowner'),
    path('editcat_fetch/<int:id>/', views.editcat_fetch, name='editcat_fetch'),
    path('editcat/<int:id>/', views.editcat, name='editcat'),
    path('registsubcat',views.registsubcat),
    path('editsubcat_fetch/<int:id>/', views.editsubcat_fetch, name='editsubcat_fetch'),
    path('editsubcat/<int:id>/', views.editsubcat, name='editsubcat'),
    path('loginverify',views.loginverify),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
