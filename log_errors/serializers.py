from rest_framework import serializers
from log_errors.models import Log_Errors
from transactions.models import Transaction


class Log_ErrorsSerialize(serializers.ModelSerializer):
    class Meta:
        model = Log_Errors
        fields = ('error','error_human')