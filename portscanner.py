from modules.clear import clear
import socket
import pyfiglet
from modules.colora import green, red, magenta
from modules.calctime import Calctime

banner = pyfiglet.figlet_format("PortScanner", font="big")

clear()

print(magenta('-')*60)
print(green(banner))

print(red('by Diogo S. Lourenco'))
print(magenta('-')*60)

ip = input("\nEnter the IP/URL target: ")
port_min = int(input('\nEnter the MIN number of ports to be scanned: '))
port_max = int(input('Enter the MAX number of ports to be scanned: '))

print('')
print(green('Scanning...'))
print('')

@Calctime
def scan():
    for port in range(port_min, port_max+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.4)
        r = s.connect_ex((ip, port))
        if r == 0:
            print(green(f'{port} OPEN'))
        else:
            print(red(f'{port} CLOSED'))
        s.close()

scan()
