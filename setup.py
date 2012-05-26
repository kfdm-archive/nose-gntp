from setuptools import setup

setup(
    name='nose-gntp',
    version='0.1',
    author='Paul Traylor',
    url='http://github.com/kfdm/nose-gntp/',
    description='nose plugin for Growl notifications',
    install_requires=['nose>=0.10', 'gntp'],
    license='MIT',
    packages=['nose_gntp'],
    package_data={'nose_gntp': [
        './*.png'
    ]},
    include_package_files=True,
    entry_points={
        'nose.plugins': [
            'growl=nose_gntp:NoseGrowl'
            ]
        }
    )
