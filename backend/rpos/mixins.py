from django.views.generic import TemplateView
from rolepermissions.mixins import HasRoleMixin, HasPermissionsMixin


class AdminPermissionMixin(HasRoleMixin, TemplateView):
    allowed_roles = 'is_admin'

    # def has_permission(self):
    #     return self.get_object().is_admin == self.request.user
    #
    # def dispatch(self, request, *args, **kwargs):
    #     if not self.has_permission():
    #         raise Http404()
    #     return super().dispatch(request, *args, **kwargs)
