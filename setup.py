from setuptools import setup, find_packages
import subprocess
import os

geoz_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='geoz',
    version= geoz_version,
    description='A Library to create Geographic Maps from Unsupervised algorithms',
    py_modules=['geoz'],
    package_dir={'':'src'},
    install_requires=['pandas', 'mlxtend', 'scikit-learn', 'matplotlib', 'geopandas'],
    
    
    extras_require={
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: GIS",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Khalid ElHaj",
    author_email="KG.Khair@Gmail.com",
    url="https://github.com/Ne-oL/geoz"
    
    )
