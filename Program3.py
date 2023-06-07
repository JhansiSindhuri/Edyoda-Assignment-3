# Calculate the upper and lower cases

# Python program  that accepts a string and calculate the number of upper case letters and lower case letters.

def given_string(s):
    a={"UPPER_CASE":0, "LOWER_CASE":0}
    for b in s:
        if b.isupper():
           a["UPPER_CASE"]+=1
        elif b.islower():
           a["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", a["UPPER_CASE"])
    print ("No. of Lower case Characters : ", a["LOWER_CASE"])

given_string('The quick Brow Fox')
