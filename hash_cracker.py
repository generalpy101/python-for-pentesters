#!./venv/bin/python3

#simple hash cracker
#todo
#add hash identification
#add feature to add multiple hashes via files

import time
import hashlib
import sys
import pyfiglet
import traceback
from pathlib import Path

if __name__ == '__main__':
	start_time = time.time()
	ascii_banner = pyfiglet.figlet_format("Hash Cracker")
	print(ascii_banner)

	args = sys.argv
	if len(args) < 3 :
		print("Invalid number of arguments!!")
		print(f"[>] Usage : {args[0]} wordlist hash [algorithm]")
		print("Default algorithm is md5")
		sys.exit(1)

	wordlist = Path(args[1])
	hash_input = args[2]

	try :
		hash_type = args[3]

	except :
		print("[!] No hash type provided")
		print("[!] Defaulting to md5")
		hash_type = "md5"

	try : 
		if not wordlist.is_file() :
			raise FileNotFoundError("Path to wordlist is invalid")
		with open(wordlist,"r") as f :
			words = f.read().splitlines()
			for word in words :
				if hash_type == "md5" :
					calculated_hash = hashlib.md5(word.strip().encode()).hexdigest()
				elif hash_type == "sha256" :
					calculated_hash = hashlib.sha256(word.strip().encode()).hexdigest()
				else :
					raise ValueError("Invalid has type")
				if calculated_hash == hash_input :
					print(f"[>] Match found for word {word}")
					print(f"[>] {word} = {hash_input}")
					print(f"[!] Type : {hash_type}")
					break
			else :
				print(f"[x] No match found for {hash_input} in wordlist")

	except Exception as e:
		traceback.print_exc()
		print(f"[X] {e}")
		print("Exiting...")
		sys.exit(1)

	print(f"[!] Took {time.time() - start_time} seconds")