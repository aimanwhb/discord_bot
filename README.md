# WORK IN PROGRESS....

# Discord Bot: AI integration and other cool features

Welcome to the **Len2code Discord Bot**! This bot is designed to help users to explore exciting features like AI integration, moderation tools, and fun commands. It’s perfect for communities looking to streamline communication and engagement.

---

## Table of Contents
1. [Features](#features)
2. [Documentation](#documentation)
3. [Getting Started](#getting-started)
4. [Support](#support)

---

## Features

The bot offers a variety of features to enhance your server experience. Use the `!menu` command to explore the following options:

### **AI Integration** 🤖
Interact with AI-powered features to get answers, generate text, or receive recommendations.  
**Example Command**: `!ask <question>`  
**Response**: "The bot is powered by AI to assist you with various tasks. Try `!ask <question>` to interact with the AI."

### **Moderation Tools** 🔒
Keep your server safe and organized with powerful moderation tools.  
**Example Commands**:
- `!kick <user>`: Remove a user from the server.
- `!mute <user>`: Restrict a user’s ability to send messages.

### **Fun Commands** 🎉
Enjoy fun and interactive commands to keep your server lively.  
**Example Commands**:
- `!joke`: Get a random joke.

### **Server Analytics** 📊
Track server activity and gain insights into member engagement.  
**Example Command**: `!stats` `!uptime` `!stats` `!userstats @<username>`.

**Response**: Displays message counts, active members, bot uptime and more.

---

## Documentation

The bot also provides easy access to important documentation. Use the `!menu` command to explore the following options:

### **Help** ❓
Get help with using the bot and its commands.  
**Response**: "Welcome to the bot! Use `!menu` to see available options. For more help, contact the admin."

### **Bot Installation** 📘
How to run the discord bot  
**Response**: "To clone a repo, install dependencies, update .env file and run the bot locally."

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- A Discord bot token (get it from the [Discord Developer Portal](https://discord.com/developers/applications))

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/len2kode/discord_bot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ./discord_bot
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a .env file and add below:
   ```bash
   LOG_LEVEL="<DEBUG/INFO/WARNING/ERROR/CRITICAL>"
   DISCORD_TOKEN="<Discord bot token>"
   DISCORD_GUILD="<Guild name>"
   AI_MODEL="meta-llama/llama-3.2-3b-instruct:free"
   AI_ENDPOINT="<API URL>"
   AI_TOKEN="<Your token>"
   ```
5. Run the bot:
   ```bash
   python main.py
   ```
