<div id="top"></div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This is a Telegram bot I made to keep me on track for all my upcoming tasks and ensures I don't forget anything.
The bot fetches all your events and tasks through Todoist. In order to use the bot, you need to have a Todoist account. The bot sends a message everyday at 10:30 PM with all the tasks and events you have for the next 7 days.
Currently, the bot does not do anything else but I plan to add more features in the future. Feel free to suggest features and/or contribute yourself.

NOTE: You need to add your events and tasks to Todoist in order for the bot to work. (For Google Calendar events, you can just sync your Todoist account with Google Calendar)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

1. Make a Telegram account if you haven't already.
1. Create a Telegram bot and get the Bot token by following the steps [here](https://core.telegram.org/bots#6-botfather). Save the bot token somewhere safe.
1. Open your Telegram app and send any message to the bot you just created.
1. Create a Todoist account if you haven't already.
1. Create a Todoist API token by:
    1. Going to Todoist Settings tab and clicking on Integrations.
    1. Scroll down to the bottom and copy the "API token" and save it somewhere safe.
1. Run the `chat_id.py` script. The script will print your chat id. Save it somewhere safe.
1. Make a `filekeys.py` file in the directory and add the following lines:

```python
bot_token = "YOUR_BOT_TOKEN"
api_key = "YOUR_API_KEY"
chat_id = "YOUR_CHAT_ID"
```

8. Create a Repl.it account if you haven't already.
1. Upload the files to Repl.it and run the `reminder.py` script.
1. Copy the url in the "webview" tab on Repl.it and save it somewhere safe.
1. Go to [UptimeRobot](https://uptimerobot.com/) and create an account if you haven't already.
1. Create a new Monitor on UptimeRobot and select HTTP(s) as the type, paste the url you copied earlier in the URL field and select 5 minutes as the interval.
1. Voila! You're done. The bot will now send you a message everyday at 10:30 PM with all your tasks and events for the next 7 days.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Pratyush Shah - <a href = "mailto: pratyushvshah@gmail.com">Email</a>, [LinkedIn](https://www.linkedin.com/in/pratyushvshah/)

Project Link: [https://github.com/pratyushvshah/Reminder](https://github.com/pratyushvshah/Reminder)

<p align="right">(<a href="#top">back to top</a>)</p>
