from setuptools import setup

setup(
    name='dumptube',
    version='1.0.0',
    packages=['dumptube'],
    include_package_data=True,
    install_requires=[
        'pytube',
        'google-api-python-client',
    ]
)
