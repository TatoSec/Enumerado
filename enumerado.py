from time import sleep
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.panel import Panel
from rich.text import Text
from rich import print as printr
import time
import requests
import os
import sys
import logging
from rich.logging import RichHandler
import nmap
import random



def banner():
    logo = '''                                                                                     
@@@@@@@@  @@@  @@@  @@@  @@@  @@@@@@@@@@   @@@@@@@@  @@@@@@@    @@@@@@   @@@@@@@    @@@@@@   
@@@@@@@@  @@@@ @@@  @@@  @@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  
@@!       @@!@!@@@  @@!  @@@  @@! @@! @@!  @@!       @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  
!@!       !@!!@!@!  !@!  @!@  !@! !@! !@!  !@!       !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  
@!!!:!    @!@ !!@!  @!@  !@!  @!! !!@ @!@  @!!!:!    @!@!!@!   @!@!@!@!  @!@  !@!  @!@  !@!  
!!!!!:    !@!  !!!  !@!  !!!  !@!   ! !@!  !!!!!:    !!@!@!    !!!@!!!!  !@!  !!!  !@!  !!!  
!!:       !!:  !!!  !!:  !!!  !!:     !!:  !!:       !!: :!!   !!:  !!!  !!:  !!!  !!:  !!!  
:!:       :!:  !:!  :!:  !:!  :!:     :!:  :!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  
 :: ::::   ::   ::  ::::: ::  :::     ::    :: ::::  ::   :::  ::   :::   :::: ::  ::::: ::  
: :: ::   ::    :    : :  :    :      :    : :: ::    :   : :   :   : :  :: :  :    : :  :                                                                                  
            '''
    colors = ["[red3]", "[cyan2]", "[steel_blue1]", "[chartreuse1]", "[magenta]", "[salmon1]"]
    color = random.choice(colors)
    printr(color + logo)
    printr("[bold white]" + "━" * 93 + "\n")


def hacker_text(text, leading_spaces = 0):

	text_chars = list(text)
	current, mutated = '', ''

	for i in range(len(text)):
		
		original = text_chars[i]
		current += original
		mutated += f'\033[1;38;5;82m{text_chars[i].upper()}\033[0m'
		print(f'\r{" " * leading_spaces}{mutated}', end = '')
		sleep(0.02)
		print(f'\r{" " * leading_spaces}{current}', end = '')
		mutated = current

	print(f'\r{" " * leading_spaces}{text}\n')	

def is_admin():
    """
    Returns True if the script is running with admin/root privileges, False otherwise.
    """
    if os.name == 'nt':  # Windows
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            return False
    else:  # Unix/Linux/Mac
        return os.geteuid() == 0

def ls_simple(path):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        mtime = time.strftime('%Y-%m-%d %H:%M', time.localtime(os.path.getmtime(full_path)))
        print(f"{mtime} {entry}")


def port_scan():
	print("")
def service_scan():
	print("")

def main():
	banner()
	ip = requests.get('https://checkip.amazonaws.com').text.strip()
	console = Console()
	logging.basicConfig(level="INFO", handlers=[RichHandler()])
	log = logging.getLogger("REASON")	
	def enum_list():
		menu_text = """
		[bold cyan]1.[/] Network Port Scan (Nmap)
		[bold cyan]2.[/] Network Service Scan (Nmap)
		[bold cyan]3.[/] SMB Share Listing (SMBClient)
		[bold cyan]4.[/] Exit
		"""

		console.print(Panel(menu_text, title="[bold green]Main Menu[/bold green]", border_style="cyan"))
				
	def show_help(console):
		table = Table(title="Enumerado Help Menu", header_style="bold cyan")

		table.add_column("Command", style="yellow", no_wrap=True)
		table.add_column("Description", style="white")

		table.add_row("help / h", "Show this help menu")
		table.add_row("pwd / cwd", "Show current working directory")
		table.add_row("ls / dir", "List files in the current directory")
		table.add_row("1 / one", "Full Network Port Scan (Nmap)")
		table.add_row("2 / two", "Network Service Scan (Nmap)")
		table.add_row("3 / three", "SMB Share Enumeration (SMBClient)")
		table.add_row("clear", "Clear the screen")
		table.add_row("exit / quit", "Exit the application")
		table.add_row("banner", "Display Banner")

		console.print(table)

	enum_list()
	while True:
		respone = console.input(f"[bold magenta]enum@{ip}[blink] > [/blink][/bold magenta]")
		one_lang_tup = ("1", "one", "One", ".1")
		two_lang_tup = ("2", "two", "Two", ".2")
		three_lang_tup = ("3", "three", "Three", ".3")
		exit_lang_tup = ("4", "quit", "Quit", "exit", "Exit", "leave", "kill", "Kill", "stop", "shutdown")
		if respone == "pwd" or respone == "cwd":
			getdir = os.getcwd()
			hacker_text(getdir)
		elif respone == "ls" or respone == "dir":
			ls_simple(path='.')
		elif respone in one_lang_tup:
			if not is_admin():
				log.error("[bold red3 blink]This command requires sudo/admin privileges! [/]", extra={"markup": True})
			else:
				target_ip = console.input("[bold green]Enter Target IP Address[blink]:[/blink] [/bold green]")
				scanner = nmap.PortScanner()
				options = "-p- --open -sS -sU -O -T4 -v --min-rate 5000"
				scanner.scan(target_ip, arguments=options)

				# Create table
				table = Table(title=f"\nScan Results for {target_ip}")

				table.add_column("Host", style="cyan", no_wrap=True)
				table.add_column("Protocol", style="magenta")
				table.add_column("Port", style="yellow")
				table.add_column("State", style="green")

				# Fill table with scan data
				for host in scanner.all_hosts():
					for proto in scanner[host].all_protocols():
						ports = scanner[host][proto].keys()
						for port in ports:
							table.add_row(
								host,
								proto,
								str(port),
								scanner[host][proto][port]['state']
							)

				console.print(table)
				additional_scan = console.input("[bold blue]Do you wish to run a service scan on the ports discovered? [blink white bold](Y[yes]/N[no]):[/] ")
				if additional_scan == "yes" or additional_scan == "Yes" or additional_scan == "Y" or additional_scan == "y":
					hacker_text("Amazing (ADD LOGIC ASAP)")
				else:
					continue

		elif respone == "clear" or respone == "Clear":
			console.clear()
		elif respone == "help" or respone == "h":
			show_help(console)
			continue
		elif respone == "banner":
			banner()
		elif respone in exit_lang_tup:
			log.info("[bold green blink]Exited Program Successfully![/]", extra={"markup": True})
			quit()
		

if __name__ == '__main__':
	main()
	