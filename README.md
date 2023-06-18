# Infero WhatsApp Bot
This application automates Codeforces contest reminders for the Infero WhatsApp group. Contest data is extracted using the [Codeforces API](https://codeforces.com/apiHelp) and the WhatsApp messages are sent using [PyWhatKit](https://github.com/Ankit404butfound/PyWhatKit). The messages will be sent through the user's [WhatsApp Web](https://web.whatsapp.com/) account.

## Installation
Clone the `single-contest` branch (handles one contest in a day properly)
```
git clone -b single-contest --single-branch https://github.com/gunjitmittal/wa_infero.git
```

or alternatively download the ZIP file directly either from GitHub or as follows
```
wget https://github.com/gunjitmittal/wa_infero/archive/refs/heads/single-contest.zip
```

Install the necessary requirements
```
pip install -r requirements.txt
```

## Usage
In `app.py`, include the group IDs of the WhatsApp groups that you want to send the message to, in the dictionary `groups`. The ID of a WhatsApp group can be obtained from its group invite link. For example, if the invite link is `https://chat.whatsapp.com/CY0TwLFKmihGxHTD9HjEM0` then the group ID is `CY0TwLFKmihGxHTD9HjEM0`. After the dictionary `groups` is ready, you can now run the script to send your message in the chosen WhatsApp groups. 
```
python app.py
```

This will open a [WhatsApp Web](https://web.whatsapp.com/) window in your default browser, so make sure you are logged in to WhatsApp Web as the message will be sent through your account. The time required for sending the message will be displayed in your terminal.
