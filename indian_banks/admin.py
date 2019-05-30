# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from indian_banks import models 


@admin.register(models.Banks)
class BanksAdmin(admin.ModelAdmin):

    list_display = ('id','name')
    search_fields = ('name',)

@admin.register(models.Branches)
class BranchesAdmin(admin.ModelAdmin):

    list_display = ('ifsc','bank','branch','city')
    list_filter = ('bank',)
    search_fields = ('ifsc','city','branch')