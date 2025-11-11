from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailOrRutBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # username será el campo único que puede ser rut o correo
        try:
            user = User.objects.get(email=username)
            print(user)
        except User.DoesNotExist:
            try:
                user = User.objects.get(rut=username)
                print(user)
            except User.DoesNotExist:
                return None
        
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
