import uuid

from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from features.core.utils import NullEmailField


# Create your models here.
class AbsSlugField(models.Model):
    slug = models.UUIDField(verbose_name=_('Slug'), default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class AbsTimestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Date'), editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated Date'), editable=False)

    class Meta:
        abstract = True


class User(AbstractUser, AbsSlugField, AbsTimestamp):
    email = NullEmailField(null=True, blank=True, unique=True)
    ci = models.IntegerField(validators=[RegexValidator(regex='\?[\d+]{11,}'), ], null=True)
    REQUIRED_FIELDS = ['email']

    EMAIL_FIELD = None

    class Meta:
        db_table = 'tbl_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created']

class Group(Group):

    class Meta:
        db_table = 'tbl_group'
        proxy = True
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
        permissions = (
            ("list_group", "Can list groups"),
        )