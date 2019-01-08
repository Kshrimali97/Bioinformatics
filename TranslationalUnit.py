seq = "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCGTGAAGCATGTGGGGGTGAGCCCAGGGGCCCCAAGGCAGGGCACCTGGCCTTCAGCCTGCCTCAGCCCTGCCTGTCTCCCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGGTGAGCCAACTGCCCATTGCTGCCCCTGGCCGCCCCCAGCCACCCCCTGCTCCTGGCGCTCCCACCCAGCATGGGCAGAAGGGGGCAGGAGGCTGCCACCCAGCAGGGGGTCAGGTGCACTTTTTTAAAAAGAAGTTCTCTTGGTCACGTCCTAAAAGTGACCAGCTCCCTGTGGCCCAGTCAGAATCTCAGCCTGAGGACGGTGTTGGCTTCGGCAGCCCCGAGATACATCAGAGGGTGGGCACGCTCCTCCCTCCACTCGCCCCTCAAACAAATGCCCCGCAGCCCATTTCTCCACCCTCATTTGATGACCGCAGATTCAAGTGTTTTGTTAAGTAAAGTCCTGGGTGACCTGGGGTCACAGGGTGCCCCACGCTGCCTGCCTCTGGGCGAACACCCCATCACGCCCGGAGGAGGGCGTGGCTGCCTGCCTGAGTGGGCCAGACCCCTGTCGCCAGGCCTCACGGCAGCTCCATAGTCAGGAGATGGGGAAGATGCTGGGGACAGGCCCTGGGGAGAAGTACTGGGATCACCTGTTCAGGCTCCCACTGTGACGCTGCCCCGGGGCGGGGGAAGGAGGTGGGACATGTGGGCGTTGGGGCCTGTAGGTCCACACCCAGTGTGGGTGACCCTCCCTCTAACCTGGGTCCAGCCCGGCTGGAGATGGGTGGGAGTGCGACCTAGGGCTGGCGGGCAGGCGGGCACTGTGTCTCCCTGACTGTGTCCTCCTGTGTCCCTCTGCCTCGCCGCTGTTCCGGAACCTGCTCTGCGCGGCACGTCCTGGCAGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCACACCCGCCGCCTCCTGCACCGAGAGAGATGGAATAAAGCCCTTGAACCAGC"
print "The given nucleotide is"
print seq
print '\n'

if 'T' in seq:
    print 'This is a DNA sequence'
    print '\n'
    start_codon="ATG"
    stop_codon="TAG","TAA","TGA"
    genetic_code = {
        'GCT':'A', 'GCC':'A','GCA':'A','GCG':'A',
        'CGT':'R', 'CGC':'R','CGA':'R','CGG':'R','AGA':'R', 'AGG':'R',
        'AAT':'N', 'AAC':'N',
        'GAT':'D', 'GAC':'D',
        'TGT':'C', 'TGC':'C',
        'CAA':'Q', 'CAG':'Q',
        'GAA':'E', 'GAG':'E',
        'GGT':'G', 'GGC':'G','GGA':'G','GGG':'G',
        'CAT':'H', 'CAC':'H',
        'ATT':'I', 'ATC':'I','ATA':'I',
        'TTA':'L', 'TTG':'L','CTT':'L','CTC':'L','CTA':'L', 'CTG':'L',
        'AAA':'K', 'AAG':'K',
        'ATG':'M',
        'TTT':'F', 'TTC':'F',
        'CCT':'P', 'CCC':'P','CCA':'P','CCG':'P',
        'TCT':'S', 'TCC':'S','TCA':'S','TCG':'S','AGT':'S', 'AGC':'S',
        'TGG':'W', 
        'TAT':'Y', 'TAC':'Y',
        'GTT':'V', 'GTC':'V','GTA':'V','GTG':'V',
        'TAA':'*', 'TGA':'*','TAG':'*',
        'ACT':'T', 'ACC':'T','ACA':'T','ACG':'T'
        }
    s = seq.replace("A","X").replace("T","A").replace("X","T").replace("G","Y").replace("C","G").replace("Y","C")
    print "Complement of nucleotide is"
    print s
    print('\n')
