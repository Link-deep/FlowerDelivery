import requests
from django.conf import settings

def send_telegram_message(order):

    message = (
        f"🛒 *Новый заказ!*\n"
        f"📦 *Игра:* {order.game.title}\n"
        f"📅 *Дата заказа:* {order.created_at.strftime('%d.%m.%Y %H:%M')}\n"
        f"💰 *Стоимость:* {order.total_price} ₽\n"
        f"📍 *Адрес доставки:* {order.address}"
    )

    photo_path = order.game.image.path

    # Отправляем фото и текст
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendPhoto"

    data = {
        "chat_id": settings.TELEGRAM_CHAT_ID,
        "caption": message,
        "parse_mode": "Markdown",
    }

    # Открываем файл и отправляем его в Telegram
    with open(photo_path, "rb") as photo:
        files = {"photo": photo}
        response = requests.post(url, data=data, files=files)

    return response.json()
