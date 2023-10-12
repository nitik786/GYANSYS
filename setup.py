from setuptools import setup, find_packages

setup(
    name='weather_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'mysql-connector-python',
        'pandas',
    ],
)

