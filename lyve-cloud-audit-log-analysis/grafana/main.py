# Copyright (c) 2021 Seagate Technology LLC and/or its Affiliates

from apscheduler.schedulers.blocking import BlockingScheduler
from job import executor
from datetime import datetime, timezone, timedelta

def Streaming():
    print("LogGateWay is running on Streaming mode")
    scheduler = BlockingScheduler()
    scheduler.add_job(executor.run,trigger='cron',minute='0',hour='*') 
    print('Press Ctrl+C to exit')

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

def OnetimePulling():
    print("LogGateWay is running on OnetimePulling mode")
    from_date = datetime.now(timezone.utc) - timedelta(days=5)
    executor.run(from_date)

if __name__ == '__main__':
    Streaming()
    # OnetimePulling()