from django.contrib import admin

import models
# Register your models here.
admin.site.register(models.docker_conf)
admin.site.register(models.pull_image_detail)
admin.site.register(models.docker_image_pull_record)
