from django.db import models
from django.utils.translation import ugettext_lazy as _

class Profile(models.Model):
    """
    Dummy profile model used for testing
    """
    user = models.OneToOneField('auth.User', related_name="profile")
    MALE, FEMALE = 'M', 'F'
    choices = (
        (MALE, _('Male')),
        (FEMALE, _('Female')))
    gender = models.CharField(max_length=1, choices=choices,
        verbose_name=_('Gender'))
    age = models.PositiveIntegerField(verbose_name=_('Age'))