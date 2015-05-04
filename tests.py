#!/usr/bin/env python3

import logging
import unittest
from propresenter_lib.presentation import Presentation
from propresenter_lib.shared import Shared

logging.basicConfig(level=logging.ERROR)


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


class TestShared(unittest.TestCase):

	def test_rgb_hex_to_propresenter_color(self):
		s = Shared()
		self.assertEqual(s.rgb_hex_to_propresenter_color(127, 127, 127),
			'0.4980392156862745 0.4980392156862745 0.4980392156862745 1')

if __name__ == '__main__':
	unittest.main()