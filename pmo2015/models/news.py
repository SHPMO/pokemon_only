from django.db import models
from pmo2015.models.bases import BaseModel
from pmo2015.models.user import PmoAdmin


class News(BaseModel):
    class Meta:
        app_label = 'pmo2015'
        verbose_name_plural = 'news'
    title = models.CharField(max_length=40)
    content = models.TextField()
    user = models.ForeignKey(to=PmoAdmin, default=PmoAdmin.get_default_admin)

    def __str__(self):
        return '%s' % self.title
