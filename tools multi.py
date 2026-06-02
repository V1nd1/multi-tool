
import socket
import subprocess
import sys
import hashlib
import base64
import platform
import getpass
import random
import string
import os
import time
import urllib.parse
import urllib.request
import re
import uuid
from datetime import datetime

class Colors:
    HEADER = '\033[95m'
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def safe_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Interrupted{Colors.RESET}")
        return ""

def loading_animation(text):
    print(f"{Colors.DIM}{text}", end="", flush=True)
    for _ in range(3):
        time.sleep(0.2)
        print(".", end="", flush=True)
    print(f"{Colors.RESET}")

def banner():
    banner_art = f"""
{Colors.PINK}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                      ║
║      ██╗   ██╗██╗██╗   ██╗██████╗ ██╗                                                ║
║      ██║   ██║██║██║   ██║██╔══██╗██║                                                ║
║      ██║   ██║██║██║   ██║██║  ██║██║                                                ║
║      ╚██╗ ██╔╝██║██║   ██║██║  ██║██║                                                ║
║       ╚████╔╝ ██║╚██████╔╝██████╔╝███████╗                                           ║
║        ╚═══╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝                                           ║
║                                                                                      ║
║                    ╔══════════════════════════════════════════════╗                  ║
║                    ║    ✦  ADVANCED MULTI-TOOL SUITE  ✦          ║                  ║
║                    ║      {Colors.CYAN}Version 5.1 | Vi1nd1 | 30+ Tools{Colors.PINK}      ║                  ║
║                    ╚══════════════════════════════════════════════╝                  ║
║                                                                                      ║
║                      {Colors.DIM}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.PINK}                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}
"""
    print(banner_art)

def print_menu():
    menu = f"""
{Colors.BOLD}{Colors.CYAN}┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                          🔥                                          │
│                              {Colors.PINK}◈  V I 1 N D 1   M E N U  ◈{Colors.CYAN}                              │
│                                          🔥                                          │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│   {Colors.GREEN}01{Colors.RESET}  🔍  Port Scanner              {Colors.GREEN}16{Colors.RESET}  🔑  Random Key Generator{Colors.CYAN}               │
│   {Colors.GREEN}02{Colors.RESET}  🔐  Password Generator        {Colors.GREEN}17{Colors.RESET}  📧  Email Validator{Colors.CYAN}                    │
│   {Colors.GREEN}03{Colors.RESET}  💻  System Information        {Colors.GREEN}18{Colors.RESET}  🌍  Public IP Checker{Colors.CYAN}                 │
│   {Colors.GREEN}04{Colors.RESET}  📁  File Hasher               {Colors.GREEN}19{Colors.RESET}  📅  Timer/Stopwatch{Colors.CYAN}                   │
│   {Colors.GREEN}05{Colors.RESET}  🏓  Ping Tool                 {Colors.GREEN}20{Colors.RESET}  🔢  Number Base Converter{Colors.CYAN}             │
│   {Colors.GREEN}06{Colors.RESET}  🔄  Base64 Tool               {Colors.GREEN}21{Colors.RESET}  📝  Text Counter{Colors.CYAN}                      │
│   {Colors.GREEN}07{Colors.RESET}  🌐  IP Lookup                 {Colors.GREEN}22{Colors.RESET}  🧮  Subnet Calculator{Colors.CYAN}                 │
│   {Colors.GREEN}08{Colors.RESET}  🌍  Web Server                {Colors.GREEN}23{Colors.RESET}  🎲  MAC Generator{Colors.CYAN}                     │
│   {Colors.GREEN}09{Colors.RESET}  🖧  MAC Changer (Info)        {Colors.GREEN}24{Colors.RESET}  🔗  DNS Lookup{Colors.CYAN}                        │
│   {Colors.GREEN}10{Colors.RESET}  🔗  URL Encoder/Decoder       {Colors.GREEN}25{Colors.RESET}  📋  HTTP Header Checker{Colors.CYAN}               │
│   {Colors.GREEN}11{Colors.RESET}  🧹  Temp Cleaner (Info)       {Colors.GREEN}26{Colors.RESET}  📸  Banner Grabber{Colors.CYAN}                    │
│   {Colors.GREEN}12{Colors.RESET}  📊  Network Statistics        {Colors.GREEN}27{Colors.RESET}  🔐  ROT13 / Caesar{Colors.CYAN}                    │
│   {Colors.GREEN}13{Colors.RESET}  🔑  Hash Checker              {Colors.GREEN}28{Colors.RESET}  📊  Entropy Calculator{Colors.CYAN}                │
│   {Colors.GREEN}14{Colors.RESET}  📡  Port List (Known)         {Colors.GREEN}29{Colors.RESET}  🖧  MAC OUI Lookup{Colors.CYAN}                    │
│   {Colors.GREEN}15{Colors.RESET}  🔎  Whois (Simulated)         {Colors.GREEN}30{Colors.RESET}  📄  String Extractor{Colors.CYAN}                  │
│                                                                                     │
│   {Colors.GREEN}00{Colors.RESET}  🚪  Exit                                                                          │
│                                                                                     │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                         {Colors.DIM}⚡  precision  ⚡  speed  ⚡  elegance  ⚡{Colors.CYAN}                         │
└─────────────────────────────────────────────────────────────────────────────────────┘{Colors.RESET}
"""
    print(menu)
