from telegram.ext import CommandHandler
import funcs


def main():
    start_handler = CommandHandler("start", funcs.start)
    funcs.dispatcher.add_handler(start_handler)

    apt_dl_handler = CommandHandler("apt_dl", funcs.apt_dl)
    funcs.dispatcher.add_handler(apt_dl_handler)

    yt_dl_handler = CommandHandler("yt_dl", funcs.yt_dl)
    funcs.dispatcher.add_handler(yt_dl_handler)

    help_handler = CommandHandler("help", funcs.help)
    funcs.dispatcher.add_handler(help_handler)

    funcs.updater.start_polling()


if __name__ == "__main__":
    main()
