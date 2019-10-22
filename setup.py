from setuptools import setup, find_packages

with open("./minette_symphony/version.py") as f:
    exec(f.read())

setup(
    name="minette_symphony",
    version=__version__,
    url="https://github.com/uezo/minette-symphony",
    author="uezo",
    author_email="uezo@uezo.net",
    maintainer="uezo",
    maintainer_email="uezo@uezo.net",
    description="Adapter for Symphony to create chatbot using Minette framework.",
    packages=find_packages(exclude=["examples*", "develop*", "tests*"]),
    install_requires=["minette", "sym-api-client-python", "lxml"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
