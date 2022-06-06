t.9
def zero_sum(num):
 z = 0
 for i in num:
  z += i
  if z == 0 :
   return True
  elif z!= 0 :
   return False
  else:
   return True
  num =(4,7,9,10,-1)
  x = zero_sum(num)
  print(x)
  
  t.10:
   because it permits access based on a key
   
   t.11:
    d = {}
    
   t.12:
    d['Fred'] = 44
    
    t.13:
  python KeyError exception is what is raised when you try to access a key that isn't in a dictionary
     
     t.14:
      must be a valid key in dictionary , or the program will raise an exception. A valid key is a key that is present in the dictionary. We see the interpreter’s reaction when we attempt to use an invalid key: the interpreter an generates KeyError exception.
      
     t.15:
     immutable
     
     t.16:
      (a){3: 0, 5: 1, 10: 1, 8: 2, 15: 4}
      (b) 3 5 10 8 15
      (c) 3 5 10 8 15
      (d) 0 1 1 2 4
      
     t.17:
     unordered