from setuptools import setup

setup(
    name='mdf',
    version='0.1',

    description='MDN a simple pip for downloading facebook videos',
    long_description="Visit https://mahim.me",
    url='https://mahim.me',

    author='Mazidul islam',
    author_email='immazidulislam@gmail.com',

    license='GNU',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'License :: OSI Approved :: GNU General Public License (GPL)',

        'Programming Language :: Python ',

    ],

    keywords='mdf mazidul mahim',

    packages=["mdf"],
    install_requires=['tqdm', "argparse"],
    entry_points={
        'console_scripts': [
            'mdf=mdf:TheMain',
        ],
    },

)
