from setuptools import setup

setup(
    name="beautifyMusic",
    version="0.1",
    license="GPLv2+",
    install_requires=["mutagenx"],
    packages=["beautifyMusic"],
    entry_points={"console_scripts": ["beautifyMusic = beautifyMusic.__main__:main"]}
)
