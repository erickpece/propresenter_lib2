from lxml import etree, objectify
from .propresenter import ProPresenterObject
import logging


class Presentation(ProPresenterObject):

	def __init__(self, title, **kwargs):
		self.title = title
		self.notes = kwargs.get("notes", "")
		self.size_x = kwargs.get("size_x", "1920")
		self.size_y = kwargs.get("size_y", "1080")

		super().__init__(**kwargs)

	def generate_version_500(self):
		logging.info('Building version 500 document structure')

		presentation = objectify.Element("RVPresentationDocument")
		presentation.attrib['CCLIArtistCredits'] = ""
		presentation.attrib['CCLICopyrightInfo'] = ""
		presentation.attrib['CCLIDisplay'] = "0"
		presentation.attrib['CCLILicenseNumber'] = ""
		presentation.attrib['CCLIPublisher'] = ""
		presentation.attrib['CCLISongTitle'] = ""
		presentation.attrib['album'] = ""
		presentation.attrib['artist'] = ""
		presentation.attrib['author'] = ""
		presentation.attrib['backgroundColor'] = "0 0 0 1"
		presentation.attrib['category'] = "Presentation"
		presentation.attrib['chordChartPath'] = ""
		presentation.attrib['creatorCode'] = "0"
		presentation.attrib['docType'] = "0"
		presentation.attrib['drawingBackgroundColor'] = "0"
		presentation.attrib['height'] = self.size_y
		presentation.attrib['lastDateUsed'] = ""
		presentation.attrib['notes'] = self.notes
		presentation.attrib['resourcesDirectory'] = ""
		presentation.attrib['usedCount'] = "0"
		presentation.attrib['versionNumber'] = str(self.version)
		presentation.attrib['width'] = self.size_x

		logging.info('Succeeded building version 500 document structure.  Returning.')

		return presentation
