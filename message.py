import pywhatkit
from keyboard import press
from datetime import datetime, timedelta

def send_message(group_id, message):
    """ Send a WhatsApp message to a group now.

    Args:
        group_id: A string that is the unique identifier of a WhatsApp group.
            It is the suffix of the group's invite link.
        message: A string containing the message to be sent

    Examples:
        >>> msg = 'Hello, world!'
        >>> grp = 'Bn3CPQ66yOh9ewXVp93hMv'
        >>> send_message(grp, msg)
    """

    # Get current time and add one minute 
    # in case the function is called near the end of a minute
    now = datetime.now()
    now = now + timedelta(minutes=1)

    # Open WhatsApp Web and type the message in the corresponding group
    pywhatkit.sendwhatmsg_to_group(group_id, message, now.hour, now.minute, 10, False)

    # Press the 'Enter' key to send the message
    press('enter')