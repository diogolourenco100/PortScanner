from modules.clear import clear
import socket
import pyfiglet
from modules.colora import green, red, magenta, yellow
from modules.calctime import Calctime
import threading

banner = pyfiglet.figlet_format("PortScanner", font="big")

clear()

print(magenta('-')*60)
print(green(banner))

print(red('by Diogo S. Lourenco'))
print(magenta('-')*60)
print(yellow('\nThis Script will scan from port 1 to port 3389, with a scan time of approximately 3 seconds.\n'))
ip = input("\nEnter the IP/URL target: ")

print(green('\nScanning...\n'))

open_ports = []
lock = threading.Lock()

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.05)
        r = s.connect_ex((ip, port))
        if r == 0:
            with lock:
                open_ports.append(port)
                print(green(f'{port} open/aberta'))
        s.close()
    except socket.error:
        pass

def thread_scan(ip, start_port, end_port, thread_count=100):
    def worker(port_range):
        for port in port_range:
            scan_port(ip, port)

    port_ranges = [range(start_port + i, end_port + 1, thread_count) for i in range(thread_count)]
    
    threads = []
    for port_range in port_ranges:
        thread = threading.Thread(target=worker, args=(port_range,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

@Calctime
def scan():
    thread_scan(ip, 1, 3389, thread_count=100)

scan()
