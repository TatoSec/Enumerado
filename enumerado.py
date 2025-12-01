from time import sleep
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.panel import Panel
from rich.markdown import Markdown
from rich.text import Text
from rich import print as printr
import time
import requests




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
    printr("[bold magenta]" + logo)
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


def main():
	banner()
	ip = requests.get('https://checkip.amazonaws.com').text.strip()
	console = Console()
	console.print(Panel(Text("Enumeration Menu", style="bold yellow"), expand=False))
	time.sleep(0.1)
	hacker_text("1. Network Port Scan (Nmap)")
	hacker_text("2. Network Service Scan (Nmap)")
	hacker_text("3. SMB Share Finder (SMBClient)")

	console.input(f"[bold magenta]enumerador@{ip}[blink] >[/blink][/bold magenta]")

if __name__ == '__main__':
	main()
	