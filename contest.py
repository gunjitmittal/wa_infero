import json
import urllib
from datetime import datetime, timedelta

# Codeforces API for obtaining the list of all contests
# Documentation: https://codeforces.com/apiHelp/methods#contest.list
URL = 'https://codeforces.com/api/contest.list'

def contest_today():
    """ Return information about a Codeforces contest happening today.

    Returns:
        A tuple (next_contest, contest_time) where next_contest is the JSON Contest object
        in the Codeforces API containing information about the next contest happening on the
        day the function is called and contest_time is a datetime object corresponding to the
        start time of the contest.

    Raises:
        HTTPError: Failed to connect to Codeforces.
    """

    with urllib.request.urlopen(URL) as url:
        contests = json.loads(url.read().decode())

        # Request was successful
        if contests['status'] == 'OK':
            
            # List of all contest object dictionaries
            contests = contests['result']
            next_contest = contests[0]
            least_start_time = contests[0]['startTimeSeconds']
            
            # Find the earliest contest that has not taken place already
            for contest in contests:
                if contest['phase'] == 'BEFORE' and contest['startTimeSeconds'] < least_start_time:
                    next_contest = contest
                    least_start_time = contest['startTimeSeconds']

            # Convert Unix timestamp to UTC
            contest_time = datetime.utcfromtimestamp(least_start_time)

            # Convert UTC to IST
            contest_time += timedelta(hours=5, minutes=30)

            # If the next contest is today
            if (contest_time.day == datetime.now().day 
                    and contest_time.month == datetime.now().month
                    and contest_time.year == datetime.now().year):
                return next_contest, contest_time

        # Request failed
        else:
            raise urllib.error.HTTPError('Failed to connect to Codeforces')