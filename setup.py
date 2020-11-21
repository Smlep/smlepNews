import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smlep_news",
    version="0.0.1",
    description="Custom news scrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=["feedparser==6.0.2", "requests==2.25.0"],
)