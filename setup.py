from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name="algoutils",
    version="0.0.3",
    description="Util functions to be used in algorithmic trading.",
    py_modules=["algoutils"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = ['ntplib',],
    extras_require = {
        "dev" : [
            "pytest>=3.7",
        ],
    },
    url="https://github.com/aticio/algoutils",
    author="Özgür Atıcı",
    author_email="aticiozgur@gmail.com",
)