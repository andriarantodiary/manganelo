from setuptools import setup, find_packages

VERSION = "1.7"


def read_file(file):
    with open(file, "r") as fh:
        return fh.read()


setup(
    name="manganelo",
    packages=find_packages(),
    version=VERSION,
    license="MIT",

    description="Unofficial API for the Manganelo website.",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",

    author="Joshua Nixon",
    author_email="joshuanixonofficial@gmail.com",

    url="https://github.com/nixonjoshua98/manganelo",

    download_url=f"https://github.com/nixonjoshua98/manganelo/archive/v{VERSION}.tar.gz",
  
    keywords=["manga", "manganelo", "scrapper", "web", "mangakakalot", "thread", "comic", "manhwa"],
  
    install_requires=[
        "bs4",
        "requests",
        "reportlab",
        "pillow"
    ],

    classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Development Status :: 5 - Production/Stable",
      "Intended Audience :: Developers",
      "Topic :: Software Development :: Build Tools",
    ],

    python_requires='>=3.7'
)
