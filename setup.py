from setuptools import setup, find_packages

from codecs import open
import os

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def files_in_folder(folder):
    return [
        (subfolder, [os.path.join(subfolder, file) for file in files])
        for subfolder, _, files in os.walk(folder)
    ]

setup(
    name='insaniquarium',

    version='0.0.1',

    description='A game about fishes and aliens.',
    long_description=long_description,

    url='https://github.com/gvpavlov/Insaniquarium',

    author='Georgi Pavlov',
    author_email='georgipavlov94@gmail.com',

    license='GPLv2',

    classifiers=[
        'Intended Audience :: End Users/Desktop',

        'Natural Language :: Bulgarian',
        'Natural Language :: English',

        'Topic :: Games/Entertainment :: Arcade',

        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='insaniquarium',

    packages=find_packages(),

    install_requires=['pyxdg'],

    extras_require={
        'dev': [],
        'test': [],
    },

    package_data={

    },

    data_files = files_in_folder('insaniquarium/gui/resources'),

    entry_points={
        'console_scripts': [
            'insaniquarium=insaniquarium.gui.ui:main',
        ],
    },
)
