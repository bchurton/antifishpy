import setuptools

def readme() -> str:
    with open("README.md", "r") as f:
        return f.read()

setuptools.setup(
    name="antifishpy",
    version="1.1.0",
    author="Benjamin Churton",
    description="A simple Python module for the Bitflow Anti-Fish API.",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["antifishpy"],
    install_requires=["aiohttp"]
)
