from ftplib import FTP

ftp = FTP("home743930078.1and1-data.host")
ftp.login(user = "u94054091", passwd = "PwBRW8@7ZbtBJ-$H")

def grabFile():
	filename = "mata.gif"
	localfile = open(filename, "wb")
	ftp.retrbinary("RETR " + filename, localfile.write, 1024)

	ftp.quit()
	localfile.close()

def placeFile():
	filename = "mata.gif"
	ftp.storbinary("STOR " + filename, open(filename, "rb"))
	ftp.quit()

placeFile()