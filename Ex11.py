#!/usr/bin/python
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# TO DO
# a) A line of hyphens the same length as the Belgium string, followed by;
# b) The string with the comma separators replaced by colons, followed by;
# c) The population of Belgium (2nd field), plus the population of the capital city (4th field)
# answer should be 11183818

print("-" * len(Belgium))
print(Belgium.replace(",", ": "))

fields = Belgium.split(",")
print(fields)
a = int(fields[1])
b = int(fields[3])
print(a + b)

answer = f"The result is: {a + b}"
print(answer)
