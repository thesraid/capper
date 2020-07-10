#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
joriordan@att.com
"""


import argparse
import ast

##########################################################################################
"""
Get command line args from the user.
"""
def get_args():
    parser = argparse.ArgumentParser(
        description='Read in dictionary values from a file')

    parser.add_argument('-f', '--filepath',
                        required=True,
                        action='store',
                        help='Path to the file containing mac address pairs')


    args = parser.parse_args()

    return args

###########################################################################################

def main():

   args = get_args()
   filepath=args.filepath


   #print(filepath)

   with open(filepath, "r") as data:
      #print (data)
      dictionary = ast.literal_eval(data.read())

   #print (type(dictionary))
   #print (dictionary)


   olddata = ["oldwindowsmac", "oldlinuxmac", "oldgwmac", "oldkalimac", "someothermac"]

   for i in olddata:
      if i in dictionary:
        print (dictionary[i])

   '''
   for p in packets:
      if p.haslayer("IP"):
         if p[IP].src in dictionary:
            p[IP].src = dictionary[IP]
         if p[IP].dst in dictionary:
            p[IP].dst = dictionary[IP]
   '''
   #output = [dictionary[mac] for mac in olddata]
   #print (output)
   #print ' '.join(output)
   #print (olddata)
###########################################################################################

""" Start program """
if __name__ == "__main__":
    main()

