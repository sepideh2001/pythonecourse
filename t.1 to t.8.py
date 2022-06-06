 t.1:
A)Tuples and lists are two similar sequences. Tuples are immutable, and they cannot be changed once they are created.While, it is a sequential list that can be changed.
B) Shows the literal syntax of tuples by parentheses, while how literally lists are represented by square brackets.
C)Tuples are heterogeneous and lists are homogeneous
.D)Tuples show the structure and lists show the order.

t.2:
tuple is created by placing all the items (elements) inside parentheses (), separated by commas. The parentheses are optional, however, it is a good practice to use them.A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).(“ “)
 
 t.3
 immutable
 
 t.4
 ordered
 
 t.5
 a = 1, 2, 3, 4, 5, 6, 7, 8 a (1, 2, 3, 4, 5, 6, 7, 8) s=-,-,*s,-,-= as = tuple(s)print(tuple(s)
                                                                                        
 t.6
 a = 1, 2, 3, 4, 5, 6, 7, 8 / a (1, 2, 3, 4, 5, 6, 7, 8)s = a[3:7] s = tuple(s) print(tuple(s))
 
 t.7
 a=7, 10, -3, 18, 6, 10 / a (7, 10, -3, 18, 6, 10)s = x,y = t[0],t[5]s = tuple(s)print(tuple(s))

t.8
 def mul_tuple(tuple) : 
  product = 1
  for i in tuple:
   product = product * i
   return product

tuple1 = (11, 12, 4, 3)
print(tuple1)
print("product:",mul_tuple(tuple1))