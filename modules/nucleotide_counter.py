# .fasta File Reader
geneWanted = input(" What gene do you want to read? ")
filename = geneWanted + ".fasta"
path = "./sequences/" + filename
file = open(path)
geneRaw = file.read()
gene = geneRaw.replace("\n", "")

# Nucleotide Counter
A = gene.count("A")
T = gene.count("T")
C = gene.count("C")
G = gene.count("G")
totalNucleotides = A + T + G + C
ATr = (A + T) / totalNucleotides
GCr = (G + C) / totalNucleotides
print(" ")
print(filename, "Nucleotide Content")
print(" ")
print("Total = ", totalNucleotides)
print("A =", A)
print("T =", T)
print("C =", C)
print("G =", G)
print(" ")
print("AT Ratio =", round(ATr, 2))
print("GC Ratio =", round(GCr, 2))
print(" ")