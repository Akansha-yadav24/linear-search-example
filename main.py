#using iterative 
def linearsearch(Arr,x):
  for a in range(len(Arr)):
      if Arr[a] == x:
        print("index value of item ",a)
        return a
 
  return -1
  print("item not found")

Arr=[50,12,30,58,95,63,40]
x=30
linearsearch(Arr,x)











"""
#using recursion
Arr=[50,12,30,58,95,63,40]
x=58
# Recursive function to search x in arr[l..r]
def recSearch( Arr, l, r, x):
	if r < l:
		return -1
	if Arr[l] == x:
		return l
	if Arr[r] == x:
		return r
	return recSearch(Arr, l+1, r-1, x)

n = len(Arr)

index = recSearch(Arr, 0, n-1, x)
if index != -1:
	print ("Element", x,"is present at index %d" %(index))
else:
	print ("Element %d is not present" %(x))"""
