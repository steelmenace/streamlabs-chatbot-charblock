# CharBlock for Streamlabs Chatbot

This is a custom script for **Streamlabs Chatbot (desktop app)** to block certain character sets (Cyrillic, ASCII-only mode, etc.) in Twitch chat.

## Installation
1. Download this repo as a `.zip` or copy `CharBlock_Streamlabs.py`.
2. Open the Streamlabs Chatbot file and look for the Scripts folder, and then make a folder called `CharBlock`.
3. Place this file `CharBlock_Streamlabs.py` into the new folder `CharBlock`.
4. Now go into Chatbot settings and enable Python scripting (if it's not already enabled).
5. Direct it to your Python install file, then refresh your scripts.
3. Restart Streamlabs Chatbot.
4. In the chatbot, go to **Scripts tab → Enable CharBlock**.

## Commands
- `!charblock on` → enable filtering  
- `!charblock off` → disable filtering  
- `!charblock -cyrillic` → block Cyrillic  
- `!charblock +cyrillic` → allow Cyrillic  
- `!charblock ascii` → toggle ASCII-only mode  

## Notes
- This script uses IronPython 2.7 (Streamlabs Chatbot’s environment).
- Cloudbot does **not** support custom scripts. You must use the **desktop Streamlabs Chatbot app**.
