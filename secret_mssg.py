import os
def rename_file():
   file_name=os.listdir(r"/home/dreamer/udacity/python_foundation/prank")
   #print file_name
   saved_path=os.getcwd()
   os.chdir(r"/home/dreamer/udacity/python_foundation/prank")
   for name in file_name:
      os.rename(name,name.translate(None,"0123456789"))
   os.chdir(saved_path)   
rename_file()    
