#run as admin or abandon all hope

#import text: File NEEDS to be named "input.txt" and saved to the C:\ directory
with open(r"C:\input.txt", 'r') as f:
    first = f.read()
    print(first)

#split data into a list of separate strings
second = first.split()
print(second)

#create new list of ONLY unique strings...
#this saves each serial, but also keeps a few stragglers such as PO, EID, timestamps, and machine types
third = []
for i in second:
    if i not in third:
        third.append(i)

print(third)

#trim away machine type and timestamps
to_remove = ['REC-', ':']
fourth = [x for x in third if not any(y in x for y in to_remove)]

#writes new text file with (mostly) only serials.
#file will be created in the C:\ directory where input.txt was originally pulled
#date/PO/EID at the beginning will still need trimmed as well as metadata at the end
#paring these down with additional paramaters may affect integrity of longer/temporary serials
with open(r"C:\output.txt", 'w') as last:
    for e in fourth:
        last.write("%s\n" % e)
    print('Done')
