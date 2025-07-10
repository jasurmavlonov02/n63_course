from rest_framework import permissions
import datetime

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
    
    
    
    
    
    
    
class IsJohnBlocked(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.username != 'john'
        # if request.user.username == 'john':
        #     return False
        # return True
        
        
class CanJohnRead(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.username == 'john':
            if request.method in ['POST','DELETE','PUT','PATCH']:
                return False
            return True
        return True
    
    
    
# Dushanba-Juma

# 9:00 and 18:00 


class WeekDayOnlyAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        today = datetime.datetime.today().weekday() # ( 0 - 4 ) 0 -dushanba
        return today < 3


class WorkDayOnlyAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        hour = datetime.datetime.now().hour
        return 10<hour<16
    
    
    
class CanReadPremiumCourse(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.is_premium:
            return request.user and request.user.is_staff
        
    
    
    
    
    
    
    
    
    
    
    
    
    