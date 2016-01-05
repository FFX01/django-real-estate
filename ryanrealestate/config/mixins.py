from django.core.exceptions import ValidationError


class SingleInstanceMixin(object):
    """
    Ensures that only one instance of any given model can be created.
    """
    def clean(self):
        model = self.__class__
        if model.objects.count() > 0 and self.id != model.objects.get().id:
            raise ValidationError("Can only create one %s instance" % model.__name__)
        super(SingleInstanceMixin, self).clean()


class SingleInstanceAdminMixin(object):
    """
    Hides the 'add' button when there is already an instance of the managed model.
    """
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        return super(SingleInstanceAdminMixin, self).has_add_permission(request)