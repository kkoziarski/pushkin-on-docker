from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

long_description = """
Pushkin is a free open source tool for sending push notifications. It was
developed with a focus on speed and enabling fast experimentation.  Pushkin was
mainly built for supporting online mobile games, but can easily be extended to
any type of application. It supports both Android and iOS platforms.
"""

setup(
    name='pushkin',
    version='0.1.6.1',

    description='Pushkin is a free open source tool for sending push notifications',
    long_description=long_description,

    url='https://github.com/Nordeus/pushkin.git',

    author='Nordeus LLC',
    author_email='pushkin.dev@nordeus.com',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],

    # What does your project relate to?
    keywords='development push notifications mobile',

    packages=find_packages(exclude=['docs']),

    setup_requires=['pytest-runner'],
    install_requires=[
        # Only used for tests
        'pytest==4.0.1',
        'pytest-mock==1.10.0',
        'funcsigs==1.0.2',
        'mock==2.0.0',
        'pytest-tornado==0.5.0',
        'tornado==5.1.1',
        'configparser==3.5.0',
        'protobuf==2.6.1',
        'psycopg2==2.7.6.1',
        'requests==2.20.1',
        'sqlalchemy==1.3.0b1',
        'alembic==1.0.3',
        'hyper==0.7.0',
        ],
    package_data = {
        '': ['*.sql', '*.sh', '*.ini', '*.mako']
    },

    entry_points={
        'console_scripts': [
            'pushkin=pushkin.pushkin_cli:main',
        ],
    },
)
