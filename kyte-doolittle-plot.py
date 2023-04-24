# Hydropathy Plot

def kyte_doolittle():
    aa_seq = str(input("Protein_Sequence: "))
    
    no_of_aa_residues = len(aa_seq)
    print('No of aa residues:', no_of_aa_residues)
    
    hydropathy_score = {'A': 1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C': 2.5,'Q':-3.5,'E':-3.5,
                        'G':-0.4,'H':-3.2,'I': 4.5,'L': 3.8,'K':-3.9,'M': 1.9,'F': 2.8,
                        'P':-1.6,'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V': 4.2}   
    dict2 = {}
    l1, l2 = [], []
    for i in list(aa_seq.upper()):
        if i in hydropathy_score.keys():
            print(i, hydropathy_score[i])
            l1.append(i)
            l2.append(hydropathy_score[i])   

    fig = px.imshow([l2], text_auto=True)
    fig.show()
    
# To call the funtion

kyte_doolittle() # Type the amino acid sequences in the query box
