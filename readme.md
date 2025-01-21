# Internship Assessment
### **Tasks**

Create a telegram bot that will:
- Continuously listen to messages sent in `Group A` inside the `Topic 1` thread.
- Forward the message from `Group A` to `Group B` inside the `Topic 2` thread.
- Add `/start` and `/stop` commands to the bot such that they can be accessed only by the Admin.

# Setup
Follow the steps below:

## Create a Telegram bot
- Open Telegram and search for **BotFather**
- Start Chat and use `/newbot` command.
- Follow the instructions to name the bot and provide a username ending with **bot** keyword.

## Create Two Groups and topics inside them and add bot to the groups with admin permissions.

Clone Repository:
```bash
git clone https://github.com/Babban33/temporary-bot.git
```

Move inside the root directory:
```bash
cd temporary-bot
```

Create Python virtual Environment:
```bash
python -m venv venv
venv\Scripts\activate
```

Install Libraries:
```bash
python install -r requirements.txt
```

Get the token and create an `.env` file and populate it with:
```bash
BOT_TOKEN=<YOUR_TOKEN>
```


Get The Group, Topic and Admin ID:
```bash
python getIds.py
```

Add Id's in .env file. Your env file should look like this:
```bash
BOT_TOKEN=<YOUR_TOKEN>
GROUP_A_ID=<ID>
GROUP_B_ID=<ID>
TOPIC_1_ID=<ID>
TOPIC_2_ID=<ID>
ADMIN_USER_ID=<ID>
```

Run Application:
```bash
python telegram_topic_forwarder.py
```
