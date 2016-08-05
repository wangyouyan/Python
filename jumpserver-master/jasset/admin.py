from django.contrib import admin
import models
# Register your models here.

admin.site.register(models.Tenant_info)
# admin.site.register(models.Host_info)
admin.site.register(models.Idrac)
admin.site.register(models.Url_info)
admin.site.register(models.Virtual_platform)
admin.site.register(models.Virtual_host)

admin.site.register(models.Asset)

admin.site.register(models.AssetAlias)
admin.site.register(models.AssetGroup)
admin.site.register(models.AssetRecord)
admin.site.register(models.IDC)
admin.site.register(models.User)
admin.site.register(models.UserGroup)