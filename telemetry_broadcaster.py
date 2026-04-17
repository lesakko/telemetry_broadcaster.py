import requests
from datetime import datetime, timezone

# REDACTED FOR GITHUB SECRECY
WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN"
APP_VERSION = "1.1.5"

def send_discord_telemetry(message: str, title: str = "System Alert", color: int = 3447003):
    """
    [PUBLIC SHOWCASE] 
    Transmits rich, color-coded telemetry payloads to the secure Discord Command Center.
    """
    if not WEBHOOK_URL or "YOUR_WEBHOOK_ID" in WEBHOOK_URL:
        print("[WARNING] Telemetry broadcast aborted. Webhook URL missing.")
        return False

    payload = {
        "embeds": [{
            "title": title,
            "description": message,
            "color": color,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "footer": {
                "text": f"Kvantix Pro v{APP_VERSION} | AI Trading Terminal"
            }
        }]
    }

    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=5)
        if response.status_code in [200, 204]:
            print(f"[TELEMETRY] Successfully broadcasted '{title}' to Command Center.")
            return True
        else:
            print(f"[TELEMETRY ERROR] Server returned HTTP {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"[TELEMETRY FATAL] Connection dropped: {e}")
        return False
