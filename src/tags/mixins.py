from .models import Tag


class TagMixin(object):
    def get_context_data(self, **kwargs):
       context = super(TagMixin, self).get_context_data(**kwargs)

       context.update({
          'tags': Tag.objects.filter(owner=self.request.user),
       })

       return context


    def check_user_or_403(self, user):
        """ Issue a 403 if the current user is no the same as the `user` param. """
        if self.request.user != user:
            raise PermissionDenied


