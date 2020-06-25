from io import open

from setuptools import find_packages, setup

with open('userpath/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = ['click']

setup(
    name='userpath',
    version=version,
    description='Cross-platform tool for adding locations to the user PATH, no elevated privileges required!',
    long_description=readme,
    author='Ofek Lev',
    author_email='ofekmeister@gmail.com',
    maintainer='Ofek Lev',
    maintainer_email='ofekmeister@gmail.com',
    url='https://github.com/ofek/userpath',
    license='MIT OR Apache-2.0',

    keywords=[
        'scripts',
        'user path',
        'path',
        'cli',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    install_requires=REQUIRES,
    extras_require={':platform_system == "Linux"': ['distro']},
    packages=['userpath'],
    entry_points={
        'console_scripts': [
            'userpath = userpath.cli:userpath',
        ],
    },
)
