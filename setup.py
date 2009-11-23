# $Id: setup.py,v 1.3 2007/08/28 15:38:19 asc Exp $

from distutils.core import setup
import os.path

setup(name="machinetag",
      version="1.1",
      description="Python class for parsing machine tags",
      author="Aaron Straup Cope",
      author_email="aaron@aaronland.net",
      url="http://aaronland.info/python/machinetag",
      license="Perl Artistic",
      packages = ['machinetag'],
      )