else:
    print 'This is a RNA sequence'
    print '\n'
    start_codon="AUG"
    stop_codon="UAG","UAA","UGA"
    genetic_code = {
        'GCU':'A', 'GCC':'A','GCA':'A','GCG':'A',
        'CGU':'R', 'CGC':'R','CGA':'R','CGG':'R','AGA':'R', 'AGG':'R',
        'AAU':'N', 'AAC':'N',
        'GAU':'D', 'GAC':'D',
        'UGU':'C', 'UGC':'C',
        'CAA':'Q', 'CAG':'Q',
        'GAA':'E', 'GAG':'E',
        'GGU':'G', 'GGC':'G','GGA':'G','GGG':'G',
        'CAU':'H', 'CAC':'H',
        'AUU':'I', 'AUC':'I','AUA':'I',
        'UUA':'L', 'UUG':'L','CUU':'L','CUC':'L','CUA':'L', 'CUG':'L',
        'AAA':'K', 'AAG':'K',
        'AUG':'M',
        'UUU':'F', 'UUC':'F',
        'CCU':'P', 'CCC':'P','CCA':'P','CCG':'P',
        'UCU':'S', 'UCC':'S','UCA':'S','UCG':'S','AGU':'S', 'AGC':'S',
        'UGG':'W', 
        'UAU':'Y', 'UAC':'Y',
        'GUU':'V', 'GUC':'V','GUA':'V','GUG':'V',
        'UAA':'*', 'UGA':'*','UAG':'*',
        'ACU':'T', 'ACC':'T','ACA':'T','ACG':'T'
        }
    s = seq.replace("A","X").replace("U","A").replace("X","U").replace("G","Y").replace("C","G").replace("Y","C")
    print "Complement of nucleotide is"
    print s
    print '\n'

l = len(s)
reverse = s[l:0:-1]
print "Reverse complement is"
print reverse
print '\n'



#CALCULATING READING FRAMES 1, 2, 3
a=[]                                                 											  #generating an empty list a
def rf123(ORF, genetic_code):                        											  #defining  a function
    
    for j in range(0,3):                             										      #3 RFs so range goes from [0,3)                             
        protein = ''                                 									          #creating an empty string
        for i in range(j, len(ORF), 3):
            codon = ORF[i:i+3]                       											  #iterating over codon of length 3
		 																						  #codon of length 3 gives a Amino Acid
            if (len(codon) < 3):                     											  #codon length cannot be less than 3
                break
            
            protein += genetic_code[codon]
        print "Frame", j+1, protein
        a.append(protein)                           											  #appending protein in the list a
        
print rf123(seq, genetic_code)

#CALCULATING READING FRAMES -1, -2, -3
b=[]                                                  											  #generating an empty list b
def rf456(ORF, genetic_code):                         											  #defining  a function
    
    for j in range(0,3):
        protein = ''
        for i in range(j, len(ORF), 3):
            codon = ORF[i:i+3]
            if (len(codon) < 3):
                break
            
            protein += genetic_code[codon]
        print "Frame", -(j+1), protein
        b.append(protein)
        
print rf456(reverse, genetic_code)



#Calculating open reading frames of 1st, 2nd and 3rd frame
c =[]                                                 												#generating an empty list c
e =[]                                                 												#generating an empty list e
for p in range(0, 3):
    print '\n'
    string=a[p]                                       												#1st 2nd & 3rd RF
       
    j = 0
    k = 0
    for i in range(j,len(string)):
        if(i<k):                                    												#if string (i points here) MTDRSTHVMKU*(k points here)
            i= i+1                                   												# MKU* is not an ORF therefore, condition is i<k
        else:
            if(string[i]=='M'):
                print "Position of M is " + str(i)
                for k in range(i+2,len(string)):     												# M* is not an ORF. So loop starts from i+2
                    if(string[k]=='*'):
                        print "Postion of * is " + str(k)
                        print "ORF", p+1, "is " + string[i:k]
                        print "length of the above ORF is " + str((len(string[i:k])))
                        e.append(string[i:k])                                						#store the given ORF in e
                        c.append(len(string[i:k]))                           						#store the length of ORF in c
                        break
    max = c[0]
    for z in range(0, len(c)):
        if(c[z]>=max):
            max = c[z]
    print "The largest ORF of RF ",p+1, "is", e[c.index(max)], "of length", max
    del(c[0:len(c)])
    del(e[0:len(e)])
   
#Calculating open reading frames of -1st, -2nd and -3rd frame
d = []                                                  											#generating an empty list d
f = []                                                  											#generating an empty list f
for p in range(0, 3):
    print '\n'
    string=b[p]
    j = 0
    k = 0
    for i in range(j,len(string)):
        if(i<k):
            i= i+1
        else:
            if(string[i]=='M'):
                print "Position of M is " + str(i)
                for k in range(i+2,len(string)):
                    if(string[k]=='*'):
                        print "Postion of * is " + str(k)
                        print "ORF", -(p+1), "is " + string[i:k]
                        print "length of the above ORF is " + str((len(string[i:k])))
                        f.append(string[i:k])
                        d.append(len(string[i:k]))
                        break
    max = d[0]
    for z in range(0, len(d)):
        if(d[z]>=max):
            max = d[z]
    print "The largest ORF of RF ",-(p+1), "is",  f[d.index(max)], "of length", max
    del(d[0:len(d)]) 
    del(f[0:len(f)])




