from message import send_message
from contest import contest_today

# Retrieve information about today's contest
cont = contest_today()

# cont will be None if there is no contest today
if cont is not None:

    next_contest, contest_time = cont

    message = f"""
Gentle reminder for today\'s contest
    
Platform: codeforces.com
Round: {next_contest['name']}
Date: Today, {contest_time.strftime('%d %B %Y, %A')}
Time: {contest_time.hour}:{contest_time.minute if contest_time.minute >= 10 else '0' + str(contest_time.minute)}

Don't forget to register if you are participating in the round """ 
    
    send_message('Bn3CPQ66yOh9ewXVp93hMv', message)

