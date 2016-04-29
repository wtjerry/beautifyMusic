from setuptools import setup

setup(
    name="beautifyMusic",
    install_requires=["mutagenx"],
    packages=["beautifyMusic"],
    entry_points={"console_scripts": ["beautifyMusic = beautifyMusic.__main__:main"]}
)
