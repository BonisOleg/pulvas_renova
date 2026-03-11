import requests
from django.conf import settings


def send_order_notification(order) -> bool:
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID

    if not token or not chat_id:
        return False

    color_name = order.shoe_color.name if order.shoe_color else "—"

    text = (
        f"🛍 <b>Нове замовлення #{order.pk}</b>\n\n"
        f"👤 <b>Ім'я:</b> {order.name}\n"
        f"📞 <b>Телефон:</b> {order.phone}\n"
        f"🎨 <b>Колір:</b> {color_name}\n"
        f"📏 <b>Розмір:</b> {order.size}\n\n"
        f"🚚 <b>Місто:</b> {order.city_name}\n"
        f"📦 <b>Відділення:</b> {order.warehouse_name}\n"
    )

    if order.comment:
        text += f"\n💬 <b>Коментар:</b> {order.comment}"

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        response = requests.post(
            url,
            json={"chat_id": chat_id, "text": text, "parse_mode": "HTML"},
            timeout=5,
        )
        return response.ok
    except requests.RequestException:
        return False
