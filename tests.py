#!/usr/bin/env python3

import unittest
from propresenter_lib.presentation import Presentation


class TestPresentation(unittest.TestCase):

	def test_version_500(self):
		p = Presentation(title='Test', version=500)
		self.assertEqual(p.version, 500)

	def test_version_fail(self):
		p = Presentation(title='Test', version=100)
		self.assertNotEqual(p.version, None)

	def test_default_format(self):
		p = Presentation(title='Test', version=500)
		self.assertEqual(p.xml_string(), b'<RVPresentationDocument CCLIArtistCredits="" CCLICopyrightInfo="" CCLIDisplay="0" CCLILicenseNumber="" CCLIPublisher="" CCLISongTitle="" album="" artist="" author="" backgroundColor="0 0 0 1" category="Presentation" chordChartPath="" creatorCode="0" docType="0" drawingBackgroundColor="0" height="1080" lastDateUsed="" notes="" resourcesDirectory="" usedCount="0" versionNumber="500" width="1920"/>')


if __name__ == '__main__':
	unittest.main()