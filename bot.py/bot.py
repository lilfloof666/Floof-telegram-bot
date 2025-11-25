import time
import os
import telebot

# 🔐 Deinen Bot-Token hier einsetzen
# Wenn du magst: vorher in BotFather einen NEUEN Token holen.
BOT_TOKEN = "8327139268:AAHldpid7j19JuxonZ6G5mimJEuLP1ZKzc8"

# 👉 Dein Kanal (wo der Bot Admin ist)
CHAT_ID = "@lilfloofcreations"

# ✨ Dein Floof-Style Text – zweisprachig
MESSAGE_TEXT = (
    "⏳ Reminder / Erinnerung\n"
        "\n"
            "EN: 24 hours left until the winner gets their FREE artwork!\n"
                "DE: Noch 24 Stunden, dann bekommt der Gewinner sein GRATIS Artwork!\n"
                    "\n"
                        "🩸🖤 lil floof creations 🖤🩸"
                        )

                        # ⏰ Alle 2 Stunden, insgesamt 24h
                        INTERVAL = 2 *