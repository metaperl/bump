from setuptools import setup


setup(
    name="bump",
    version="1.1.0",
    description="Bumps package version numbers",
    long_description=open("README.rst").read(),
    license="MIT",
    url="https://github.com/di/bump",
    author="Mark Steve Samson",
    author_email="hello@marksteve.com",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="bump increment package version",
    zip_safe=False,
    py_modules=["bump"],
    install_requires=["click>=6,<7", "first", "packaging>=17.1"],
    entry_points={"console_scripts": ["bump = bump:main"]},
)
