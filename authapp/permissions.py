from rest_framework import permissions
from django.contrib.auth.models import Group, Permission


class AdministratorsPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        groups = request.user.groups.all()
        administrators_group = Group.objects.get(name='Administrators')
        if administrators_group in groups:
            return True

# class TeachersPermissions(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         user_groups = request.user.groups.all()
#         Teachers_group = Group.objects.get(name='Teachers')
#         add_student = Permission.objects.get(codename="add_student")
#         view_student = Permission.objects.get(codename="view_student")
#         teacher_permissions = [
#             add_student,
#             view_student,
#         ]
#         Teachers_group.permissions.set(teacher_permissions)




# class GroupsPermissions(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         groups = request.user.groups.all()
#
#         per_administrators = Group.objects.get(name='Administrators')
#         per_students = Group.objects.get(name='Students')
#         per_teachers = Group.objects.get(name='Teachers')
#
#         if per_administrators in groups:
#             return True
#         if per_teachers in groups:
#             if request.method in ['PUT', 'GET']:
#                 return True
#         if per_students in groups:
#             if request.method == 'GET':
#                 return True