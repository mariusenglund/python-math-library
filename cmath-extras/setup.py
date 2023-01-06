from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='cmath_extras',
    version='1.0.0',
    description='A package of functions to deal with complex numbers in Python more efficiently.',
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type='text/markdown',
    url='xxx',
    author='Marius Englund',
    author_email='englund.marius@outlook.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        ],
    keywords=[
        'python', 'math', 'mathematics', 'complex numbers', 
        'imaginary numbers', 'electrical circuits',
        ],
    packages=find_packages(),
    python_requires='>=3'
)