from todoist.api import TodoistAPI
import datetime
import calendar
from datetime import timezone
import requests
import dateutil.parser
import pytz
import time
import schedule
from keep_alive import keep_alive
from filekeys import bot_token, api_key, chat_id

BOT_TOKEN = bot_token
API_KEY = api_key
CHAT_ID = chat_id


class Todoist():
    def __init__(self):
        self.api = TodoistAPI(API_KEY)
        self.api.sync()
        self.tasks = self.api.items.all()

    def convert_time(self, time):
        length = len(time)
        local_timezone = pytz.timezone('America/Toronto')
        time = dateutil.parser.parse(str(time))
        time = str(time.replace(
            tzinfo=timezone.utc).astimezone(tz=local_timezone))
        if length > 10:
            dt = str(dateutil.parser.parse(
                time).strftime('%d %B %H:%M')).split(' ')
        else:
            dt = str(dateutil.parser.parse(time).strftime('%d %B')).split(' ')
        day = calendar.day_name[dateutil.parser.parse(time).weekday()]
        if len(dt) == 2:
            return f'{day}, {dt[0]} {dt[1]}'
        else:
            return f'{day}, {dt[0]} {dt[1]} - {dt[2]}'

    def convert_priority(self, priority):
        if priority == 1:
            return 'Low'
        elif priority == 2:
            return 'Normal'
        elif priority == 3:
            return 'Important'
        else:
            return 'Critical'

    def get_tasks(self):
        tasks = {}
        for task in self.tasks:
            task = task.__dict__
            if task['data']['due'] is not None:
                tasks[task['data']['id']] = {
                    'task': task['data']['content'],
                    'due': task['data']['due']['date'],
                    'priority': task['data']['priority']
                }
        tasks = dict(sorted(tasks.items(), key=lambda kv: kv[1]['due']))
        return tasks

    def get_tasks_week(self):
        tasks = self.get_tasks()
        today = datetime.datetime.today().date()
        week = (datetime.datetime.today() + datetime.timedelta(days=7)).date()
        required_tasks = {}
        for task in tasks:
            task_date = datetime.date(int(tasks[task]['due'][:4]),
                                      int(tasks[task]['due'][5:7]),
                                      int(tasks[task]['due'][8:10]))
            if task_date >= today and task_date <= week:
                clean_date = self.convert_time(tasks[task]['due'].replace(
                    'T', ' ').replace('-', ' '))
                if clean_date[-8:] == ' - 00:00':
                    clean_date = clean_date[:-8]
                required_tasks[task] = {
                    'task': tasks[task]['task'],
                    'due': clean_date,
                    'priority': self.convert_priority(tasks[task]['priority']),
                }
        return required_tasks


def main():
    td = Todoist()
    tasks = td.get_tasks_week()
    message = f'''
A Snapshot of Your Next 7 Days:

'''
    if tasks != {}:
        for task in tasks:
            message += f'''
Name: {tasks[task]["task"]}
Time: {tasks[task]["due"]}
Priority: {tasks[task]["priority"]}

-----------------------------------------------------------------

'''
    else:
        message += 'No tasks scheduled for the next 7 days.\n\n'
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url)


schedule.every().day.at('02:30').do(main)
keep_alive()
while True:
    schedule.run_pending()
    time.sleep(1)
