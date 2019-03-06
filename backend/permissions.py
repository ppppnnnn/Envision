#codeing=utf-8
from rest_framework import permissions
from .models        import Administrators,Group

#----------------只读或者对象所有者可进行删改---------------------
class IsOwnerOrReadOnly(permissions.BasePermission):
    #视图级权限控制
    def has_permission(self,request,view):
        return True
    # 检查用户是否为该对象的拥有者
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True                                   #如果请求方法为读取类型，则通过
        return request.user.id == obj.author_id       #请求方法非读取类型，则验证对象所有者


#-------------------------管理员操作----------------------------
class IsAdminUser(permissions.BasePermission):
    def has_permission(self,request,view):
        return True
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return Administrators.objects.get(uid=request.user.uid)


#-------------------------群组管理员----------------------------
class IsGroupAdminUser(permissions.BasePermission):
    def has_permission(self,request,view):
        return True
    
    def has_object_permission(self,request,view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            admin = Group.objects.get(request.data.get('group_id')).group_admin_id
            for i in list(admin):
                if request.user.id == int(i):
                    return True
                    break
                else:
                    continue
            return False


            