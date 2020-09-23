import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="env-automatically",
    version="0.0.1",
    author="Thiago Nogueira",
    author_email="thiagonf10@gmail.com",
    description="Tool extract environments from settings.py to .env file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiagonf/env-automatically",
    packages=setuptools.find_packages(),
    entry_points ={ 
        'console_scripts': ['env-automaticaly=env_automatically.extract_env:main']}, 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)