from subprocess import call
import os.path

def install_package(git_address, package_name):
	BASEDIR = os.path.join(os.path.dirname((os.path.dirname(__file__))))
	box_path = os.path.join(BASEDIR, 'box/')
	name = package_name.lower()
	install_temp_path = os.path.join(box_path, name + "-pkg/")
	install_path = os.path.join(box_path, name)
	if not git_address:
		print "You need to specify a git repo address"
	else:
		call(['mkdir', install_temp_path])
		call(['git', 'clone', git_address, install_temp_path])
		call(['ln','-s',install_temp_path+name+'/',install_path])
		print "Package " + name + " installed"