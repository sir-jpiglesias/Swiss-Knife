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

selection = input(" What do you want to do? ")

if selection == "count":
    import nucleotide_counter
    nucleotide_counter.count()
    print("")
elif selection == "complement":
    import sequence_complementor
    sequence_complementor.complement()
    print("")
elif selection == "transcribe":
    import sequence_transcript
    sequence_transcript.transcribe()
    print("")
else:
    print("ERROR: Input is not valid.")
