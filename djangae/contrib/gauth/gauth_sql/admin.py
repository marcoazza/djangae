from django.contrib import admin

# DJANGAE
from djangae.contrib.gauth.gauth_sql.models import GaeUser

admin.site.register(GaeUser)
