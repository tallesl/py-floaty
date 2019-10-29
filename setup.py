from setuptools import find_packages, setup

setup(name='floaty',
      version='2.1.0',
      url='https://github.com/tallesl/py-floaty',
      author='Talles Lasmar',
      author_email='talleslasmar@gmail.com',
      description='Bandages for boto3 floating-point wounds.',
      long_description=open('README.md', 'r').read(),
      long_description_content_type='text/markdown',
      packages=find_packages())
