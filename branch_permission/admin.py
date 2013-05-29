from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.contrib.sites.models import get_current_site
from django.core.urlresolvers import reverse


class ModelPermissionAdmin(object):

    def __init__(self, *args, **kwargs):
        super(ModelPermissionAdmin, self).__init__(*args, **kwargs)
        if self.fieldsets:
            self.fieldsets.append(('Branch permissions',
               {
                   'fields': ('owner', 'sites', 'is_published',),
                   'classes': ('collapse',),
               }))

    @property
    def media(self):
        base_media = super(ModelPermissionAdmin, self).media
        base_media.add_css({'all': [reverse('hide_site_selection_css')]})
        return base_media

    def save_model(self, request, obj, form, change):
        #deal with owner
        owner = None
        try:
            owner = getattr(obj, 'owner')
        except ObjectDoesNotExist:
            pass
        if owner is None:
            obj.owner = request.user

        super(ModelPermissionAdmin, self).save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super(ModelPermissionAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['sites'].widget = forms.CheckboxSelectMultiple()
        form.base_fields['sites'].help_text = None
        #always select current site
        if obj is None:
            current_site = get_current_site(request)
            form.base_fields['sites'].initial = [current_site.pk]

        return form

    def get_readonly_fields(self, request, obj=None):
        ro_fields = super(ModelPermissionAdmin, self).get_readonly_fields(request, obj)
        ro_fields += ('owner',)
        return ro_fields