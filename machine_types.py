#run as admin

#import text: File NEEDS to be named "input.txt" and saved to the C:\ directory
with open(r"C:\input.txt", 'r') as f:
    first = f.read()

#split data into a list of separate strings
second = first.split()


#create new list of ONLY unique strings...
#this saves each serial, but also keeps a few stragglers such as PO, EID, timestamps, and machine types
third = []
for i in second:
    if i not in third:
        third.append(i)

#keeps only list items with 'REC-'
to_keep = ['REC-']
fourth = [x for x in third if any(y in x for y in to_keep)]

#for as many uniqe models that exist in the list,
#print which model they are and how many times each occurs (total number)
#slapped together appending of models results to the end of output.txt
for models in fourth:
    print(f'{models} {second.count(models)}')
    with open(r"C:\output.txt", 'a') as last:
        last.write("%s" % models + " " + str(second.count(models)) + "\n")

print('Done')
