import shutil
import os

def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)


def check_exist_or_mkdirs(path):
    '''thread-safe mkdirs if not exist'''
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


with open('pathlist.txt', 'r') as filehandle:
	for line in filehandle:
		line = line.strip()
		src_path = os.path.join('../', line)
		dest_path = line
		copyDirectory(src_path, dest_path)
		
		
