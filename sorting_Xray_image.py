#mahadi


import os
import shutil


'''

destination1 =os.mkdir('Pneumonia') 
destination2 = os.mkdir('Normal')
'''


destination1 = "/Users/mhway/Desktop/Os test/Pneumonia"
destination2 = "/Users/mhway/Desktop/Os test/Normal"



source = os.listdir()

 

for f in source:

    if f=='.DS_Store':
       continue
    
    if f.startswith("person"):
        print("Pneumonia")
        shutil.move(f,destination1)
        
        #shutil.copy('os.getcdw(f.startswith("per"))','Pneumonia')
        #shutil.copy('os.getcwd()/f','Pneumonia' )
    if f.startswith("nor") or f.startswith("NOR") or f.startswith("IM-") or f.startswith("im-") :
        print("normal")
        shutil.move(f,destination2)
 
