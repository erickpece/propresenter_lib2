from lxml import etree, objectify
import logging


class ProPresenterObject():

	def __init__(self, version=500):
		logging.info('Created ProPresenterObject: {}'.format(type(self)))

		self.version = version

	def xml(self):
		logging.info('Attempting to generate object from XML structure.')

		pro_object = None

		if self.version == 500:
			pro_object = self.generate_version_500()
		else:
			return None

		objectify.deannotate(pro_object, pytype=True, xsi=True, xsi_nil=True, cleanup_namespaces=True)

		logging.info('Succeeded generating object from XML structure.  Returning.')

		return pro_object

	def xml_string(self):
		logging.info('Returning string version of XML object.')

		return etree.tostring(self.xml())

	def __str__(self):
		description = "=" * 80
		description += "\nObject: {}\n".format(self.__class__.__name__)
		description += "=" * 80

		for attr in vars(self):
			description += "\n{}: {}".format(attr, getattr(self, attr))

		description += "\n"

		return description