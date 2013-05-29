from distutils.core import setup

setup(
    name='django-branch-permission',
    version='0.1.0',
    packages=['branch-permission'],
    license='LGPL',
    long_description=open('README.txt').read(),
    requires=['Django>=1.5']
)