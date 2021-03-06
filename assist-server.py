#!/usr/bin/env python3

import sys
import os
import argparse

from modules import security
from modules import connection


class Server:
	"""assist-server class"""
	pass


def main():
	if len(sys.argv) == 3:
		assist_server = connection.ServerConnection(sys.argv[1], sys.argv[2])
		assist_server.start_server()

if __name__ == "__main__":
	main()

