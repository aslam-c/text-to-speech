import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_pdf_reader",
    version="0.0.1",
    author="aslam",
    author_email="asdmail045@gmail.com",
    description="Reads text from PDF document and save it as an audio file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aslam-c/text-to-speech",
    project_urls={
        "Bug Tracker": "https://github.com/aslam-c/text-to-speech",
        "repository": "https://github.com/aslam-c/text-to-speech"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)
