#ask for input dna sequence
user_dna=input("Enter your Dna seq- ")

#calculating A,T amount using '.count()' method
amt_A=user_dna.count("A")
amt_T=user_dna.count("T")
amt_total=len(user_dna)
amt_AT=(amt_A+amt_T)/amt_total*100
print("AT content is given dna seq is ",amt_AT)
