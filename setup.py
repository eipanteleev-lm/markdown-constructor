import os
from setuptools import setup, find_packages

BASE_PATH = os.path.abspath(__file__)
FOLDER_PATH = os.path.dirname(BASE_PATH)


def get_readme():
    with open(os.path.join(FOLDER_PATH, 'README.md')) as f:
        text = f.read()

    return text.strip()


setup(
    name='markdown-constructor',
    description=(
        'A simple python module for object oriented generating '
        'Markdown formatted text'
    ),
    version='0.1.0',
    packages=find_packages(),  # list of all packages
    python_requires='>=3.7',  # any python greater than 3.7
    include_package_data=True,
    author='Evgenii Panteleev',
    long_description=get_readme(),
    long_description_content_type="text/markdown"
)
