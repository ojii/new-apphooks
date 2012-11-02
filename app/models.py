# -*- coding: utf-8 -*-
from cms.api import create_page
from cms.models import Title, Page
from django.db import models
from django.db.models.signals import post_save, post_delete


class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __unicode__(self):
        return self.name

def sync_page(instance, created, **kwargs):
    if created:
        page = create_page(instance.name, 'tpl.html', 'en', slug=instance.slug,
            parent=Page.objects.get_home(), published=True, in_navigation=True)
        page.view_path = 'app.views.show_member'
        page.save()

def sync_page_delete(instance, **kwargs):
    title = Title.objects.get(slug=instance.slug, page__view_path='app.views.show_member')
    title.page.delete()

post_save.connect(sync_page, sender=TeamMember)
post_delete.connect(sync_page_delete, sender=TeamMember)
