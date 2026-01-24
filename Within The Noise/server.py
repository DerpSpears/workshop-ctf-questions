import socket
import random
import datetime
import time

HOST = '0.0.0.0'
PORT = 9999
FLAG = "tac{w0w_n0w_u_s33_m3}"

def caesar_cipher(text, shift=4):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def get_timestamp():
    return datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')

def generate_http(inject_flag=False):
    codes = ["200 OK", "302 Found", "404 Not Found", "503 Service Unavailable"]
    headers = [
        f"Date: {get_timestamp()}",
        f"Server: Apache/2.4.50 (Unix)",
        f"Content-Type: text/html; charset=UTF-8",
        f"Connection: keep-alive"
    ]
    if inject_flag:
        encrypted_flag = caesar_cipher(FLAG, shift=4)
        headers.append(f"X-Debug-Trace-ID: {encrypted_flag}")
        headers.append(f"X-Runtime: 0.045s")
    else:
        headers.append(f"X-Request-ID: {random.randint(10000,99999)}")

    header_str = "\r\n".join(headers)
    body = "<html><body><h1>System Status</h1><p>Operation completed.</p></body></html>"
    return (
        f"HTTP/1.1 {random.choice(codes)}\r\n"
        f"{header_str}\r\n"
        f"Content-Length: {len(body)}\r\n"
        f"\r\n"
        f"{body}\n\n"
    )

def generate_ftp():
    files = ["data.bin", "todo.txt", "logo.png", "script.py"]
    return (
        f"150 Opening ASCII mode data connection.\r\n"
        f"-rw-r--r--   1 user     group      {random.randint(500,5000)} {get_timestamp()} {random.choice(files)}\r\n"
        f"226 Transfer complete.\r\n"
    )

def generate_smtp():
    return (
        f"MAIL FROM:<system@local>\r\n"
        f"250 2.1.0 Ok\r\n"
        f"RCPT TO:<admin@local>\r\n"
        f"DATA\r\n"
        f"Subject: Heartbeat Check {random.randint(1,100)}\r\n"
        f".\r\n"
    )

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"[+] Server running on port {PORT}")

        while True:
            conn, addr = s.accept()
            with conn:
                flag_index = random.randint(15, 35)
                for i in range(50):
                    if i == flag_index:
                        payload = generate_http(inject_flag=True)
                    else:
                        choice = random.choice(['HTTP', 'FTP', 'SMTP'])
                        if choice == 'HTTP': payload = generate_http()
                        elif choice == 'FTP': payload = generate_ftp()
                        else: payload = generate_smtp()
                    conn.sendall(payload.encode())
                    time.sleep(0.05)

if __name__ == "__main__":
    start_server()