def port_scanner():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  PORT SCANNER  ◈{Colors.RESET}\n")
    target = safe_input(f"{Colors.CYAN}📡  Target IP {Colors.DIM}›{Colors.RESET} ")
    if not target:
        return
    ports = [21, 22, 23, 80, 443, 445, 8080, 8443]
    loading_animation(f"\n{Colors.BLUE}Scanning {target}")
    print()
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"  {Colors.GREEN}●{Colors.RESET} Port {Colors.BOLD}{port}{Colors.RESET} → {Colors.GREEN}OPEN{Colors.RESET}")
            else:
                print(f"  {Colors.DIM}○{Colors.RESET} Port {port} → closed")
            sock.close()
        except:
            print(f"  {Colors.RED}✖{Colors.RESET} Port {port} → error")

def password_generator():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  PASSWORD GENERATOR  ◈{Colors.RESET}\n")
    try:
        length = int(safe_input(f"{Colors.CYAN}📏  Length {Colors.DIM}›{Colors.RESET} "))
        if length < 1:
            length = 12
    except:
        length = 12
    include_special = safe_input(f"{Colors.CYAN}✨  Include special chars? (y/n) {Colors.DIM}›{Colors.RESET} ").lower() == 'y'
    chars = string.ascii_letters + string.digits
    if include_special:
        chars += "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"\n  {Colors.GREEN}★{Colors.RESET}  Generated Password:")
    print(f"\n  {Colors.BOLD}{Colors.CYAN}{password}{Colors.RESET}\n")

def system_info():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  SYSTEM INFORMATION  ◈{Colors.RESET}\n")
    info = [
        ("🖥️  System", f"{platform.system()} {platform.release()}"),
        ("🏷️  Node", platform.node()),
        ("👤  User", getpass.getuser()),
        ("⚙️  Architecture", platform.machine()),
        ("🐍  Python", platform.python_version()),
        ("📁  OS", os.name),
    ]
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        info.append(("🌐  Local IP", ip))
    except:
        info.append(("🌐  Local IP", "Could not determine"))
    
    for label, value in info:
        print(f"  {Colors.CYAN}{label}{Colors.RESET} {Colors.DIM}→{Colors.RESET} {value}")

def file_hasher():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  FILE HASHER  ◈{Colors.RESET}\n")
    filepath = safe_input(f"{Colors.CYAN}📂  File path {Colors.DIM}›{Colors.RESET} ")
    if not filepath:
        return
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
            md5 = hashlib.md5(data).hexdigest()
            sha1 = hashlib.sha1(data).hexdigest()
            sha256 = hashlib.sha256(data).hexdigest()
        print(f"\n  {Colors.GREEN}●{Colors.RESET}  MD5    → {md5}")
        print(f"  {Colors.GREEN}●{Colors.RESET}  SHA1   → {sha1}")
        print(f"  {Colors.GREEN}●{Colors.RESET}  SHA256 → {sha256}")
    except:
        print(f"\n  {Colors.RED}✖{Colors.RESET}  File not found or unreadable")

