import os
from os import listdir
from os.path import isfile, join

try:
	#Define movie directory.
	rawMovieList = os.listdir('/ YOUR MOVIE DIRECTORY HERE /')
	#Create movie file to write to.
	movieFile = open("movieList.txt", "w+")
	#Create show file to write to.
	showFile = open("showList.txt", "w+")

	#Removes .DS_STORE file - Only use if you use/get your files from a Mac.
	#del rawMovieList[0]

	#Removes extensions on files.
	extensionsMovieList = [extension[:-4] for extension in rawMovieList]
	#Removes duplicate file names due to subtitle files.
	filteredMovieList = set(extensionsMovieList)
	#Reorders movies in alphabetic order.
	filteredMovieList = sorted(filteredMovieList)
	#Writes movie list to txt file.
	for movie in filteredMovieList:
		movieFile.write(movie+"\r\n")
	movieFile.close()
	print("Movie list complete!")
except:
	print("An error occured while writing the movie list.")

try:
	#Define show list.
	rawShowList = []
	#Gets all files in all directories and writes them to list.
	for subdir, dirs, files in os.walk('/ YOUR TV SHOW DIRECTORY HERE /'):
		for file in files:
			rawShowList.append(file)
	#Remove extensions on files.
	extensionShowList = [extension[:-4] for extension in rawShowList]
	#Removes any .DS_Store files and write show list to txt file.
	for show in extensionShowList:
		if not show.startswith('.'):
			showFile.write(show+"\r\n")
	showFile.close()
	print("Show list complete!")
except:
	print("An error occured while writing the show list.")