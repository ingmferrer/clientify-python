import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='clientify',
      version='0.0.6',
      description='API wrapper for Clientify written in Python',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
      url='https://github.com/ingmferrer/clientify-python',
      author='Miguel Ferrer',
      author_email='ingferrermiguel@gmail.com',
      license='MIT',
      packages=['clientify'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
