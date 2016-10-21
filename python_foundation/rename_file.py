import os
def rename_files():
	file_list=os.listdir(r"/home/dreamer/udacity/python_foundation/prank")
	print file_list
	os.chdir(r"/home/dreamer/udacity/python_foundation/prank")
	for file_name in file_list:
		print("old name->"+file_name)
		os.rename(file_name,file_name.translate(None,"0123456789"))
		print("new name->"+file_name)
rename_files()	
