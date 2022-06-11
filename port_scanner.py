#!./venv/bin/python3
#simple port scanner
#added some pyfigment fancy stuff

import sys
import socket
import pyfiglet
import traceback


def probe_port(ip,port) :
	result = 1
	try: 
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		sock.settimeout(0.5) 
		r = sock.connect_ex((ip, port))   
		if r == 0: 
			result = r 
		sock.close() 
	except Exception as e: 
		traceback.print_exc()
		print(f"[X] {e}") 
	return result


if __name__ == '__main__':
	ascii_banner = pyfiglet.figlet_format("Port Scanner")
	print(ascii_banner)
	args = sys.argv

	if len(args) < 2 :
		print("Invalid number of arguments!!")
		print(f"[>] Usage : {args[0]} ip/host_to_scan [port(s)]")
		print("Port(s) must be , separated")
		print("If no ports provide, will scan all ports")
		sys.exit(1)

	target = socket.gethostbyname(args[1])
	open_ports = []

	try :
		ports = args[2].split(",")
	except :
		#traceback.print_exc()
		print("[!] Defaulting to ports 1 to 65534")
		ports = range(1,65535)

	try :
		for port in ports :
			#print(port)
			res = probe_port(target,port)
			if res == 0 :
				open_ports.append(port)
		lp = len(open_ports)
		if lp == 0:
			print("[x] All ports are closed!!")
		else :
			print(f"[>] Total {lp} ports are open and are listed below : ")
			sys.stdout.flush() 
			print(*sorted(open_ports))

	except KeyboardInterrupt :
		print("[!] KeyboardInterrupt detected")
		print("[!] Showing results from scanned results till now :")
		lp = len(open_ports)
		if lp == 0:
			print("[x] All ports are closed!!")
		else :
			print(f"[>] Total {lp} ports are open and are listed below : ")
			sys.stdout.flush() 
			print(*sorted(open_ports))
		sys.exit(0)

	except Exception as e:
		traceback.print_exc()
		print(f"[X] {e}")
		print("Exiting...")
		sys.exit(1)