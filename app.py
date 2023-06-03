from message import send_message
from contest import contest_today

# Retrieve information about today's contest
cont = contest_today()

# cont will be None if there is no contest today
if cont is not None:

    next_contest, contest_time, contest_end = cont

    message = f"""
Reminder for today\'s contest
    
Platform: codeforces.com
Round: {next_contest['name']}
Date: Today, {contest_time.strftime('%d %B %Y, %A')}
Time: {contest_time.hour}:{contest_time.minute if contest_time.minute >= 10 else '0' + str(contest_time.minute)} to {contest_end.hour}:{contest_end.minute if contest_end.minute >= 10 else '0' + str(contest_end.minute)}

Don't forget to register if you are participating in the round """ 

    send_message('CY0TwLFKmihGxHTD9HjEM0', message)