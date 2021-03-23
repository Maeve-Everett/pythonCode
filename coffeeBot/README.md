# Coffee Bot
This was a program that I made back in 2018. I was working with a friend who needed some help with the Python code of a small project. This project was a Raspberry Pi that would tell you when your coffee was ready through a screen on the Pi and a Slack bot. There are a lot of problems with this code, from redundant and imported twice libraries to using Linux environment variables for the OAuth token, but to be honest I'm scared to touch any of this code for fear that it will explode. Dispite its many issues, it worked and was my first time making a bot.

## Requirements
You need quite a bit for this and I'm doubtful that it even works anymore but if you want to give it a shot then you will need an Inky pHAT and a BME680.

For the Python side of things, these are the dependencies of the script.

| Dependencies |
| --- |
| icalendar |
| slackclient |
| inkyphat |
| bme680 |

## Usage
This is just copied and pasted from the short bit of documentation that I wrote for this so there is a high chance that this won't work properly but the general gist of it all should still be fine.

1. Go to https://api.slack.com/apps?new_app=1 and enter the name and set the workspace for your bot and click create app
2. Once the settings page for your new bot has loaded, go to Bot Users under the Features heading on the side of the page.
3. Set the display name to something like 'Coffee Bot' and the username to 'coffeebot' and click save changes
4. Then go to the OAuth & Permissions tab that is just above the Bot Users tab
5. Click Install App to Workspace and then Authorize
6. Click Copy on the Bot User OAuth Access Token box
7. Then go to the Slack Channel that you want the bot to message
8. Open PuTTY or something similar to access the Raspberry Pi
9. Navigate to the file that the program was saved to using the cd command - e.g. `cd /your/file/path/here`
10. Enter `export SLACK_TOKEN=(right click here)`
11. Obviously, don't actually enter 'right click here' but right click at that spot to paste the OAuth Token
12. Enter 'nano coffeeBot.py'
13. Change Channel Id Here on lines 61 and 67 (you can find out what line you are on by hitting ctrl+c) to the bit after /messages/ in the url of your channel - e.g. `yourchannel.slack.com/messages/*this bit*/`
14. Hit ctrl+x then y and then enter and you are done
15. When you want the program to run, type `python coffeeBot.py` in the file that has the bot file in