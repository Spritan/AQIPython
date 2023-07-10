from setuptools import find_packages, setup

with open("./README.md", "r") as f:
    long_description = f.read()

setup(
    name="AQIPython",
    version="0.0.07",
    description="An python AQI calculator library",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Spritan/py-aqi",
    author="Spritan",
    author_email="proypabsab@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
    # install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    # python_requires=">=3.10",
)