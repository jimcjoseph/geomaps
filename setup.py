import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="geomaps",
    version="0.1",
    author="Jim Joseph",
    author_email="jimcjoseph@gmail.com",
    description="GeoMaps",
    long_description=(read('README')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: GeoNode',
        'License :: OSI Approved :: BSD',
    ],
    license="BSD",
    keywords="geonode django",
    url='https://github.com/jim/geomaps',
    scripts = [
               'scripts/geomaps',
              ],
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
)