def ping_tool():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  PING TOOL  ◈{Colors.RESET}\n")
    target = safe_input(f"{Colors.CYAN}🎯  Target {Colors.DIM}›{Colors.RESET} ")
    if not target:
        return
    param = "-n" if platform.system().lower() == "windows" else "-c"
    loading_animation(f"{Colors.BLUE}Pinging {target}")
    try:
        response = subprocess.run(["ping", param, "2", target], capture_output=True, text=True, timeout=10)
        print(f"\n  {Colors.GREEN}●{Colors.RESET}  Response:\n")
        for line in response.stdout.split('\n')[:5]:
            if line.strip():
                print(f"    {line[:80]}")
    except:
        print(f"\n  {Colors.RED}✖  Ping failed{Colors.RESET}")

def base64_tool():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  BASE64 TOOL  ◈{Colors.RESET}\n")
    print(f"  {Colors.CYAN}1{Colors.RESET}  Encode")
    print(f"  {Colors.CYAN}2{Colors.RESET}  Decode")
    choice = safe_input(f"\n{Colors.CYAN}⚡  Choice {Colors.DIM}›{Colors.RESET} ")
    text = safe_input(f"{Colors.CYAN}📝  Text {Colors.DIM}›{Colors.RESET} ")
    if choice == "1":
        encoded = base64.b64encode(text.encode()).decode()
        print(f"\n  {Colors.GREEN}★{Colors.RESET}  Encoded:\n  {encoded}")
    elif choice == "2":
        try:
            decoded = base64.b64decode(text).decode()
            print(f"\n  {Colors.GREEN}★{Colors.RESET}  Decoded:\n  {decoded}")
        except:
            print(f"\n  {Colors.RED}✖  Invalid Base64{Colors.RESET}")

def ip_lookup():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  IP LOOKUP  ◈{Colors.RESET}\n")
    domain = safe_input(f"{Colors.CYAN}🔍  Domain or IP {Colors.DIM}›{Colors.RESET} ")
    if not domain:
        return
    try:
        ip = socket.gethostbyname(domain)
        print(f"\n  {Colors.GREEN}●{Colors.RESET}  IP Address → {ip}")
        try:
            host = socket.gethostbyaddr(ip)[0]
            print(f"  {Colors.GREEN}●{Colors.RESET}  Hostname  → {host}")
        except:
            pass
    except:
        print(f"\n  {Colors.RED}✖  Could not resolve{Colors.RESET}")

def simple_web_server():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  WEB SERVER  ◈{Colors.RESET}\n")
    try:
        port = int(safe_input(f"{Colors.CYAN}🔌  Port {Colors.DIM}›{Colors.RESET} "))
    except:
        port = 8000
    print(f"\n  {Colors.GREEN}●{Colors.RESET}  Server started on port {port}")
    print(f"  {Colors.DIM}Press Ctrl+C to stop{Colors.RESET}\n")
    try:
        subprocess.run([sys.executable, "-m", "http.server", str(port)])
    except KeyboardInterrupt:
        print(f"\n  {Colors.YELLOW}⚠  Server stopped{Colors.RESET}")

def change_mac():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  MAC CHANGER  ◈{Colors.RESET}\n")
    print(f"  {Colors.YELLOW}⚠  Requires root/admin privileges{Colors.RESET}\n")
    interface = safe_input(f"{Colors.CYAN}🔌  Interface (eth0, wlan0) {Colors.DIM}›{Colors.RESET} ")
    if not interface:
        return
    print(f"\n  {Colors.DIM}Commands:{Colors.RESET}")
    print(f"    sudo ip link set {interface} down")
    print(f"    sudo ip link set {interface} address 00:11:22:33:44:55")
    print(f"    sudo ip link set {interface} up")

