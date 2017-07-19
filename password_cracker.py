#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2015 AVELAZCX <aldo.alfonsox.velasco.meza@intel.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.	:

# Description	: Old school password cracker using python

from sys import platform as _platform

# Check the current operating system to import the correct version of crypt
if _platform in ["linux", "linux2", "darwin"]: # darwin is _platform name for Mac OS X
    import crypt # Import the module
elif _platform == "win32":
    # Windows
    try:
       import fcrypt # Try importing the fcrypt module
    except ImportError:
       print 'Please install fcrypt if you are on Windows'


def testPass(cryptPass):	  # Start the function
  salt = cryptPass[0:2]
  dictFile = open('dictionary.txt','r')	  # Open the dictionary file
  for word in dictFile.readlines():	  # Scan through the file
    word = word.strip('\n')
    cryptWord = crypt.crypt(word, salt)	  # Check for password in the file
    if (cryptWord == cryptPass):
      print "[+] Found Password: "+word+"\n"
      return
  print "[-] Password Not Found.\n"
  return


def main():
  passFile = open('passwords.txt')		  # Open the password file
  for line in passFile.readlines():	   # Read through the file
    if ":" in line:
      user = line.split(':')[0]
      cryptPass = line.split(':')[1].strip(' ') # Prepare the user name etc
      print "[*] Cracking Password For: " + user
      testPass(cryptPass)				# Call it to crack the users password

if __name__ == "__main__":
  main()
