import os,sys
#initialize some useful lists
ext_list = []
docs = ['.pdf','.doc','.docx','.ppt','.pptx','.xls','.xlsx','.txt','.xml','.html','.htm','.php','.epub']
scripts = ['.ini','.bat','.c','.cpp','.py','.java','.css','.sh','.js']
videos = ['.mp4','.mkv','.avi','.m4a','.wmv']
music = ['.mp3','.wav','.wma']
archives = ['.7z','.gz','.tar','.zip','.jar','.rar','.iso']
exes = ['.msi','.exe','.deb']
android = ['.apk']
images = ['.jpg','.jpeg','.tiff','.gif','.png','.bmp','.ico']
others = ['.torrent','.crdownload']
#directory names
docsdir = 'Documents'
scriptsdir = 'Scripts'
videosdir = 'Videos'
musicdir = 'Music'
archivesdir = 'Compressed'
exesdir = 'Software'
androiddir = 'Android'
imagesdir = 'Images'
othersdir = 'Other'
androiddir='Android'
#current script name
current_script = sys.argv[0]
#create_dir function
def create_dir(dirname):
	if not os.path.exists(dirname):
		os.makedirs(dirname)
#copy files function
def copyfile(f,dirname):
	print 'Moving '+f+' to '+dirname+'...'
	os.rename(os.getcwd()+'/'+f,os.getcwd()+'/'+dirname+'/'+f)
	
#main program
#store names of files in the current folder
file_list = os.listdir(os.getcwd())

#loop through each file, find unique extensions
for f in file_list:
	extension = os.path.splitext(f)[1]
	if extension.lower() not in ext_list:
	    ext_list.append(extension.lower())
#print found extensions
print 'Found the following extensions:',
for f in ext_list:
	print f[1:],
print ''
#create directories
for f in ext_list:
	if f in docs:
		create_dir(docsdir)
	elif f in scripts:
		create_dir(scriptsdir)
	elif f in videos:
		create_dir(videosdir)
	elif f in music:
		create_dir(musicdir)
	elif f in archives:
		create_dir(archivesdir)
	elif f in exes:
		create_dir(exesdir)
	elif f in images:
		create_dir(imagesdir)
	elif f in others:
		create_dir(othersdir)
	elif f in android:
		create_dir(androiddir)
#loop through files
for f in file_list:
	if f == current_script:
	        continue
	ext = os.path.splitext(f)[1]
	ext = ext.lower()
	if ext in docs:
		copyfile(f,docsdir)
	elif ext in scripts:
		copyfile(f,scriptsdir)
	elif ext in images:
		copyfile(f,imagesdir)
	elif ext in archives:
		copyfile(f,archivesdir)
	elif ext in exes:
		copyfile(f,exesdir)
	elif ext in music:
		copyfile(f,musicdir)
	elif ext in videos:
		copyfile(f,videosdir)
	elif ext in others:
		copyfile(f,othersdir)
	elif ext in android:
		copyfile(f,androiddir)
print 'Done organizing your folder!'
