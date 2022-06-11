#!./venv/bin/python3
import requests
import os
import sys
from pathlib import Path

if __name__ == "__main__" :
	args = sys.argv
	if len(args) < 3 :
		print("Invalid number of arguments!!")
		print(f"[>] Usage : {args[0]} wordlist domain [protocol]")
		print("If no protocol provided, defaults to http")
		sys.exit(1)
	
	try :
		wordlist = Path(args[1])
		domain = args[2]
		try :
			protocol = args[3]
		except :
			protocol = "http"
		
		if not wordlist.is_file() :
			raise FileNotFoundError("Path to wordlist is invalid")
		
		with open(wordlist,"r") as f :
			words = f.read().splitlines()
			
			for word in words :
				url = f"{protocol}://{word}.{domain}"
				try :
					req = requests.get(url) 
				
				except requests.ConnectionError: 
					print(f"[x] Tried {url}, no subdomain found",end="\r")
					sys.stdout.flush()
					pass
				
				except Exception as e :
					print(f"[X] {e}")
					print("Exiting...")
					sys.exit(1)
				
				else : 
					print(f"\n[=] Subdomain found at {url}")

	except Exception as e:
		print(f"[X] {e}")
		print("Exiting...")
		sys.exit(1)
