import os 
import filedate
import shutil

# Google
### Google script for taking the creation date from its .json counterpart, and applying it to the image file. 
### For all the files it can't get a date for it'll put them in a folder named "date extract failed"
### just like the snapchat one put the folder path in "path" just like the snapchat script, 
### currently it doesn't go into subfolders, I should probably add that. 

path = r"E:\Google Checkout\Takeout\Google Photos\Untitled(10)"

for x in os.listdir(path):
    try:
        os.mkdir(os.path.join(path,"failed"))
    except:
        pass

    try:
        file = open(os.path.join(path,x+".json"),"r")
        line = file.readlines()[10]

        convtime = line.split(' ')[8].split(":")
        time = convtime[0]+":"+convtime[1]+":00 "+convtime[2][-2:]
        year = line.split(' ')[7][:-1]
        month = line.split(' ')[5][1:]
        day = line.split(' ')[6][:-1]

        filedate.File(os.path.join(path,x)).set(created = f"{day} {month} {year}, {time}",
                             modified = f"{day} {month} {year}, {time}")     
        
    except:
        if x.endswith(".json"):
            pass
        else:
            shutil.move(os.path.join(path,x), os.path.join(path,"date extract failed",x))
            print(f'failed on file {x}')
        pass


