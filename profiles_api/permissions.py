from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""

        # safe methods do not change/manipulate obj.
        if request.method in permissions.SAFE_METHODS:
            return True

        # user is only allowed to edit their own profile.
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow a user to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to update their own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
