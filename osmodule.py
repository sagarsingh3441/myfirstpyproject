import os

if ( not os.path.exists("folder")):
    os.mkdir("folder")
    for i in range (0,100):
        os.mkdir(f"folder/{i+1}")

    folders=os.listdir("folder")

    print(folders)
# os.chdir("/fol")


msg=input("Enter your data ")
oslistdata=dir(os)                   # all function of os save in oslistdata
f=open('sagguu.txt', 'a')
f.write(f"\n{msg}")
f.close()
f=open('sagguu.txt', 'r')
text=f.read()
print(text)

