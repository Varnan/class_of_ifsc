from rest_framework import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings

from indian_banks import models


class BranchSerializer(serializers.ModelSerializer):
    bank_name = serializers.SerializerMethodField()

    def get_bank_name(self, obj):
        return obj.bank.name

    class Meta:
        model = models.Branches
        fields = ('ifsc','branch','bank_name','city','district','state','address')