def url_encoder():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  URL ENCODER/DECODER  ◈{Colors.RESET}\n")
    print(f"  {Colors.CYAN}1{Colors.RESET}  Encode")
    print(f"  {Colors.CYAN}2{Colors.RESET}  Decode")
    choice = safe_input(f"\n{Colors.CYAN}⚡  Choice {Colors.DIM}›{Colors.RESET} ")
    text = safe_input(f"{Colors.CYAN}📝  URL {Colors.DIM}›{Colors.RESET} ")
    if choice == "1":
        encoded = urllib.parse.quote(text)
        print(f"\n  {Colors.GREEN}★{Colors.RESET}  Encoded:\n  {encoded}")
    elif choice == "2":
        decoded = urllib.parse.unquote(text)
        print(f"\n  {Colors.GREEN}★{Colors.RESET}  Decoded:\n  {decoded}")

def temp_cleaner():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  TEMP CLEANER (INFO)  ◈{Colors.RESET}\n")
    if platform.system().lower() == "windows":
        temp_path = os.environ.get("TEMP", "C:\\Windows\\Temp")
    else:
        temp_path = "/tmp"
    print(f"  {Colors.CYAN}📁  Temp path:{Colors.RESET} {temp_path}")
    print(f"\n  {Colors.YELLOW}⚠  Manual cleanup: rm -rf {temp_path}/* (Linux) or del %TEMP%\\* (Windows){Colors.RESET}")

def network_stats():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  NETWORK STATISTICS  ◈{Colors.RESET}\n")
    try:
        response = subprocess.run(["netstat", "-an"], capture_output=True, text=True, timeout=10)
        lines = response.stdout.split('\n')
        established = 0
        listening = 0
        for line in lines[:30]:
            if "ESTABLISHED" in line:
                established += 1
            elif "LISTEN" in line or "LISTENING" in line:
                listening += 1
        print(f"  {Colors.GREEN}●{Colors.RESET}  Established connections: {established}")
        print(f"  {Colors.GREEN}●{Colors.RESET}  Listening ports: {listening}")
        print(f"\n  {Colors.DIM}(First 30 lines displayed){Colors.RESET}")
    except:
        print(f"  {Colors.RED}✖  Could not get network stats{Colors.RESET}")

def random_key_generator():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  RANDOM KEY GENERATOR  ◈{Colors.RESET}\n")
    print(f"  {Colors.CYAN}1{Colors.RESET}  API Key (32 chars)")
    print(f"  {Colors.CYAN}2{Colors.RESET}  Secret Key (16 chars)")
    print(f"  {Colors.CYAN}3{Colors.RESET}  UUID")
    choice = safe_input(f"\n{Colors.CYAN}⚡  Choice {Colors.DIM}›{Colors.RESET} ")
    if choice == "1":
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        print(f"\n  {Colors.GREEN}★{Colors.RESET}  API Key:\n  {key}")
    elif choice == "2":
        key = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%", k=16))
        print(f"\n  {Colors.GREEN}★{Colors.RESET}  Secret Key:\n  {key}")
    elif choice == "3":
        key = str(uuid.uuid4())
        print(f"\n  {Colors.GREEN}★{Colors.RESET}  UUID:\n  {key}")

def email_validator():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  EMAIL VALIDATOR (SYNTAX)  ◈{Colors.RESET}\n")
    email = safe_input(f"{Colors.CYAN}📧  Email address {Colors.DIM}›{Colors.RESET} ")
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print(f"\n  {Colors.GREEN}✅  Valid syntax{Colors.RESET}")
    else:
        print(f"\n  {Colors.RED}❌  Invalid syntax{Colors.RESET}")

def public_ip():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  PUBLIC IP CHECKER  ◈{Colors.RESET}\n")
    loading_animation(f"{Colors.BLUE}Fetching public IP")
    try:
        req = urllib.request.urlopen("https://api.ipify.org", timeout=5)
        ip = req.read().decode()
        print(f"\n  {Colors.GREEN}🌍  Public IP:{Colors.RESET} {ip}")
    except:
        print(f"\n  {Colors.RED}✖  Could not fetch public IP{Colors.RESET}")

