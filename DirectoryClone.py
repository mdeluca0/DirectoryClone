import os

# Path to directory to be cloned
target = ""

# Path to directory to be created
clone = ""

print("Cloning \"" + target + "\" to \"" + clone + "\"")

os.mkdir(clone)

for (root, dirs, files) in os.walk(target):
	for name in files:
		path = os.path.join(root, name);
		path = path.replace(target, clone, 1)
		f = open(path, "w+")
		f.close()
		print("Created file: " + path)
	for name in dirs:
		path = os.path.join(root, name);
		path = path.replace(target, clone, 1)
		os.mkdir(path)
		print("Created directory: " + path)

print("Finished!")
