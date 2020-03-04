import os, shutil

def work(directory, list):
	directory = directory + os.path.sep + 'maps'
	print(list)
	files = os.listdir(directory)
	listfile = open(list).readlines()
	
	restrictedfiles = len(listfile);
	resFound = 0;
	
	for f in files:
		#print(f);
		fl = str(f).rstrip().lower().replace(':', '').replace(' ', '_').replace('\'', '')
		for l in listfile:
			#print(l)
			lf = str(l).rstrip().lower().replace(':', '').replace(' ', '_').replace('\'', '')
			if(lf == fl):
				resFound = resFound + 1;
				print("'" + fl + "' -> '" + lf + "' == '" + str(lf == fl) + "' #" + str(resFound))
				shutil.rmtree(os.getcwd() + os.path.sep + directory + os.path.sep + f)
	
	print("Found " + str(resFound) + "/" + str(restrictedfiles))

work('PGMCollection', 'PGMCollectionRestrictions.txt');
work('StratusCollection', 'StratusCollectionRestrictions.txt');
work('OCNCollectionAF', 'OCNCollectionRestrictionsAF.txt');
work('OCNCollectionGN', 'OCNCollectionRestrictionsGN.txt');
work('OCNCollectionOZ', 'OCNCollectionRestrictionsOZ.txt');