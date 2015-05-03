#!/usr/bin/env python3

from propresenter_lib.presentation import Presentation


p = Presentation(title='Test', version=500)
print(p.xml_string())