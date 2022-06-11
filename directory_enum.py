#!./venv/bin/python3

import requests
import sys
from pathlib import Path
import traceback


if __name__ == '__main__':
	args = sys.argv
	if len(args) < 3 :
		print("Invalid number of arguments!!")
		print(f"[>] Usage : f{args[0]} wordlist target [extensions] [protocol]")
		print("Extensions are to be separated by ,")
		print("Default extension is html and default protocol is http")
		sys.exit(1)

	wordlist = Path(args[1])
	domain = args[2]

	try :
		extensions = args[3].split(",")
	except :
		extensions = ["html"]

	try :
		protocol = args[4]
	except :
		protocol = "http"

	try :
		if not wordlist.is_file() :
			raise FileNotFoundError("Path to wordlist is invalid")
		with open(wordlist,"r") as f :
			words = f.read().splitlines()
			for word in words :
				for extension in extensions :
					url = f"{protocol}://{domain}/{word}.{extension}"
					#print(url)
					try :
						req = requests.get(url)
						if req.status_code == 404 :
							print(f"[x] Tried {url}, no directory found",end="\r")
							sys.stdout.flush()
						else :
							print(f"\n[>] Valid directory found at {url}")
					except Exception as e:
						print(f"[x] {e}")
	
	except Exception as e:
		traceback.print_exc()
		print(f"[X] {e}")
		print("Exiting...")
		sys.exit(1)