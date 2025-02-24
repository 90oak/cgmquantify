from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    ld = f.read()
    

setup(name='cgmquantify',
      version='0.5',
      description='Quantifying glucose and glucose variability from CGM devices',
      long_description= ld,
      long_description_content_type= 'text/markdown',
      url='https://github.com/brinnaebent/cgmquantify',
      #download_url='https://github.com/brinnaebent/cgmquantify/archive/0.4.tar.gz',
      author='Brinnae Bent',
      author_email='bmbent@ncsu.edu',
      license='MIT',
      packages=['cgmquantify'],
      install_requires=['pandas','numpy','matplotlib','datetime','statsmodels', 'plotly',
                        ],
      zip_safe=False)
