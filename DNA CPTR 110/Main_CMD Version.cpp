//This C++ Program is a program that shows how long it takes for DNA to become an oligopeptide
//Dillon Britt
//

#include <iostream>
#include <vector>
#include <map>
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

std::vector<char> DNA( int DNA_sequence_length)
{
    //DNA is made of nucleotides; Each nucleotide contains a phosphate group, a sugar group and a nitrogen base.
    //The four types of nitrogen bases are adenine (A), thymine (T), guanine (G) and cytosine (C). 
    //The order of these bases is what determines DNA's instructions, or genetic code.
    std::vector<char> DNA_letters;
    DNA_letters.push_back('A');//when i = 0, it is adenine
    DNA_letters.push_back('C');//when i = 1, it is cytosine
    DNA_letters.push_back('T');//when i = 2, it is thymine
    DNA_letters.push_back('G');//when i = 3, it is guanine
    
    std::vector<char> DNA_sequence;
    std::cout << "DNA input code :  ";
    for(int i = 1; i <= DNA_sequence_length; i++)
    {
        int random = rand() % 3 + 1;
        char random_char = DNA_letters[random];
        std::cout << random_char;
        DNA_sequence.push_back(random_char);
    }
    std::cout << "\n";
    return DNA_sequence;
}

std::vector<char> DNA_RNA(std::vector<char> DNA_sequence)
{
    //Function gets the DNA from the DNA function and turns it into RNA
    //
    std::vector<char> RNA_strand;
    
    int size = DNA_sequence.size();
    int i = 0;
    std::cout << "RNA output code : ";
    for( ; i < size; i++ )
        {
            char DNA_char_sequence = DNA_sequence[i];
            RNA_strand.push_back(DNA_char_sequence);
            char RNA = RNA_strand[i];
            
            if(RNA == 'G')
                {
                    RNA = 'C';
                }
            
            else if(RNA =='C')
                {
                    RNA = 'G';
                }
                
            else if(RNA == 'T')
                {
                    RNA = 'A';
                }
            else if(RNA == 'A')
                {
                    RNA = 'U';
                }
                
                RNA_strand[i] = RNA;
            std::cout << RNA;
        }
    
    return RNA_strand;
}

std::vector<std::string> Amino_acid()
{
    //This is a list of all the twenty Amino acids that are used in this process
    std::vector<std::string>Amino_acid;
    std::vector<std::string> New_Amino_list;
    
    Amino_acid.push_back("non");//0
    Amino_acid.push_back("Arg");//1
    Amino_acid.push_back("Lys");//2
    Amino_acid.push_back("Asp");//3
    Amino_acid.push_back("Glu");//4
    Amino_acid.push_back("Gln");//5
    Amino_acid.push_back("Asn");//6
    Amino_acid.push_back("His");//7
    Amino_acid.push_back("Ser");//8
    Amino_acid.push_back("Thr");//9
    Amino_acid.push_back("Tyr");//10
    Amino_acid.push_back("Cys");//11
    Amino_acid.push_back("Met");//12
    Amino_acid.push_back("Trp");//13
    Amino_acid.push_back("Ala");//14
    Amino_acid.push_back("Ile");//15
    Amino_acid.push_back("Leu");//16
    Amino_acid.push_back("Phe");//17
    Amino_acid.push_back("Val");//18
    Amino_acid.push_back("Pro");//19
    Amino_acid.push_back("Gly");//20

    
    
    int size = Amino_acid.size();
    for(int i = 1; i < size ; i++)
        {
            std::cout << Amino_acid[i] << " Number  = " << i << "\n";
        }
        
        
        
    int number_picked;
    int count = 1;
    for( ;count <=20 ; count ++)
        {
            std::cout << "Pick an Amino Acid Number (Press zero when you are done picking Amino Acids), 1 - 20 : ";
            std::cin>> number_picked;
            
            if(number_picked == 0)
                {
                    break;
                }
            
            while(number_picked < 0 || number_picked > 20)
            {
                std::cout << "Please pick a valid number : ";
                std::cin >> number_picked;
                
            }
            std::string new_amino_acid_string = Amino_acid[number_picked];
            New_Amino_list.push_back(new_amino_acid_string);
        }
    
    

    return New_Amino_list;
}

std::vector<char> Ribosome(std::vector<std::string> Amino_acid, std::vector<char> RNA_strand)
{
    //The ribosome is a large and complex molecular machine, found within all living cells, that serves as the primary site of biological protein synthesis (translation). 
    //Ribosomes link amino acids together in the order specified by messenger RNA (mRNA) molecules.
    int i = 0;
    int size = Amino_acid.size();
    
    
    
    return RNA_strand;//Temp for now
}

int main()
{
    
    std::vector<std::string> Amino_acid_list = Amino_acid();//You pick the amino acids and returns the vectors of elements you have chosen
    int DNA_sequence_length = Amino_acid_list.size() * 3;
    std::vector<char> DNA_sequence = DNA(DNA_sequence_length);
    std::vector<char> RNA;
    
    DNA_RNA(DNA_sequence);
    DNA_sequence = RNA;
    Ribosome(Amino_acid_list, RNA);
}