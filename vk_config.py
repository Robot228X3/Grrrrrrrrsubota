import os

# VK group token (сообщения сообщества -> Настройки -> Работа с API -> Ключи доступа)
VK_GROUP_TOKEN: str = (os.getenv("VK_GROUP_TOKEN", "vk1.a.BdJy8P7Q-XAPVYuUb3Ix8vkjy_BUFuKUI8yDWIeJslpq4uqCbpENQUThTgtrhE7jxU5UO4JQvySnIaPqg3_GYl1nPFLHh2gmTDMpVe6LGxFamCv619tphorhqIB3TQtDrz63tgn5HXHLy0KfaVQJQVcFtA5Z_nmDJ15ea96sCfGCusVCrSnMXdiOc8WjSfFd1sYQbN8aixu8l-gLpN6elw") or "").strip()

# ID сообщества (число). Нужен для некоторых методов/проверок.
VK_GROUP_ID: int = int((os.getenv("VK_GROUP_ID", "238134588") or "0").strip() or "0")

# Список VK user_id админов, которым доступна админ-панель (whitelist).
VK_ADMIN_IDS: list[int] = [
    int(x.strip())
    for x in (os.getenv("1056674561", "1056674561") or "").split(",")
    if x.strip().isdigit()
]

# SQLite файл
VK_DATABASE_PATH: str = (os.getenv("VK_DATABASE_PATH", "vk_bot.sqlite3") or "").strip()

# Таймзона для напоминаний
TIMEZONE: str = (os.getenv("TIMEZONE", "Europe/Moscow") or "").strip()

