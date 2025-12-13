import network
import socket
import time
import sys
import urequests as requests   # preinstalled on Pico W

SSID = "Babu_17"
PASSWORD = "heslo.heslo123"

def wifi_connect() -> str | None:
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print("Connecting to WiFi...")
    for _ in range(20):
        if wlan.isconnected():
            ip = wlan.ifconfig()[0]
            print(f"Connected! Local IP: {ip}")
            return ip
        time.sleep(0.5)

    print("Failed to connect to WiFi.")
    return None


def check_internet() -> bool:
    try:
        r = requests.get("https://google.com")
        print("Internet OK:", r.status_code)
        return r.status_code == 200
    except:
        print("No internet connection detected.")
        return False


def webpage() -> str:
    return """\
<!DOCTYPE html>
<html>
<head>
<title>Pico Server</title>
<style>
body { background:#f5f5f5; font-family:Arial; text-align:center; }
h1 { color:#333; padding-top:40px; }
</style>
</head>
<body>
<h1>Hello from Raspberry Pi Pico W!</h1>
<p>This is your web server :)</p>
</body>
</html>
"""


def server(ip):
    import socket
    addr = (ip, 80)
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)
    print("Web server running at: http://" + ip)

    while True:
        try:
            conn, addr = s.accept()
            request = conn.recv(1024).decode()
            print("Request received\n", request)

            response = webpage()
            conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
            conn.send(response)
            conn.close()

        except KeyboardInterrupt:
            print("Server stopped.")
            sys.exit()


def main():
    ip = wifi_connect()
    if ip is None:
        sys.exit(1)

    check_internet()
    server(ip)


if __name__ == "__main__":
    main()