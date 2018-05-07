from setuptools import setup

setup(
    name='tuxinator_api',
    version='0.0.1',
    author='Grant Gangi',
    author_email='grant@tuxinator.net',
    packages=['tuxinator_api'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest',
        'pytest-runner',
    ],
)
