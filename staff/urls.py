from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('become-staff/', views.become_staff,name="become_staff"),
    path('staff-admin/', views.staff_admin,name="staff_admin"),
    path('logout/', views.logoutUser, name="logout" ),
    path('login/', views.loginUser, name='login'),
    path('add-product/', views.add_product,name="add_product"),
    path('edit-staff/', views.edit_staff, name='edit_staff'),
    path('', views.staffs, name='staffs'),
    path('<int:staff_id>/', views.staff, name='staff'),
    path('edit-product/<str:pk>/', views.edit_product,name="edit_product"),
    path('delete-product/<str:pk>/', views.delete_product, name="delete_product"),




]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)