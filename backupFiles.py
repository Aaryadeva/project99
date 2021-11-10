import os
import shutil
import time

def backup():
	deleted_folders_count = 0
	deleted_files_count = 0
	path = "C:\Users\rajee\Desktop\game\backup"
	days = 30
	seconds = time.time() - (days * 24 * 60 * 60)
	if os.path.exists(path):
		for firstFolder, folders, files in os.walk(path):
			if seconds >= get_file_or_folder_age(firstFolder):
				delete_folder(firstFolder)
				deleted_folders_count += 1 
				break
			else:
				for folder in folders:
					folder_path = os.path.join(firstFolder, folder)
					if seconds >= get_file_or_folder_age(folder_path):
						delete_folder(folder_path)
						deleted_folders_count += 1 
				for file in files:
					file_path = os.path.join(firstFolder, file)					
					if seconds >= get_file_or_folder_age(file_path):						
						delete_file(file_path)
						deleted_files_count += 1 
		else:
			if seconds >= get_file_or_folder_age(path):
				delete_file(path)
				deleted_files_count += 1

	else:
		print(f'"{path}" was not found')
		deleted_files_count+=1
         
	print(f"number of folders deleted:{deleted_folders_count}")
	print(f"number of files deleted:{deleted_files_count}")

def delete_folder(path):
	if not shutil.rmtree(path):
		print(f"{path} is removed successfully")
	else:
		print(f"not able to delete the "+path)

def delete_file(path):
	if not os.remove(path):
		print(f"{path} was deleted")
	else:
		print("not able to delete "+path)

def get_file_or_folder_age(path):
	ctime = os.stat(path).st_ctime
	return ctime


backup()