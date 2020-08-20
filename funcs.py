import download
from telegram.ext import Updater
from glob import glob
import os

updater = Updater("1290917968:AAHR9D-lcdyP2KrALcdH2mtPD6cSNRxIJzQ", use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    msg = "hey\n\n use /help"
    user_id = update.message.chat.id
    context.bot.send_message(chat_id=user_id, text=msg)


def apt_dl(update, context):
    link = context.args
    user_id = update.message.chat.id
    download.aparat_dl(link[0])
    video = glob("aparat-video.*")[0]
    context.bot.send_message(chat_id=user_id, text="Done!")
    context.bot.send_video(chat_id=user_id, video=open(video, "rb"))
    os.unlink(video)


def yt_dl(update, context):
    user_id = update.message.chat.id
    link, quality = context.args
    download.yt_download(link, quality)
    video = glob("yt-video.*")[0]
    context.bot.send_message(chat_id=user_id, text="Done!")
    context.bot.send_video(chat_id=user_id, video=open(video, "rb"))
    os.unlink(video)


def help(update, context):
    msg = "/apt_dl [link]\n\n/yt_dl [link] [quality]\n\n -don't be a fuckin' idiot and don't use [  ]"
    user_id = update.message.chat.id
    context.bot.send_message(chat_id=user_id, text=msg)
