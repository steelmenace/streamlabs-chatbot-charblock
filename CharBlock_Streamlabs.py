# ---------------------------
# Streamlabs Chatbot Script
# CharBlocker - Unicode filter with commands
# ---------------------------

import re
import json
import os

# Script info
ScriptName = "CharBlocker"
Description = "Blocks chat messages by character set (Cyrillic, ASCII-only, etc.)"
Creator = "ChatGPT"
Version = "1.0.0"

# ---------------------------
# Global config
# ---------------------------
configFile = os.path.join(os.path.dirname(__file__), "CharBlocker.json")
state = {
    "enabled": False,
    "block_cyrillic": False,
    "ascii_only": False
}

# Regex definitions
REGEX_BLOCKS = {
    "cyrillic": re.compile(u"[\u0400-\u04FF]+"),
    "nonascii": re.compile(u"[^\u0000-\u007F]+")
}

# ---------------------------
# Load / Save state
# ---------------------------
def SaveConfig():
    with open(configFile, "w") as f:
        json.dump(state, f)

def LoadConfig():
    global state
    if os.path.isfile(configFile):
        with open(configFile, "r") as f:
            state = json.load(f)
    else:
        SaveConfig()

# ---------------------------
# Init
# ---------------------------
def Init():
    LoadConfig()
    return

def Execute(data):
    global state

    if not data.IsChatMessage():
        return

    message = data.Message
    user = data.User

    # -------------------
    # Command handling
    # -------------------
    if data.GetParam(0).lower() == "!charblock":
        if data.GetParamCount() == 2:
            arg = data.GetParam(1).lower()
            
            if arg == "on":
                state["enabled"] = True
                Parent.SendStreamMessage("CharBlock: Enabled ✅")
            elif arg == "off":
                state["enabled"] = False
                Parent.SendStreamMessage("CharBlock: Disabled ❌")
            elif arg == "ascii":
                state["ascii_only"] = not state["ascii_only"]
                Parent.SendStreamMessage("CharBlock: ASCII-only mode {}".format("ON" if state["ascii_only"] else "OFF"))
            elif arg == "-cyrillic":
                state["block_cyrillic"] = True
                Parent.SendStreamMessage("CharBlock: Cyrillic blocked 🚫")
            elif arg == "+cyrillic":
                state["block_cyrillic"] = False
                Parent.SendStreamMessage("CharBlock: Cyrillic allowed ✅")
            else:
                Parent.SendStreamMessage("Usage: !charblock [on|off|ascii|-cyrillic|+cyrillic]")
            SaveConfig()
            return

    # -------------------
    # Message filtering
    # -------------------
    if state["enabled"]:
        if state["block_cyrillic"] and REGEX_BLOCKS["cyrillic"].search(message):
            Parent.SendStreamWhisper(user, "Message blocked: Cyrillic not allowed.")
            Parent.DeleteMessage(user, message)
            return

        if state["ascii_only"] and REGEX_BLOCKS["nonascii"].search(message):
            Parent.SendStreamWhisper(user, "Message blocked: Non-ASCII characters not allowed.")
            Parent.DeleteMessage(user, message)
            return

def Tick():
    return