def timer_stopwatch():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  TIMER  ◈{Colors.RESET}\n")
    print(f"  {Colors.CYAN}1{Colors.RESET}  Countdown Timer")
    print(f"  {Colors.CYAN}2{Colors.RESET}  Stopwatch")
    choice = safe_input(f"\n{Colors.CYAN}⚡  Choice {Colors.DIM}›{Colors.RESET} ")
    if choice == "1":
        try:
            seconds = int(safe_input(f"{Colors.CYAN}⏱️  Seconds {Colors.DIM}›{Colors.RESET} "))
        except:
            seconds = 5
        print(f"\n  {Colors.GREEN}Timer started{Colors.RESET}")
        for i in range(seconds, 0, -1):
            print(f"  {i} seconds remaining", end="\r")
            time.sleep(1)
        print(f"\n  {Colors.GREEN}✅  Time's up!{Colors.RESET}")
    elif choice == "2":
        safe_input(f"\n  {Colors.CYAN}Press Enter to start stopwatch{Colors.RESET}")
        start = time.time()
        safe_input(f"  {Colors.CYAN}Press Enter to stop{Colors.RESET}")
        elapsed = time.time() - start
        print(f"\n  {Colors.GREEN}⏱️  Elapsed: {elapsed:.2f} seconds{Colors.RESET}")

def number_base_converter():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  NUMBER BASE CONVERTER  ◈{Colors.RESET}\n")
    number = safe_input(f"{Colors.CYAN}🔢  Number {Colors.DIM}›{Colors.RESET} ")
    try:
        num = int(number)
        print(f"\n  {Colors.GREEN}●{Colors.RESET}  Binary:  {bin(num)}")
        print(f"  {Colors.GREEN}●{Colors.RESET}  Octal:   {oct(num)}")
        print(f"  {Colors.GREEN}●{Colors.RESET}  Decimal: {num}")
        print(f"  {Colors.GREEN}●{Colors.RESET}  Hex:     {hex(num)}")
    except:
        print(f"\n  {Colors.RED}✖  Invalid number{Colors.RESET}")

def text_counter():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  TEXT COUNTER  ◈{Colors.RESET}\n")
    text = safe_input(f"{Colors.CYAN}📝  Enter text {Colors.DIM}›{Colors.RESET} ")
    chars = len(text)
    words = len(text.split())
    lines = len(text.split('\n'))
    print(f"\n  {Colors.GREEN}●{Colors.RESET}  Characters: {chars}")
    print(f"  {Colors.GREEN}●{Colors.RESET}  Words:      {words}")
    print(f"  {Colors.GREEN}●{Colors.RESET}  Lines:      {lines}")

def subnet_calculator():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  SUBNET CALCULATOR  ◈{Colors.RESET}\n")
    ip = safe_input(f"{Colors.CYAN}🌐  IP Address {Colors.DIM}›{Colors.RESET} ")
    try:
        cidr = int(safe_input(f"{Colors.CYAN}🔢  CIDR (0-32) {Colors.DIM}›{Colors.RESET} "))
        mask_int = (0xffffffff >> (32 - cidr)) << (32 - cidr)
        mask = f"{(mask_int >> 24) & 0xff}.{(mask_int >> 16) & 0xff}.{(mask_int >> 8) & 0xff}.{mask_int & 0xff}"
        print(f"\n  {Colors.GREEN}●{Colors.RESET}  Subnet Mask: {mask}")
        print(f"  {Colors.GREEN}●{Colors.RESET}  CIDR: /{cidr}")
    except:
        print(f"\n  {Colors.RED}✖  Invalid input{Colors.RESET}")

def mac_generator():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  MAC ADDRESS GENERATOR  ◈{Colors.RESET}\n")
    mac = ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])
    print(f"\n  {Colors.GREEN}★{Colors.RESET}  Random MAC:\n  {mac}")

