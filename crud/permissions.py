from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.user.is_staff:
            print("Is staff")
            if request.user.has_perm("crud.view_productmodel"): # "<app_name>.<crud_operation_name>_<model_name>"
                return True
            return False
        print("Not staff")
        return False
