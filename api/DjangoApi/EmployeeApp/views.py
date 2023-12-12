from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404


from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer


# Deparments APIS.
@require_http_methods(['GET'])
@csrf_exempt
def getDepartments(request):
  departments = Departments.objects.all()
  departments_serializer = DepartmentSerializer(departments, many=True)
  return JsonResponse(departments_serializer.data, safe=False)


@require_http_methods(['POST'])
@csrf_exempt
def addDepartment(request):
  department_data = JSONParser().parse(request)
  departments_serializer = DepartmentSerializer(data=department_data)
  if departments_serializer.is_valid():
    departments_serializer.save()
    return JsonResponse('Added Successfully', safe=False)


@require_http_methods(['PUT'])
@csrf_exempt
def editDepartment(request, department_id):
  
  department = get_object_or_404(Departments, DepartmentId = department_id)
  
  try:
    department_data = JSONParser().parse(request)
  except:
    return JsonResponse({'error': 'Error delete department'})
  
  departments_serializer = DepartmentSerializer(department, data=department_data)
  if departments_serializer.is_valid():
    departments_serializer.save()
    return JsonResponse({'message' : 'Update Successfully'})
  return JsonResponse({'error': 'Invalid data'}, status = 400)


@require_http_methods(['DELETE'])
@csrf_exempt
def deleteDepartment(request, department_id):
  
  department = get_object_or_404(Departments, DepartmentId = department_id)
  department.delete()
  return JsonResponse({'message': 'Deleted Successfully'})


#Employees APIS
