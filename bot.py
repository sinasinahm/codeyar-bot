import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)


# =========================================================
# تنظیمات
# =========================================================

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))


# =========================================================
# منوی اصلی
# =========================================================

def main_menu():
    keyboard = [
        [InlineKeyboardButton("⭐ تلگرام استارز", callback_data="stars")],
        [InlineKeyboardButton("🎮 گیفت کارت پلی‌استیشن", callback_data="playstation")],
        [InlineKeyboardButton("🎮 گیفت کارت استیم", callback_data="steam")],
        [InlineKeyboardButton("🍎 گیفت کارت آیتونز", callback_data="itunes")],
        [InlineKeyboardButton("🟢 گیفت کارت ایکس‌باکس", callback_data="xbox")],
        [InlineKeyboardButton("▶️ گیفت کارت گوگل پلی", callback_data="googleplay")],
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================================================
# شروع بات
# =========================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "🛍 به فروشگاه کد یار خوش آمدید!\n\n"
        "محصول مورد نظر خود را انتخاب کنید:"
    )

    await update.message.reply_text(
        text,
        reply_markup=main_menu()
    )


# =========================================================
# Telegram Stars
# =========================================================

async def show_stars(query):

    keyboard = [
        [
            InlineKeyboardButton(
                "⭐ ۱۰۰ استارز",
                callback_data="order:stars:100"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ بازگشت",
                callback_data="main"
            )
        ],
    ]

    await query.edit_message_text(
        "⭐ تلگرام استارز\n\n"
        "مقدار مورد نظر را انتخاب کنید:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================================================
# PlayStation
# =========================================================

async def show_playstation(query):

    keyboard = [
        [
            InlineKeyboardButton(
                "💵 ۱۰ دلار",
                callback_data="order:ps:10"
            )
        ],
        [
            InlineKeyboardButton(
                "💵 ۱۰۰ دلار",
                callback_data="order:ps:100"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ بازگشت",
                callback_data="main"
            )
        ],
    ]

    await query.edit_message_text(
        "🎮 گیفت کارت پلی‌استیشن\n\n"
        "مقدار مورد نظر را انتخاب کنید:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================================================
# Steam - انتخاب ریجن
# =========================================================

async def show_steam_regions(query):

    keyboard = [
        [
            InlineKeyboardButton(
                "🇺🇸 آمریکا",
                callback_data="steam:us"
            )
        ],
        [
            InlineKeyboardButton(
                "🇹🇷 ترکیه",
                callback_data="steam:tr"
            )
        ],
        [
            InlineKeyboardButton(
                "🇦🇷 آرژانتین",
                callback_data="steam:ar"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ بازگشت",
                callback_data="main"
            )
        ],
    ]

    await query.edit_message_text(
        "🎮 گیفت کارت استیم\n\n"
        "ریجن مورد نظر خود را انتخاب کنید:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================================================
# Steam - انتخاب مبلغ
# =========================================================

async def show_steam_amounts(query, region_code):

    regions = {
        "us": "آمریکا",
        "tr": "ترکیه",
        "ar": "آرژانتین",
    }

    region_name = regions[region_code]

    keyboard = [
        [
            InlineKeyboardButton(
                "💵 ۱۰ دلار",
                callback_data=f"order:steam:{region_code}:10"
            )
        ],
        [
            InlineKeyboardButton(
                "💵 ۱۰۰ دلار",
                callback_data=f"order:steam:{region_code}:100"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ بازگشت",
                callback_data="steam"
            )
        ],
    ]

    await query.edit_message_text(
        f"🎮 گیفت کارت استیم\n"
        f"🌎 ریجن: {region_name}\n\n"
        f"مقدار مورد نظر را انتخاب کنید:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================================================
# iTunes
# =========================================================

async def show_itunes(query):

    keyboard = [
        [
            InlineKeyboardButton(
                "💵 ۱۰ دلار",
                callback_data="order:itunes:10"
            )
        ],
        [
            InlineKeyboardButton(
                "💵 ۱۰۰ دلار",
                callback_data="order:itunes:100"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ بازگشت",
                callback_data="main"
            )
        ],
    ]

    await query.edit_message_text(
        "🍎 گیفت کارت آیتونز\n\n"
        "مقدار مورد نظر را انتخاب کنید:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================================================
# Xbox
# =========================================================

async def show_xbox(query):

    keyboard = [
        [
            InlineKeyboardButton(
                "💵 ۱۰ دلار",
                callback_data="order:xbox:10"
            )
        ],
        [
            InlineKeyboardButton(
                "💵 ۱۰۰ دلار",
                callback_data="order:xbox:100"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ بازگشت",
                callback_data="main"
            )
        ],
    ]

    await query.edit_message_text(
        "🟢 گیفت کارت ایکس‌باکس\n\n"
        "مقدار مورد نظر را انتخاب کنید:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================================================
# Google Play
# =========================================================

async def show_googleplay(query):

    keyboard = [
        [
            InlineKeyboardButton(
                "💵 ۱۰ دلار",
                callback_data="order:googleplay:10"
            )
        ],
        [
            InlineKeyboardButton(
                "💵 ۱۰۰ دلار",
                callback_data="order:googleplay:100"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ بازگشت",
                callback_data="main"
            )
        ],
    ]

    await query.edit_message_text(
        "▶️ گیفت کارت گوگل پلی\n\n"
        "مقدار مورد نظر را انتخاب کنید:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================================================
# ثبت سفارش
# =========================================================

async def create_order(query, product, amount):

    user = query.from_user

    username = (
        f"@{user.username}"
        if user.username
        else "بدون یوزرنیم"
    )

    user_name = user.full_name

    order_message = (
        "🛒 سفارش جدید\n"
        "━━━━━━━━━━━━━━\n\n"
        f"📦 محصول: {product}\n"
        f"💵 مقدار: {amount}\n\n"
        f"👤 مشتری: {user_name}\n"
        f"🔗 یوزرنیم: {username}\n"
        f"🆔 آیدی کاربر: {user.id}\n"
    )

    await query.get_bot().send_message(
        chat_id=ADMIN_ID,
        text=order_message
    )

    await query.edit_message_text(
        "✅ سفارش شما با موفقیت ثبت شد!\n\n"
        "💰 قیمت نهایی سفارش توسط ادمین برای شما ارسال خواهد شد.\n\n"
        "❤️ ممنون که کد یار را انتخاب کردید.",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "🛍 بازگشت به فروشگاه",
                    callback_data="main"
                )
            ]
        ])
    )


# =========================================================
# مدیریت دکمه‌ها
# =========================================================

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data

    # -------------------------
    # منوی اصلی
    # -------------------------

    if data == "main":

        await query.edit_message_text(
            "🛍 به فروشگاه کد یار خوش آمدید!\n\n"
            "محصول مورد نظر خود را انتخاب کنید:",
            reply_markup=main_menu()
        )

    # -------------------------
    # محصولات
    # -------------------------

    elif data == "stars":
        await show_stars(query)

    elif data == "playstation":
        await show_playstation(query)

    elif data == "steam":
        await show_steam_regions(query)

    elif data == "itunes":
        await show_itunes(query)

    elif data == "xbox":
        await show_xbox(query)

    elif data == "googleplay":
        await show_googleplay(query)

    # -------------------------
    # Steam region
    # -------------------------

    elif data.startswith("steam:"):

        region_code = data.split(":")[1]

        await show_steam_amounts(
            query,
            region_code
        )

    # -------------------------
    # سفارش
    # -------------------------

    elif data.startswith("order:"):

        parts = data.split(":")

        product_code = parts[1]

        # Telegram Stars
        if product_code == "stars":

            amount = parts[2]

            await create_order(
                query,
                "تلگرام استارز",
                f"{amount} استارز"
            )

        # PlayStation
        elif product_code == "ps":

            amount = parts[2]

            await create_order(
                query,
                "گیفت کارت پلی‌استیشن",
                f"{amount} دلار"
            )

        # Steam
        elif product_code == "steam":

            region_code = parts[2]
            amount = parts[3]

            regions = {
                "us": "آمریکا",
                "tr": "ترکیه",
                "ar": "آرژانتین",
            }

            region_name = regions[region_code]

            await create_order(
                query,
                f"گیفت کارت استیم - {region_name}",
                f"{amount} دلار"
            )

        # iTunes
        elif product_code == "itunes":

            amount = parts[2]

            await create_order(
                query,
                "گیفت کارت آیتونز",
                f"{amount} دلار"
            )

        # Xbox
        elif product_code == "xbox":

            amount = parts[2]

            await create_order(
                query,
                "گیفت کارت ایکس‌باکس",
                f"{amount} دلار"
            )

        # Google Play
        elif product_code == "googleplay":

            amount = parts[2]

            await create_order(
                query,
                "گیفت کارت گوگل پلی",
                f"{amount} دلار"
            )


# =========================================================
# اجرای بات
# =========================================================

def main():

    if not BOT_TOKEN:
        print("خطا: BOT_TOKEN در Environment Variables تنظیم نشده.")
        return

    if not ADMIN_ID:
        print("خطا: ADMIN_ID در Environment Variables تنظیم نشده.")
        return

    app = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    print("بات کد یار در حال اجراست...")

    app.run_polling()


if __name__ == "__main__":
    main()