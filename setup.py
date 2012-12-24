import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Don't import paysio module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'paysio'))
import importer
import version

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

# Get simplejson if we don't already have json
install_requires = ['requests >= 0.8.8']
try:
  importer.import_json()
except ImportError:
  install_requires.append('simplejson')

try:
  import json
  _json_loaded = hasattr(json, 'loads')
except ImportError:
  pass

setup(name='paysio',
      version=version.VERSION,
      description='Paysio python bindings',
      author='Paysio',
      author_email='support@paysio.com',
      url='https://paysio.com/',
      packages=['paysio'],
      package_data={'paysio' : ['data/ca-certificates.crt', '../VERSION']},
      install_requires=install_requires,
      test_suite='test',
)
