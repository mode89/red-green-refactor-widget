import setuptools

def get_long_description():
    with open("README.md", "r") as readme_file:
        return readme_file.read()

setuptools.setup(
    name="red-green-refactor-widget",
    version="0.0.1",
    author="Andrey Krainyak",
    author_email="mode.andrew@gmail.com",
    description=\
        "A simple user interface that will help you to stick with "
        "the red-green-refactor workflow",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="http://github.com/mode89/red-green-refactor-widget",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)