def dns_lookup():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  DNS LOOKUP  ◈{Colors.RESET}\n")
    domain = safe_input(f"{Colors.CYAN}🔍  Domain {Colors.DIM}›{Colors.RESET} ")
    if not domain:
        return
    try:
        ip = socket.gethostbyname(domain)
        print(f"\n  {Colors.GREEN}●{Colors.RESET}  A Record: {ip}")
    except:
        print(f"\n  {Colors.RED}✖  Could not resolve{Colors.RESET}")

def http_headers():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  HTTP HEADER CHECKER  ◈{Colors.RESET}\n")
    url = safe_input(f"{Colors.CYAN}🌐  URL (with http://) {Colors.DIM}›{Colors.RESET} ")
    if not url:
        return
    try:
        req = urllib.request.urlopen(url, timeout=5)
        headers = req.headers
        print(f"\n  {Colors.GREEN}●{Colors.RESET}  Headers:")
        for key, value in list(headers.items())[:10]:
            print(f"    {key}: {value[:60]}")
    except:
        print(f"\n  {Colors.RED}✖  Could not fetch headers{Colors.RESET}")

def banner_grabber():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  BANNER GRABBER  ◈{Colors.RESET}\n")
    target = safe_input(f"{Colors.CYAN}📡  Target IP {Colors.DIM}›{Colors.RESET} ")
    try:
        port = int(safe_input(f"{Colors.CYAN}🔌  Port {Colors.DIM}›{Colors.RESET} "))
    except:
        return
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((target, port))
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = sock.recv(1024).decode()
        print(f"\n  {Colors.GREEN}●{Colors.RESET}  Banner:\n  {banner[:200]}")
        sock.close()
    except:
        print(f"\n  {Colors.RED}✖  Could not grab banner{Colors.RESET}")

def rot13_caesar():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  ROT13 / CAESAR  ◈{Colors.RESET}\n")
    text = safe_input(f"{Colors.CYAN}📝  Text {Colors.DIM}›{Colors.RESET} ")
    encoded = ''.join(chr((ord(c) - 97 + 13) % 26 + 97) if c.islower() else chr((ord(c) - 65 + 13) % 26 + 65) if c.isupper() else c for c in text)
    print(f"\n  {Colors.GREEN}★{Colors.RESET}  ROT13:\n  {encoded}")

def entropy_calculator():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  ENTROPY CALCULATOR  ◈{Colors.RESET}\n")
    text = safe_input(f"{Colors.CYAN}📝  Password/Text {Colors.DIM}›{Colors.RESET} ")
    unique = len(set(text))
    entropy = len(text) * (unique.bit_length() if unique > 0 else 0)
    print(f"\n  {Colors.GREEN}●{Colors.RESET}  Length: {len(text)}")
    print(f"  {Colors.GREEN}●{Colors.RESET}  Unique chars: {unique}")
    print(f"  {Colors.GREEN}●{Colors.RESET}  Entropy (bits): ~{entropy}")

def mac_oui_lookup():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  MAC OUI LOOKUP  ◈{Colors.RESET}\n")
    mac = safe_input(f"{Colors.CYAN}🖧  MAC Address {Colors.DIM}›{Colors.RESET} ")
    oui = mac[:8].upper() if len(mac) >= 8 else mac.upper()
    print(f"\n  {Colors.GREEN}●{Colors.RESET}  OUI: {oui}")
    print(f"  {Colors.DIM}Full database offline. Use online lookup for manufacturer.{Colors.RESET}")

def string_extractor():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  STRING EXTRACTOR  ◈{Colors.RESET}\n")
    filepath = safe_input(f"{Colors.CYAN}📂  Binary file path {Colors.DIM}›{Colors.RESET} ")
    if not filepath:
        return
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
        strings = re.findall(b'[\\x20-\\x7E]{4,}', data)
        print(f"\n  {Colors.GREEN}●{Colors.RESET}  Found strings:")
        for s in strings[:10]:
            try:
                print(f"    {s.decode()}")
            except:
                print(f"    {s}")
        if len(strings) > 10:
            print(f"    ... and {len(strings)-10} more")
    except:
        print(f"\n  {Colors.RED}✖  Could not read file{Colors.RESET}")

