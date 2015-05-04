import os
import uuid
import shutil


class Shared:
	
	def get_uuid(self):
		uuid_string = uuid.uuid4()
		return str(uuid_string).upper()

	def rgb_hex_to_propresenter_color(self, r, g, b):
		return "{} {} {} 1".format(r/255, g/255, b/255)

	def write_to_file(self, filename, data):
		target = open(filename, 'w')
		target.write(data.decode())
		target.close()

	def copy_file(self, source, target):
		head, tail = os.path.split(source)

		destination = os.path.join(target, tail)
		# destination += ".{}".format(extension)

		print("Trying to copy {} to {}".format(source, destination))

		shutil.copy(source, destination)