import sys
# Project 2
# Filte_packets.py by caleb ghatt (trying his best!)

def filter(fileName) :
	print('called filter function in filter_packets.py')
	f=open(str(fileName), 'r')
	line=f.readline()
	fileName=fileName[:-4]
	while line:
		#line=f.readline()
		line=line.strip()
		if "Echo" in line:
			print("", file=open(fileName+"_filtered.txt", "a"))
			print("No.     Time           Source                Destination           Protocol Length Info", file=open(fileName+"_filtered.txt", "a"))
			
			print(line, file=open(fileName+"_filtered.txt", "a"))
			line=f.readline().strip()

			if line=="":
				#line=f.readline() #Commenting this out will determine whether the program skips the line or adds blank
				while(line!="\n"):
					print(str.rstrip(line), file=open(fileName+"_filtered.txt", "a"))
					line=f.readline()

			#line=f.readline()
			line=f.readline()
			#print(line)
		line=f.readline()
	f.close()

fileName=str(sys.argv[1])
filter(fileName)

