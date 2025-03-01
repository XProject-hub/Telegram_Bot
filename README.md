# Always-On Telegram Bot: Message Re-Sender

This project contains a Telegram bot that listens to a source Telegram group and re-sends messages (text, images, videos, etc.) to a destination group without displaying the original sender's details (i.e. no "Forwarded from" header). This bot uses the legacy version of the python-telegram-bot library (v13.15).

> **Important:** This project requires python-telegram-bot version 13.15. Please follow the installation instructions below.

---

## Table of Contents

- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [Running the Bot](#running-the-bot)
- [Deploying as a Systemd Service](#deploying-as-a-systemd-service)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Installation & Setup

### 1. Clone the Repository

Clone this repository to your local machine or server:
bash
git clone https://github.com/XProject-hub/Telegram_Bot.git
cd Telegram_Bot

2. Install Prerequisites
Ensure your system meets the following requirements:

Operating System: Linux (Ubuntu is recommended)
Python: 3.6 or later
pip: Python package installer
Update your package list and install Python & pip:

sudo apt update
sudo apt install python3 python3-pip -y

3. (Optional) Set Up a Virtual Environment
Using a virtual environment is recommended. In the repository folder, run:

python3 -m venv venv
source venv/bin/activate

Your prompt should now begin with (venv).

4. Install the Required Python Package
Install the legacy version of python-telegram-bot (v13.15):

pip install --force-reinstall python-telegram-bot==13.15


Configuration
Edit the Bot Script
Open the file telegram_bot.py in your favorite editor and update the following variables:

TOKEN: Replace "YOUR ACTUAL TELEGRAM BOT API" with your actual Telegram Bot API token.
SOURCE_CHAT_ID: Set this to the ID of the source Telegram group (as a negative integer).
DESTINATION_CHAT_ID: Set this to the ID of the destination Telegram group (as a negative integer).

# --- Configuration ---
SOURCE_CHAT_ID = -xxxxxxx      # Group where messages originate
DESTINATION_CHAT_ID = -xxxxxxx  # Group where messages will be re-sent

Edit the Systemd Service File (Optional)
If needed, adjust the file telegram_bot.service (e.g., change the paths or the user) to suit your environment.

Running the Bot
To test the bot locally, simply run:

python3 telegram_bot.py

You should see logging messages indicating that the bot is running and processing messages from the source group.


Deploying as a Systemd Service
To keep your bot running continuously—even after you close your SSH session or reboot the server—set it up as a systemd service.

1. Move the Service File
Copy the provided telegram_bot.service file to the systemd directory:

sudo cp telegram_bot.service /etc/systemd/system/

2. Reload and Enable the Service
Reload systemd to recognize the new service:

sudo systemctl daemon-reload

Enable the service to start automatically on boot:

sudo systemctl enable telegram_bot.service

Start the service:

sudo systemctl start telegram_bot.service

3. Verify the Service Status
Check that your service is running:

sudo systemctl status telegram_bot.service


Usage
Editing:
Modify telegram_bot.py as needed. If you update the code, restart the service:

sudo systemctl restart telegram_bot.service

Monitoring:
Use journalctl or systemctl status telegram_bot.service to monitor the bot's activity.