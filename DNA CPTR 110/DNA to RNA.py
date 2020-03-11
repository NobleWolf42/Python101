__author__ = "Benjamin Carpenter", "Dillon Britt"

#Imports
from random import randrange

#http://www.soc-bdr.org/rds/authors/unit_tables_conversions_and_genetic_dictionaries/e5202/index_en.html

#Dictionaries
amino_acids = {"GCU": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine",
               "CGU": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine", "AGA": "Arginine", "AGG": "Arginine",
               "AAU": "Asparagine", "AAC": "Asparagine",
               "GAU": "Aspartate", "GAC": "Aspartate",
               "UGU": "Cysteine", "UGC": "Cysteine",
               "CAA": "Glutamine", "CAG": "Glutamine",
               "GAA": "Glutamate", "GAG": "Glutamate",
               "GGU": "Glycine", "GGC": "Glycine", "GGA": "Glycine", "GGG": "Glycine",
               "CAU": "Histidine", "CAC": "Histidine",
               "AUU": "Isoleucine", "AUC": "Isoleucine", "AUA": "Isoleucine",
               "AUG": "Methionine",
               "UUA": "Leucine", "UUG": "Leucine", "CUU": "Leucine", "CUC": "Leucine", "CUA": "Leucine", "CUG": "Leucine",
               "AAA": "Lysine", "AAG": "Lysine",
               "UUU": "Phenylalanine", "UUC": "Phenylalanine",
               "CCU": "Proline", "CCC": "Proline", "CCA": "Proline", "CCG": "Proline",
               "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine", "AGU": "Serine", "AGC": "Serine",
               "ACU": "Threonine", "ACC": "Threonine", "ACA": "Threonine", "ACG": "Threonine",
               "UGG": "Tryptophan",
               "UAU": "Tyrosine", "UAC": "Tyrosine",
               "GUU": "Valine", "GUC": "Valine", "GUA": "Valine", "GUG": "Valine",
               "UAG": "Stop", "UGA": "Stop", "UAA": "Stop"
                }


#Global Variables
done = False
rn = 0
seconds = 0
userls = []
userlsin = []


def dna_to_rna(dnas): #Converts a three charter DNA to a three charter RNA
    '''
    RNA: U G A C
         ^ ^ ^ ^
         | | | |
    DNA: A C T G
    '''

    rnal = []
    j = ""
    h = ""
    c = 0
    #rna = []
    for i in range(0, len(dnas)):
        dna = list(dnas[i])
        rna = []
        for j in range(0, len(dna)):
            if dna[j] == "A":
                h = "U"
            elif dna[j] == "C":
                h = "G"
            elif dna[j] == "T":
                h = "A"
            elif dna[j] == "G":
                h = "C"
            rna.append(h)
            #print(h)
        rnal.append(rna[0]+rna[1]+rna[2])
    #rnal.append(rna[3]+rna[4]+rna[5])
    return rnal


def dna_to_amino(dna):
    hello = False
    rna = dna_to_rna(dna)
    aa = []
    rna.append("UAG")
    while not hello:
        for k in range(0, len(rna)):
            if amino_acids[rna[k]] == "Stop":
                hello = True
            elif len(rna[k]) != 3:
                pass
            else:
                aa.append(amino_acids[rna[k]])
    return aa

def missing(checklist, mainlist):
    """ Returns the list containing all the elements of list
        checklist that are not found in list mainlist.  If
        mainlist contains all the elements in checklist, the
        function returns the empty list. This function does
        not modify the lists passed to it. """

    return [i for i in checklist if i not in mainlist]
                # statement that uses list comprehension
def looping():
    global userlsin
    loop = True
    time = 0
    userlsin = []
    print('Type a section of DNA, which consists of three letters. The possible letters are "A", "C", "T", or "G".')
    print('Repeat this as much as you wish, up to 20 DNA strands, typing "Done" will exit the loop.')
    while loop:
        if time != 20:
            userin = input("::")
            userin = userin.upper()
            time += 1
            if userin == "DONE":
                loop = False
            else:
                userlsin.append(userin)
        else:
            loop = False
looping()

userls = dna_to_amino(userlsin)


while not done:
    dnall = []
    for j in range(0, len(userls)):
        dnal = []
        for i in range(0,3):
            dnain = randrange(1, 5)
            if dnain == 1:
                dnal.append("A")
            elif dnain == 2:
                dnal.append("C")
            elif dnain == 3:
                dnal.append("T")
            elif dnain == 4:
                dnal.append("G")
        #print(dnal)
        dnall.append(dnal[0]+dnal[1]+dnal[2])
    rndmamino = dna_to_amino(dnall)
    miss = missing(rndmamino, userls)
    #print(dna_to_amino(dnall))
    if miss == [] and len(userls) > 1:
        done = True
        seconds += 10
        print("The peptide contains the following amino acids:",)
        print(userls)
    elif miss == [] and len(userls) <= 1:
        done = True
        seconds += 10
        print("There is no peptide, you have the following amino acid:",)
        print(userls)
    else:
        seconds += 10
    secnd = seconds
    seconds = int((secnd+1000)*(1/720)*1000)
    if miss == [] and len(userls) <= 1:
        print("It took", seconds, "seconds to form this amino acid")
    elif miss == [] and len(userls) > 1:
        print("It took", seconds, "seconds to form this peptide")


seco = seconds
year = 0
month = 0
days = 0
hours = 0
minuet = 0
tookt = 0
while seco > 0:
    sec5 = 0
    while seco >= 31557600:
        year += 1
        seco -= 31557600
    while seco >= 2592000:
        month =+ 1
        seco -= 2592000
    while seco >= 86400:
        days += 1
        seco -= 86400
    while seco >= 3600:
        hours += 1
        seco -= 3600
    while seco >= 60:
        minuet += 1
        seco -= 60
    while seco < 60 and seco > 0:
        sec5 = seco
        seco = 0
print(year, " Year(s), ", month, " Month(s), ", days, " Day(s), ", hours, " Hour(s), ", minuet, " Minute(s), ", sec5, " Second(s)", sep = "")


# time for one amino acid 4.934466339439176e-05
