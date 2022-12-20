#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
        n = 0           
        for m in range(x):
         try:
            print("{}".format(my_list[m], end="")
        except IndexError:
             break
        n += 1
      print("")
      return n
