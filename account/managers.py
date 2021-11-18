from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password, **info):
        if not username:
            raise ValueError("The username must be set")

        user = self.model(username=username, password=password, **info)
        user.set_password(password)
        user.save()

        return user
