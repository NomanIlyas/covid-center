#========================================
# Scheduler Jobs
#========================================
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
import scheduler_jobs
import import_countries,import_states
from frontend.management.commands import import_countries, import_states
from frontend.models import CovidRecordUpdateSetting
scheduler = BackgroundScheduler()
scheduler.configure(timezone=utc)
# jobs
query = CovidRecordUpdateSetting.objects.filter(pk=1)

for q in query:
    print(q.days)
    d = q.days
    h = q.hour
    m = q.minutes
    s = q.seconds

scheduler.add_job(scheduler_jobs.handle, 'interval', days=d,hours=h,minutes=m,seconds=s)

scheduler.add_job(import_countries.Command, 'interval', days=d,hours=h,minutes=m,seconds=s)

scheduler.add_job(import_states.Command, 'interval', days=d,hours=h,minutes=m,seconds=s)

scheduler.start()
#========================================