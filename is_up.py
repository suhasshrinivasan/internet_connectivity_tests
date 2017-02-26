"""
Python script to checking Internet connection.
Possibly most optimum.
1. Does not do a dns resolution.
2. Relies on a stable IP, Google's Public DNS: 8.8.8.8
3. Port: (Open Port) 53
4. Service: domain (dns/tcp)
5. Does not rely on application layer such as HTTP
6. Does not rely on third party library.

Running instructions:
python is_up 

Author: Suhas Shrinivasan, DESE, IISc.
License: Open
"""

import socket

def is_up(host='8.8.8.8', port=53, timeout=3):

	try:
		socket.setdefaulttimeout(timeout)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		return True

	except: 
		return False

def main():
	print is_up()

if __name__ == '__main__':
	main()