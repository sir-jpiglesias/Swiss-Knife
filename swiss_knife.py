#        ___           ___                       ___           ___                    ___           ___                       ___           ___     
#       /\__\         /\  \                     /\__\         /\__\                  /|  |         /\  \                     /\__\         /\__\    
#      /:/ _/_       _\:\  \       ___         /:/ _/_       /:/ _/_                |:|  |         \:\  \       ___         /:/ _/_       /:/ _/_   
#     /:/ /\  \     /\ \:\  \     /\__\       /:/ /\  \     /:/ /\  \               |:|  |          \:\  \     /\__\       /:/ /\__\     /:/ /\__\  
#    /:/ /::\  \   _\:\ \:\  \   /:/__/      /:/ /::\  \   /:/ /::\  \            __|:|  |      _____\:\  \   /:/__/      /:/ /:/  /    /:/ /:/ _/_ 
#   /:/_/:/\:\__\ /\ \:\ \:\__\ /::\  \     /:/_/:/\:\__\ /:/_/:/\:\__\          /\ |:|__|____ /::::::::\__\ /::\  \     /:/_/:/  /    /:/_/:/ /\__\
#   \:\/:/ /:/  / \:\ \:\/:/  / \/\:\  \__  \:\/:/ /:/  / \:\/:/ /:/  /          \:\/:::::/__/ \:\~~\~~\/__/ \/\:\  \__  \:\/:/  /     \:\/:/ /:/  /
#    \::/ /:/  /   \:\ \::/  /   ~~\:\/\__\  \::/ /:/  /   \::/ /:/  /            \::/~~/~      \:\  \        ~~\:\/\__\  \::/__/       \::/_/:/  / 
#     \/_/:/  /     \:\/:/  /       \::/  /   \/_/:/  /     \/_/:/  /              \:\~~\        \:\  \          \::/  /   \:\  \        \:\/:/  /  
#       /:/  /       \::/  /        /:/  /      /:/  /        /:/  /                \:\__\        \:\__\         /:/  /     \:\__\        \::/  /   
#       \/__/         \/__/         \/__/       \/__/         \/__/                  \/__/         \/__/         \/__/       \/__/         \/__/    
# 
# BIOINFORMATICS SWISS KNIFE
# Simple set of tools for doing some science.
# Built by: José Pablo Iglesias (https://github.com/sir-jpiglesias)
# Licensed under the MIT License
# Last Edit (01/13/2020)

# Welcome Code
print("Welcome to Swiss Knife")
print("Tools Integrated: DNA Sequence Complementor (complement), DNA Nucleotide Counter (count), DNA Sequence Transcription (transcribe)")

# .fasta File Reader
geneWanted = input(" What sequence do you want to analyze? ")
filename = geneWanted + ".fasta"
path = "sequences/" + filename
file = open(path)
geneRaw = file.read()
gene = geneRaw.replace("\n", "")

selection = input(" What do you want to do? ")

if selection == "count":
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
elif selection == "complement":
    # Sequence Complementor
    print("Given Strand")
    print(gene)
    print("")
    print("Complementary Strand")
    for i in gene:
        if i == "A":print("T", end= "")
        elif i == "T":print("A", end= "")
        elif i == "C":print("G", end= "")
        elif i == "G":print("C", end= "")
        else: print("Error")
    print("")
elif selection == "transcribe":
    # DNA Transcription
    print("")
    print("Given DNA Strand")
    print(gene)
    print("")
    print("RNAm Strand")
    for i in gene:
        if i == "A":print("U", end= "")
        elif i == "T":print("A", end= "")
        elif i == "C":print("G", end= "")
        elif i == "G":print("C", end= "")
        else: print("Error")
    print("")
else:
    print("ERROR: Input is not valid.")
