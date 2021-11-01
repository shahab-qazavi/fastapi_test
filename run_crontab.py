from crontab import CronTab
from PrintException import PrintException as prEx

try:
    cron = CronTab(user='root')
    job = cron.new(command='python3 check_price.py')
    job.minute.every(10)
    cron.write()
except:
    print(prEx())

