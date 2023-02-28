from datetime import datetime, timedelta
from portafolio.models import IPUsers
from blog.models import IPUsuarios

def delete_old_records():
    one_month_ago = datetime.now() - timedelta(days=30)
    inactive_users = IPUsers.objects.filter(last_time__lt=one_month_ago)
    inactive_users.delete()

def delete_old_records_blog():
    one_month_ago = datetime.now() - timedelta(days=30)
    inactive_users = IPUsuarios.objects.filter(last_time__lt=one_month_ago)
    inactive_users.delete()