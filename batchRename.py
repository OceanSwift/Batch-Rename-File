import sys
import os

thisdir = os.getcwd()
pattern = ".wav"
newName = "file"

def main():
	if len(sys.argv) > 1:
		if sys.argv[1] == '?':
			print("arg1 = new name")
			print("arg2 = extention")
			return
		else:			
			newName = sys.argv[1]
	else:
		newName = "file"
	if len(sys.argv) > 2:
		pattern = sys.argv[2]
	else:
		pattern = ".wav"					

	fileList = [x for x in os.listdir(thisdir) if x.endswith(pattern)]	
	numberList = ["%.2d" % i for i in range(len(fileList))]
	
	i = 0
	for selections in fileList:
		if selections != '':
			os.rename(thisdir + "\\" + selections, thisdir + "\\" + newName + "_" + numberList[i] + pattern)
			i +=1	

if __name__ == "__main__":
    main()
       
