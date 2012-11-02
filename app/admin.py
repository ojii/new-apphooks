# -*- coding: utf-8 -*-
from app.models import TeamMember
from django.contrib import admin


admin.site.register(TeamMember,
    prepopulated_fields = {
        'slug': ['name']
    }
)
