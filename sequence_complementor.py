# .fasta File Reader
geneWanted = input(" What gene do you want to read? ")
filename = geneWanted + ".fasta"
path = "/Users/jpiglesias/Desktop/JPIglesias/Bioinformatics/sequences/" + filename
file = open(path)
geneRaw = file.read()
gene = geneRaw.replace("\n", "")

print("Given Strand")
print(gene)
print("")

print("Complementary Strand")
# Complement Generator
for i in gene:
    if i == "A":print("T", end= "")
    elif i == "T":print("A", end= "")
    elif i == "C":print("G", end= "")
    elif i == "G":print("C", end= "")
    else: print("Error")

print("")
