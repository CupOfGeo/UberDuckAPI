from setuptools import setup
setup(
    name='uberduckapi',
    version='0.0.9',
    description='python wrapper for uberduck api',
    packages=["uberduckapi"],
    url='https://uberduck.ai/',
    maintainer='George Mazzeo',
    maintainer_email='mazzeogeorge@gmail.com',
    install_requires=['requests','polling'],

    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)
