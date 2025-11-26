"""
import time
import os
from datetime import datetime, timedelta
import telebot

# \U0001F510 Deinen Bot-Token hier einsetzen oder besser: als Umgebungsvariable TELEGRAM_BOT_TOKEN
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8327139268:AAHldpid7j19JuxonZ6G5mimJEuLP1ZKzc8")

# \U0001F449 Dein Kanal (wo der Bot Admin ist)
CHAT_ID = "@lilfloofcreations"

bot = telebot.TeleBot(BOT_TOKEN)

def next_15_clock(now: datetime) -> datetime:
    """
    Gibt das nächste Datum/Uhrzeit-Objekt für 15:00 (heute oder morgen) zurück.
    """
    target = now.replace(hour=15, minute=0, second=0, microsecond=0)
    if target <= now:
        target = target + timedelta(days=1)
    return target

def format_delta(delta: timedelta) -> (int, int, int):
    total_seconds = int(delta.total_seconds())
    hours, rem = divmod(total_seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return hours, minutes, seconds

def build_message(hours: int, minutes: int, seconds: int) -> str:
    return (
        "⏳ Countdown bis 15:00 / Countdown until 3:00 PM\n\n"
        f"DE: Noch {hours} Stunden, {minutes} Minuten, {seconds} Sekunden bis 15:00 Uhr!\n"
        f"EN: {hours} hours, {minutes} minutes, {seconds} seconds left until the winner gets their FREE artwork!\n\n"
        "🩸🖤 lil floof creations 🖤🩸"
    )

def seconds_to_next_hour(now: datetime) -> int:
    """Sekunden bis zur nächsten vollen Stunde."""
    seconds_past_hour = now.minute * 60 + now.second
    return 3600 - seconds_past_hour if seconds_past_hour != 0 else 3600

def run_hourly_until_15():
    try:
        now = datetime.now()
        target = next_15_clock(now)
        print(f"[{now.isoformat()}] Countdown gestartet, Ziel: {target.isoformat()}")

        # Sofort eine Nachricht senden
        while now < target:
            delta = target - now
            hours, minutes, seconds = format_delta(delta)
            text = build_message(hours, minutes, seconds)
            try:
                bot.send_message(CHAT_ID, text)
                print(f"[{datetime.now().isoformat()}] Gesendet: {hours}h {minutes}m {seconds}s verbleibend")
            except Exception as e:
                print(f"Fehler beim Senden der Nachricht: {e}")

            # Wenn Ziel bereits erreicht (kann nach send vorkommen), abbrechen
            now = datetime.now()
            if now >= target:
                break

            # Auf die nächste volle Stunde warten, dann erneut senden (jede Stunde)
            wait = seconds_to_next_hour(now)
            print(f"Warte {wait} Sekunden bis zur nächsten vollen Stunde...")
            time.sleep(wait)
            now = datetime.now()

        # Ziel (15:00) erreicht — Abschlussnachricht senden
        final_text = (
            "🎉 Zeit ist abgelaufen! / Time's up!\n\n"
            "DE: Die Frist um 15:00 Uhr ist erreicht — der Gewinner erhält sein GRATIS Artwork!\n"
            "EN: The deadline at 3:00 PM has been reached — the winner will receive their FREE artwork!\n\n"
            "🩸🖤 lil floof creations 🖤🩸"
        )
        try:
            bot.send_message(CHAT_ID, final_text)
            print(f"[{datetime.now().isoformat()}] Ziel erreicht - Abschlussnachricht gesendet.")
        except Exception as e:
            print(f"Fehler beim Senden der Abschlussnachricht: {e}")

    except KeyboardInterrupt:
        print("Countdown gestoppt (KeyboardInterrupt).")

if __name__ == "__main__":
    if not BOT_TOKEN:
        raise SystemExit("Fehler: Kein BOT_TOKEN gesetzt. Bitte TELEGRAM_BOT_TOKEN als Umgebungsvariable setzen oder den Token direkt im Skript hinterlegen.")
    run_hourly_until_15()
"""