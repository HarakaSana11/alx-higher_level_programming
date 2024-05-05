#!/usr/bin/python3
"""
Module 0-read_file
contains function hat reads and prints from file
"""

def read_file(filename=""):
	"""Reads and prints text from file"""
	with open(filename, mode="r", encoding="utf=8") as f:
		print(f.read(), end"")
