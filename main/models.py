import logging

from django.db import models

logger = logging.getLogger(__name__)


class Manager(models.Manager):
    def dfilter(self, *args, **kwargs):
        return self.filter(is_deleted=False, **kwargs)


class BaseModel(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, db_index=True)

    objects = Manager()

    def delete(self):
        self.is_deleted = True
        self.save(update_fields=["is_deleted"])

    class Meta:
        abstract = True
