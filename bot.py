"""
ALPHA AI - Bot Telegram de publication automatique
====================================================

Ce bot publie automatiquement du contenu (texte + image optionnelle) sur un
canal ou groupe Telegram, selon un planning défini dans posts.json.

Fonctionnement :
- Au démarrage, le bot lit posts.json
- Chaque post a une date/heure de publication (format ISO)
- Un scheduler vérifie chaque minute s'il y a un post à publier
- Une fois publié, le post est marqué "sent": true pour ne pas être republié

Configuration : voir le fichier .env.example
"""

import os
import json
import logging
import asyncio
from datetime import datetime
from pathlib import Path

from telegram import Bot
from telegram.error import TelegramError
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

# --- Configuration ---------------------------------------------------------

load_dotenv()  # charge les variables depuis le fichier .env

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # ex: @moncanal ou -1001234567890
POSTS_FILE = Path(__file__).parent / "posts.json"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("alpha-bot")

if not BOT_TOKEN or not CHAT_ID:
    raise RuntimeError(
        "TELEGRAM_BOT_TOKEN et TELEGRAM_CHAT_ID doivent être définis "
        "dans le fichier .env (voir .env.example)."
    )

bot = Bot(token=BOT_TOKEN)


# --- Gestion des posts ------------------------------------------------------

def load_posts():
    """Charge la liste des posts depuis posts.json."""
    if not POSTS_FILE.exists():
        logger.warning("posts.json introuvable, création d'un fichier vide.")
        save_posts([])
        return []
    with open(POSTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_posts(posts):
    """Sauvegarde la liste des posts dans posts.json."""
    with open(POSTS_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)


async def publish_post(post: dict):
    """Publie un post unique sur Telegram (texte + image optionnelle)."""
    try:
        if post.get("image"):
            image_path = Path(__file__).parent / "media" / post["image"]
            if image_path.exists():
                with open(image_path, "rb") as photo:
                    await bot.send_photo(
                        chat_id=CHAT_ID,
                        photo=photo,
                        caption=post.get("text", ""),
                    )
            else:
                logger.error("Image introuvable: %s — envoi en texte seul.", image_path)
                await bot.send_message(chat_id=CHAT_ID, text=post.get("text", ""))
        else:
            await bot.send_message(chat_id=CHAT_ID, text=post.get("text", ""))

        logger.info("Post publié: %s", post.get("id"))
        return True

    except TelegramError as e:
        logger.error("Erreur Telegram lors de la publication de %s: %s", post.get("id"), e)
        return False


# --- Boucle de vérification --------------------------------------------------

async def check_and_publish():
    """Vérifie les posts à publier et les envoie si leur heure est arrivée."""
    posts = load_posts()
    now = datetime.now()
    changed = False

    for post in posts:
        if post.get("sent"):
            continue

        try:
            scheduled_time = datetime.fromisoformat(post["datetime"])
        except (KeyError, ValueError):
            logger.error("Date invalide pour le post %s, ignoré.", post.get("id"))
            continue

        if scheduled_time <= now:
            success = await publish_post(post)
            if success:
                post["sent"] = True
                changed = True

    if changed:
        save_posts(posts)


# --- Démarrage ---------------------------------------------------------------

async def main():
    logger.info("ALPHA AI Bot démarré. Vérification des posts toutes les 60s.")

    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_and_publish, "interval", seconds=60)
    scheduler.start()

    # vérification immédiate au lancement
    await check_and_publish()

    # garde le programme actif indéfiniment
    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
