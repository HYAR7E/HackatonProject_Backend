from django.db import models
from django.utils.translation import ugettext_lazy as _
from master.models import User

import binascii
import os


class Token(models.Model):
    """ Token model """
    key = models.CharField(_("Key"), max_length=40, primary_key=True)

    user = models.OneToOneField(
        User, related_name='auth_token',
        on_delete=models.CASCADE, verbose_name="User"
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
