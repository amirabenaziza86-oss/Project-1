from pandas import DataFrame
data={"sequence":["ATGCGTACGTA","GCTAGCTAGGCC","ATGCGCGTAAGT","TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGAT"] ,"Longueur":[12,12,12,10,11,10,10] ,"Pourcentage GC":[50,66.67,58.33,40,45.45,60,50]}
df=DataFrame(data)
print("Creation de tableau","\n",df,"\n")
Longueur=df["Longueur"]
print("La colonne de Longueur","\n",Longueur,"\n")
filtred=df[df["Longueur"]>10]
print("Le tableau avec filtrage","\n",filtred,"\n")
average_GC=df["Pourcentage GC"].mean()
print(f"Pourcentage  moyen de GC={average_GC:.3f}%","\n")

df["Catégorie"]=df["Pourcentage GC"].apply(lambda x: "Riche" if x>55 else("Faible" if x<45 else "Moyen"))
print("Tableau avec nouveau colonne Catégorie","\n",df,"\n")
df["Nombre de G"]=df["sequence"].str.count("G")
print("Tableau avec nouveau colonne Nombre de G","\n",df,"\n")
ecart_de_gc=(sum((df["Pourcentage GC"]-average_GC)**2)/len(df["Pourcentage GC"]))**(1/2)
print("L'ecart de Pourcentage GC =",ecart_de_gc,"\n")
for i in df["sequence"]:
    print(f"La longueur de la sequence {i} est :{len(i)}")
df.to_csv("tableau_sequences.csv",index=False)    
