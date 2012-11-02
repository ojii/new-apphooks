# -*- coding: utf-8 -*-
from app.models import TeamMember
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def show_member(request, slug):
    obj = get_object_or_404(TeamMember, slug=slug)
    return HttpResponse('Team Member: %s' % obj.name)

def extract_args_kwargs(slug):
    return (filter(bool, slug.split('/'))[-1],), {}

show_member.extract_args_kwargs = extract_args_kwargs
