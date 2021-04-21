from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, first_name, last_name='', password=None, is_waiter=False, is_cook=False,
                    is_admin=False):
        user = self.model(first_name=first_name, last_name=last_name, password=password, is_waiter=is_waiter,
                          is_cook=is_cook,
                          is_admin=is_admin, username=username)

        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, password, username, first_name, last_name):
        user = self.create_user(username=username,
                                password=password,
                                first_name=first_name,
                                last_name=last_name,
                                is_waiter=False, is_cook=False,
                                is_admin=False
                                )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Username', max_length=50)
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)

    # WAITER = 0
    # COOK = 1
    # ADMIN = 2
    #
    # ROLE = [
    #     (WAITER, 'Официант'),
    #     (COOK, 'Повар'),
    #     (ADMIN, 'Администратор'),
    # ]
    # role = models.PositiveSmallIntegerField(choices=ROLE, default=WAITER)
    is_admin = models.BooleanField('Студент', default=False)
    is_cook = models.BooleanField('Преподаватель', default=False)
    is_waiter = models.BooleanField('Партнер', default=False)
    is_active = models.BooleanField('Активный', default=True)
    is_staff = models.BooleanField('Сотрудник', default=False)
    is_superuser = models.BooleanField('Админ', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Все пользователи'

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_full_name()
