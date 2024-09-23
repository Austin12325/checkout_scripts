import os 
import filedate
import shutil

# Google
### Google script for taking the creation date from its .json counterpart, and applying it to the image file. 
### For all the files it can't get a date for it'll put them in a folder named "failed"
### just like the snapchat one put the folder path in "path" just like the snapchat script, 
### currently it doesn't go into subfolders, I should probably add that. 
### I added it 

#Put your path inbetween the quotes
#Example, path = r"E:\Google Checkout\Takeout\Google Photos"
path = r""
failed = 0
finished = 0
to_process = 0 

for file in os.walk(os.path.join(path)):
     if os.path.isdir(os.path.join(path,file[0])):
          for f in os.listdir(os.path.join(path,file[0])):
            if f.endswith('json'):
                to_process += 1

max_amount = to_process

for folder in os.walk(os.path.join(path)):
        print(folder[0])
        if os.path.isdir(os.path.join(path,folder[0])) == True:
            if os.path.join(path,folder[0]) == os.path.join(path,'failed'):
                pass
            
            else:
                if os.path.isdir(os.path.join(path,folder[0],'failed')) == False:
                    if folder[0].endswith('failed'):
                        pass
                    else:
                        os.mkdir(os.path.join(path,folder[0],'failed'))
                           
                for f in os.listdir(folder[0]):
                    
                    if f == 'failed':
                            pass
             
                    else:
                        
                        if os.path.isdir(os.path.join(path,folder[0],f)):
                            pass
                        else:
                            try:
                                file = open(os.path.join(path,folder[0],f+".json"),"r")
                                line = file.readlines()[10]

                                convtime = line.split(' ')[8].split(":")
                                time = convtime[0]+":"+convtime[1]+":00 "+convtime[2][-2:]
                                year = line.split(' ')[7][:-1]
                                month = line.split(' ')[5][1:]
                                day = line.split(' ')[6][:-1]

                                filedate.File(os.path.join(path,folder[0],f)).set(created = f"{day} {month} {year}, {time}",
                                                    modified = f"{day} {month} {year}, {time}")     
                                # filedate.File(os.path.join(path,folder[0],f)).set(created = f"{day} {month} {year}, {time}",
                                #                     modified = f"{1} {1} {2000}, {time}")   
                                to_process -= 1
                                finished += 1                 
                            except:
                                if f.endswith(".json"):
                                    pass
                                else:
                                    shutil.move(os.path.join(path,folder[0],f), os.path.join(path,folder[0],"failed",f))
                                    failed += 1

                        print(f'{to_process} / {max_amount}')
# Unsure why its saying a handful is left to process. 
print(f' total {to_process}')
print(f'Number of files processed {finished}')
print(f'Number of files failed {failed}')
