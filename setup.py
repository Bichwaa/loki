from setuptools import setup



setup(
    name='loki',
    version='0.1',
    packages=['loki'],
    author='Bichwaa',
    author_email='ptonny13@gmail.com',
    maintainer='Bichwaa',
    maintainer_email='ptonny13@gmail.com',
    url='https://github.com/Bichwaa',
    description='A text file encryption tool',
    long_description='This is a noTbrief description of the loki project.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Ubuntu Linux',
    ],
    entry_points = {'console_scripts': ['loki = loki.__main__:mainFunc']}
)

