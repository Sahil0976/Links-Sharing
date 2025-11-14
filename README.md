# 📱 Advanced Link Sharing Bot

Welcome to the **Advanced Link Sharing Bot**! 🚀

This bot is designed to help you **keep your channels safe** from copyright issues while sharing links in a simple and secure manner. If you just want to ensure that your content stays protected, this bot has got your back! 💪

---

## 🌟 Features

- **Secure Link Sharing**: Share your links without worrying about copyright strikes! 📤
- **Advanced Protection**: Safeguard your channel from malicious or harmful links! 🔒
- **Easy-to-use**: Simply use `/start` and get started with a smooth experience. 🚀
- **Admin Controls**: Access commands to manage your channels and users with ease! 🛠️

---

## 🚀 Deployment

### 🌍 Deploy on **Heroku**

*Before you deploy on HEROKU, you should fork the repo and change its name*<br>

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)</br>

---

### 🖥️ Deploy on **VPS**

If you're using a VPS (Virtual Private Server), follow these steps:

1. **Edit config.py then Clone the repository** to your VPS.
    ```bash
    git clone https://github.com/{github_username}/{repo_name}
    cd {repo_name}
    ```
2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the bot with:
    ```bash
    python main.py
    ```
4. Your bot will start running. You can keep it running in the background using **screen** or **tmux**.

---

## 🔑 Secrets (Environment Variables)

Add the following environment variables to ensure the bot runs smoothly:

- **TG_BOT_TOKEN**: Your bot's Telegram token.
- **APP_ID**: Your Telegram App ID (get it from [my.telegram.org](https://my.telegram.org)).
- **API_HASH**: Your Telegram API hash.
- **OWNER_ID**: Your Telegram user ID.
- **PORT**: Port number (usually `8080` for Heroku, or any port on VPS).
- **DATABASE_URL**: The MongoDB database URI.
- **DATABASE_NAME**: The name of your database.

---

## ⚡ Commands

Here are all the commands you can use with the bot:

- `start`: Start the bot and get a welcome message! 🏁
- `broadcast`: Send a message to all users! 📢
- `users`: List all users who have interacted with the bot. 📋
- `channelpost`: Generate invite links for your channels. 🔗
- `reqpost`: Generate request invite links for your channels. 📩
- `setchannel`: Set a channel to manage with the bot. ⚙️
- `delchannel`: Remove a channel from the bot's control. ❌
- `stats`: Check bot usage and other statistics! 📊
- `addfsub`: Add a force subscribe channel. ➕
- `rmfsub`: Remove the force subscribe channel. ➖
- `fsub`: Show the current force subscribe channel. ℹ️

---

## 🧑‍💻 Credits

This bot is powered by **[Seishiro Nagi](https://t.me/The_Seishiro_Nagi)** 🙏. Huge thanks to **Seishiro Nagi** for the awesome creation and constant support! 🔥

---

## 📞 Contact

- Telegram: [@the_Seishiro_Nagi](https://t.me/The_Seishiro_Nagi) 📱
- Join Support Channel: [Anime Hunters](https://t.me/Anime_X_Hunters) 🆘

---

### ⭐️ Thank you for using this bot! ⭐️

We hope you find it helpful. Stay protected and share links safely! 🌐
