import subprocess,time
from os import walk



def ShowFileNames(path):
    return next(walk(path),(None,None,[]))[2]

AllFiles = ShowFileNames(".")

def SendMeFile(i):
    try:
        ConvertName = i.replace("xlsx","") + "txt"
        subprocess.run(["ssconvert", i, ConvertName])
    except Exception as Hata:
        print("Dostum Birseyler Bok Yolu. ->" + Hata)
        pass

if __name__ == "__main__":
    for i in AllFiles:
        try:
            SendMeFile(i)
        except Exception as Hata:
            print("Dostum Birseyler Bok Yolu. ->" + Hata)
            pass
        finally:
            print("Finito.")