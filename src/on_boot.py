import fire
import requests
import socket

from datetime import datetime

TOKEN = "5263324187:AAEzg4JaT-rDQYPHXc200RrSV90RpYK8rKE"
CHAT_ID = "168421237"

import socket


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def on_boot():
    dt = datetime.now()

    ip =  get_ip()

    message = f"""
    Server boot at {dt}
    ip: {ip}
    """
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}")


if __name__ == '__main__':
  fire.Fire(on_boot)
