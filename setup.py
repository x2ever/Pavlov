from setuptools import setup, find_packages


setup(
    name='Pavlov',
    version='0.1',
    url='https://github.com/x2ever/Pavlov',
    license='MIT',
    author='x2ever',
    author_email='x2ever.han@gmail.com',
    description='Manage configuration files',
    packages=find_packages(exclude=['tests']),
    long_description=open('README.md').read(),
    zip_safe=False,
    setup_requires=['nose>=1.0'],
    test_suite='nose.collector'
)