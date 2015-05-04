#!/usr/bin/env python3
import logging

FORMAT = '%(asctime)-15s | %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

from propresenter_lib.presentation import Presentation


p = Presentation(title='Test', version=500)
print(p.xml_string())