def port_list():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  KNOWN PORTS  ◈{Colors.RESET}\n")
    known_ports = {
        20: "FTP Data", 21: "FTP Control", 22: "SSH", 23: "Telnet",
        25: "SMTP", 53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
        443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
        8080: "HTTP-Alt", 8443: "HTTPS-Alt"
    }
    for port, service in list(known_ports.items())[:15]:
        print(f"  {Colors.GREEN}{port}{Colors.RESET} → {service}")

def hash_checker():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  HASH CHECKER  ◈{Colors.RESET}\n")
    hash_input = safe_input(f"{Colors.CYAN}🔑  Hash to check {Colors.DIM}›{Colors.RESET} ")
    test_string = safe_input(f"{Colors.CYAN}📝  Test string {Colors.DIM}›{Colors.RESET} ")
    if not hash_input or not test_string:
        return
    test_hash = hashlib.md5(test_string.encode()).hexdigest()
    if hash_input.lower() == test_hash:
        print(f"\n  {Colors.GREEN}✅  Hash matches!{Colors.RESET}")
    else:
        print(f"\n  {Colors.RED}❌  No match{Colors.RESET}")

def whois_sim():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.PINK}◈  WHOIS (SIMULATED)  ◈{Colors.RESET}\n")
    domain = safe_input(f"{Colors.CYAN}🔍  Domain {Colors.DIM}›{Colors.RESET} ")
    if not domain:
        return
    print(f"\n  {Colors.GREEN}●{Colors.RESET}  Domain: {domain}")
    print(f"  {Colors.GREEN}●{Colors.RESET}  Registrar: Simulated Data")
    print(f"  {Colors.GREEN}●{Colors.RESET}  Creation Date: 2020-01-01")
    print(f"  {Colors.DIM}Full whois requires internet connection and whois module{Colors.RESET}")

def main():
    while True:
        try:
            clear_screen()
            banner()
            print_menu()
            choice = safe_input(f"\n{Colors.BOLD}{Colors.PINK}⚡  SELECT TOOL {Colors.DIM}›{Colors.RESET} ")
            
            tools = {
                "01": port_scanner, "1": port_scanner,
                "02": password_generator, "2": password_generator,
                "03": system_info, "3": system_info,
                "04": file_hasher, "4": file_hasher,
                "05": ping_tool, "5": ping_tool,
                "06": base64_tool, "6": base64_tool,
                "07": ip_lookup, "7": ip_lookup,
                "08": simple_web_server, "8": simple_web_server,
                "09": change_mac, "9": change_mac,
                "10": url_encoder,
                "11": temp_cleaner,
                "12": network_stats,
                "13": random_key_generator,
                "14": email_validator,
                "15": public_ip,
                "16": timer_stopwatch,
                "17": number_base_converter,
                "18": text_counter,
                "19": subnet_calculator,
                "20": mac_generator,
                "21": dns_lookup,
                "22": http_headers,
                "23": banner_grabber,
                "24": rot13_caesar,
                "25": entropy_calculator,
                "26": mac_oui_lookup,
                "27": string_extractor,
                "28": port_list,
                "29": hash_checker,
                "30": whois_sim,
                "00": None, "0": None
            }
            
            if choice in tools:
                if choice in ["00", "0"]:
                    clear_screen()
                    print(f"\n  {Colors.BOLD}{Colors.PINK}✦  Vi1nd1 says goodbye  ✦{Colors.RESET}\n")
                    print(f"  {Colors.DIM}Precision. Speed. Elegance.{Colors.RESET}\n")
                    break
                elif tools[choice]:
                    tools[choice]()
            else:
                print(f"\n  {Colors.RED}✖  Invalid choice{Colors.RESET}")
            
            safe_input(f"\n{Colors.DIM}  Press Enter to continue...{Colors.RESET}")
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Interrupted{Colors.RESET}")
            break

if __name__ == "__main__":
    main()