# .fasta File Reader
geneWanted = input(" What gene do you want to read? ")
filename = geneWanted + ".fasta"
path = "/Users/jpiglesias/Desktop/JPIglesias/Bioinformatics/sequences/" + filename
file = open(path)
geneRaw = file.read()
gene = geneRaw.replace("\n", "")