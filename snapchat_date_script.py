import os 
import filedate

# SNAPCHAT
# Snapchat modify date script, I don't know if Immich now gets the image creation date from the file name,
###  when I tried it didn't and resulted in everything being "taken" on the same day. Replace path with the directory of the images you want to process

path = r"C:\Users\Name\Downloads\datacheckout\images"
month = ['','January','February','March','April','May','June','July','August','September','October','November','December']

for x in os.listdir(path):
    if os.path.isdir(os.path.join(path,x)) == True:
        pass
    else:
        namesplit = x.split("-")
        day = namesplit[2][:2]
        convmonth = month[int(namesplit[1])]
        year = namesplit[0]

        imgfile = os.path.join(path,x)

    # Some files were labled Nov 31st, thus giving an error, could be some daylight savings funkery idk how it happened. 

        try:
            filedate.File(imgfile).set(
            created = f"{day} {convmonth} {year}, 12:32",
            modified = f"{day} {convmonth} {year}, 12:32"
            )
        except:
            filedate.File(imgfile).set(
            created = f"2 {convmonth} {year}, 12:32",
            modified = f"2 {convmonth} {year}, 12:32"
            )        
