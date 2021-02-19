import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="seq_alignment_rls542", # Replace with your own username
    version="0.0.5",
    author="Ryan Stevens and James Nesbit",
    author_email="ryan.louis.stevens@gmail.com",
    description="A package to compute edit distance measurements and sequence alignments.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryanlstevens/py_string_matchers",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
