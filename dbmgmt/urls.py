from django.urls import path
from .views import backup_db, restore_db

app_name = 'dbmgmt'

urlpatterns = [
    path('backup', backup_db, name='backup_db'),
    path('restore', restore_db, name='restore_db')
]