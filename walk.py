import os
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   
   return "%s %s" % (s, size_name[i])

print()

for dirpath, dirnames, filenames in os.walk("/opt"):
	print("Current Path:", dirpath)
	print("SubDirectories:", dirnames)
	print("Files:", filenames)
	print()

	for fn in filenames:
		path = os.path.join(dirpath, fn)
		size = os.stat(path).st_size

		print("\tFile: {} {}".format(path, convert_size(size)))
	
	print("--------------------------------------------------------------")

