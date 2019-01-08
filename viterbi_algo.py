
#taking input sequence
str=raw_input()
#print seq[2]
#To check the sequence contains only A,G,C,T in it!!
#if not then then we re-enter the sequence.

for i in range(0,len(str)):
  if str[i]!='a' and str[i]!='c' and str[i]!='g' and str[i]!='t':
    print "Enter the sequence again"
    seq=raw_input()

#converting to upper case
str=str.upper()
print "The sequence is:"+str
print ""

str1=list(str)

#starting probabilities
p1=p2=-1

#Only log odd scores are taken in the emmision and transition probabilities .

#Emission Probabilities
h={'A': -2.322 , 'C': -1.737 , 'G': -1.737 , 'T': -2.322}
l={'A': -1.737 , 'C': -2.322 , 'G': -2.322 , 'T': -1.737}

#Transition Probabilities
hh=-1		#high to high
ll=-0.737	#low to low
hl=-1		#high to low
lh=-1.322	#low to high

#lists to store the probability of element coming from high or low state
high=[]
low=[]

#for first nucleotide
high.append(p1 + h[str1[0]])
low.append(p2 + l[str1[0]])

for j in range(1,len(str)):
	high.append(h[str1[i]] + max((high[j-1] + hh) , (low[j-1] + lh)))
	low.append(l[str1[i]] + max((high[j-1] + hl) , (low[j-1] + ll)))


print("probabilities taken from high state are")
print high

print ""

print("probabilities taken from low state are")
print low
print

output=[]

#checking for max probabilities 
for i in range(len(str)-1, -1, -1):
	if(low[i]>high[i]):
		output.append('L')
	else:
		output.append('H')

output=output[ : :-1]

print "Output"
print output
