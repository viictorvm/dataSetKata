from setuptools import setup, find_packages

requires = [
    'tornado',
    'tornado-sqlalchemy',
    'psycopg2',
]

setup(
    name='dataset',
    version='0.0',
    description='dataset problem',
    author='Victor Vallecillo',
    author_email='viictorvallecillo@gmail.com',
    keywords='web tornado',
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'serve_app = todo:main',
        ],
    },
)