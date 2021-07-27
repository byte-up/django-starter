from django.db import models
from django.utils.translation import gettext_lazy as _

class Base(models.Model):
    order = models.PositiveIntegerField(_('Sorting'), default=0,
                                        help_text=_('We usualy order a model in a client and an admin part.'))
    is_active = models.BooleanField(_('Public'), default=True,
                                    help_text=_('This entry is visible or unvisible for a client part or admin part.'))
    is_deleted = models.BooleanField(_('Delete status'), default=False)
    created_date = models.DateTimeField(auto_now_add=True, help_text=_('Show when an entry was created.'))
    modified_date = models.DateTimeField(auto_now=True,  help_text=_('Show when an entry was updated'))

    class Meta(object):
        abstract = True