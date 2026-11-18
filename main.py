
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BOT_NAME = "FA Trading Bot"
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "مرحباً بك في FA Trading Bot 🚀\n\n"
        "بوتك جاهز لاستقبال أوامر التداول.\n\n"
        "الأوامر المتاحة:\n"
        "/start - تشغيل البوت\n"
        "/help - المساعدة\n"
        "/status - حالة البوت\n"
        "/signal - حالة نظام الإشارات\n\n"
        "السوق المستهدف: EUR/USD OTC"
    )
    await update.message.reply_text(message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "FA Trading Bot 🤖\n\n"
        "/start - البداية\n"
        "/status - فحص التشغيل\n"
        "/signal - فحص نظام الإشارات\n"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "FA Trading Bot 🟢\n"
        "حالة اتصال تيليجرام: يعمل\n"
        "السوق المستهدف: EUR/USD OTC\n"
        "نظام الإشارات: بانتظار ربط مصدر البيانات"
    )


async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 FA Trading Bot\n\n"
        "نظام تحليل EUR/USD OTC لم يُفعّل بعد.\n"
        "نحتاج أولاً إلى مصدر بيانات موثوق للأسعار والشموع.\n\n"
        "لن نرسل توصية شراء أو بيع دون بيانات فعلية."
    )


def main():
    if not TOKEN:
        raise RuntimeError(
            "Missing TELEGRAM_BOT_TOKEN environment variable"
        )

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("signal", signal))

    logging.info("%s is starting...", BOT_NAME)
    app.run_polling()


if __name__ == "__main__":
    main()
