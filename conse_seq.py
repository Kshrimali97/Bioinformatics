import numpy as np 

string = "GTACAGACGGACAAAAATTGTACAGACGAGTGTTGCCCAAGTTAGAACATTCAACTGTACAGACGATTCAACTAAGTTAGAACAGTGTTGCCCATTCAACTAAGTTAGAACGACAAAAATTATTCAACTAAGTTAGAACATTCAACTGTACAGACGAGTGTTGCCCAGTGTTGCCCAGTGTTGCCCAGTGTTGCCCATTCAACTAGTGTTGCCCATTCAACTAGTGTTGCCCGACAAAAATTAGTGTTGCCCAGTGTTGCCCAGTGTTGCCCAAGTTAGAACAAGTTAGAACGACAAAAATTATTCAACTAGTGTTGCCCAGTGTTGCCCGTACAGACGGTACAGACGAAGTTAGAACAAGTTAGAACAAGTTAGAACGACAAAAATTAAGTTAGAACGACAAAAATTAAGTTAGAACGTACAGACGAAGTTAGAACAGTGTTGCCCAGTGTTGCCCGTACAGACGGTACAGACGAGTGTTGCCCGTACAGACGATTCAACTGACAAAAATTATTCAACTAGTGTTGCCCGTACAGACGGTACAGACGATTCAACTATTCAACTAGTGTTGCCCGTACAGACGGTACAGACGATTCAACTATTCAACTAAGTTAGAACAGTGTTGCCCGTACAGACGGTACAGACGATTCAACTATTCAACTAGTGTTGCCCATTCAACTAGTGTTGCCCGTACAGACGATTCAACTAGTGTTGCCCATTCAACTGTACAGACGGTACAGACGATTCAACTAGTGTTGCCCGTACAGACGATTCAACTAGTGTTGCCCGACAAAAATTAAGTTAGAACGACAAAAATTATTCAACTATTCAACTGACAAAAATTATTCAACTAAGTTAGAACATTCAACTGACAAAAATTAAGTTAGAACGACAAAAATTATTCAACTAAGTTAGAACAGTGTTGCCCATTCAACTATTCAACTATTCAACTGTACAGACG"


d={}  #Creating a dictionary to store all the 10-mers and their frequencies.

count=0

for i in range(0,len(string)):
  for j in range(i,len(string),10):
    s=string[i:i+10]
    if(len(s)==10):
      if s in d.keys():
        d[s]=d[s]+1  #if that pattern already exists then it's value is increment by 1.
      else:
        d[s]=1    #if that pattern occurs for the first time theb it's value is set to 1.
        
        
print "Printing all the 10-mers along with their frequencies"

print ""
for key,values in d.items():
  print d.items()  
list=d.keys()   #storing all the patterns in a list.
arr=np.array(list)
a=[]
f={} #creating a dictionary to store the similar patterns and their frequencies.
for i in range(0,len(arr)-1):
	for j in range(0,len(arr)-1):
		count=0
		for k in range(0,10):
			if(arr[i][k]!=arr[j][k]):
		  		count=count+1
		
	  	if(count<=2):
	  	  s=arr[i]
	  	  if s in f.keys():
	  	    f[s]=f[s]+1
	  	  else:
	  	    f[s]=1
print ""
		
print "Now printing all the similar patterns along with their frequencies."	
print ""
for key,values in f.items():
  print f.items() 
print ""    
list1=f.values()
arr1=np.array(list1)
max1=list1[0]
# Finding the max freq of all the similar patterns present in f. 
for i in range(0,len(list1)):
  if list1[i]>max1:
    max1=list1[i]
print "Maximum Frequency found in the above similar patterns is ", max1 
print ""
#Now printing all the patterns whose frequncy matches with the max frequency.
for key,values in f.items():
  if(values==max1):
    print key
