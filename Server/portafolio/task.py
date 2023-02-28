from datetime import datetime, timedelta
from portafolio.models import IPUsers

def delete_old_records():
    one_month_ago = datetime.now() - timedelta(days=1)
    inactive_users = IPUsers.objects.filter(last_time__lt=one_month_ago)
    inactive_users.delete()