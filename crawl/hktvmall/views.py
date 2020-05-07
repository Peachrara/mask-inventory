import os

# Create your views here.
from django.http import HttpResponse
from django.views.static import serve
from apscheduler.schedulers.background import BackgroundScheduler
from hktv import crawlHKTV
from datetime import datetime

filepath = os.getcwd() + "/hktv.json"
sched = BackgroundScheduler()

@sched.scheduled_job('interval', minutes=3, next_run_time=datetime.now())
def timed_job():
    print('This job is run every three minutes.')
    try:
        crawlHKTV()
    except:
        print("Error occured")


sched.start()


def index(request):
    if not os.path.isfile(filepath):
        return HttpResponse("Crawling")
    else:
        return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
