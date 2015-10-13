from django.db.models import Model
from django.db.models.fields import CharField, TextField, DateTimeField


class Transaction(Model):
    message = TextField(null=True)
    send = CharField(null=True, blank=True, max_length=15, default='')
    response = TextField(null=True)
    status = CharField(null=True, blank=True, max_length=4, default='')
    folio_android = CharField(null=True, max_length=15)
    date_time = DateTimeField(auto_now_add=True)

    list_display = ('send','folio_android')
    #
    # def __unicode__(self):
    #     return "%s" % self.send

    class Meta:
        ordering = ('date_time',)


