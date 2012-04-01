from setuptools import setup, find_packages

setup(
    name='nose-gntp',
    version='0.1',
    author='Paul Traylor',
    url='http://github.com/kfdm/nose-gntp/',
    description='nose plugin for Growl notifications',
    install_requires=['nose>=0.10', 'gntp'],
    license='MIT',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'nose.plugins': [
            'growl=nose_gntp:NoseGrowl'
            ]
        }
    )
