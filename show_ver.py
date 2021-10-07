show_version = "    *0       CISCO881-SEC-K9       FTX0000038X    "

#if you wanted to remove all spaces could use .replace method
#this first matches the space in ' ' and replaces with contents of second brackets (nothing)
#show_version = show_version.replace(' ',  '')

#strip removes all the leading and trailing whitespace, but not inbetween
show_version = show_version.strip()

#print (show_version)

# now we want to spilt show_version into a list

output = show_version.split()
model = output[1]
serial = output[2]

# note spilt 0 is not relevant

print("Model number is: " ,model)
print("serial Number is: " ,serial)

# make model number lowercase

model = model.lower()
#print(model)

vendor_chk = "juniper" in model
print("Is this a Juniper Router?: " ,vendor_chk)

vendor_chk = "cisco" in model
print("Is this a Cisco Router?: " ,vendor_chk)

model_chk = "881" in model
print("Is this an 881 Router? " ,model_chk)