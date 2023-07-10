from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="idgenerator",
    version="0.0.10",
    description="An python AQI calculator library",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Spritan/py-aqi",
    author="Spritan",
    author_email="proypabsab@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
    # install_requires=["bson >= 0.5.10"],
    extras_require={
    },
    # python_requires=">=3.10",
)