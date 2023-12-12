from django.urls import path
from EmployeeApp import views

urlpatterns = [
  path('getDepartments/', views.getDepartments, name='get_department'),
  path('addDepartments/', views.addDepartment, name='add_department'),
  path('editDepartments/<int:department_id>', views.editDepartment, name='edit_department'),
  path('deleteDepartments/<int:department_id>', views.deleteDepartment, name='delete_department')
]
