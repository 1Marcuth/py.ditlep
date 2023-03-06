from setuptools import setup, find_packages

with open("README.md", "r") as file:
    readme_content = file.read()

setup(
    name="ditlep",
    version="1.0",
    license="MIT License",
    author="Marcuth",
    long_description=readme_content,
    long_description_content_type="text/markdown",
    author_email="marcuth2006@gmail.com",
    keywords="dragoncity dcutils tools",
    description=f"Fetcher/scraper of https://ditlep.com",
    packages=[ "ditlep/" + x for x in find_packages("ditlep") ],
    install_requires=[
        "anyio==3.6.2",
        "certifi==2022.12.7",
        "charset-normalizer==3.0.1",
        "h11==0.14.0",
        "h2==4.1.0",
        "hpack==4.0.0",
        "httpcore==0.16.3",
        "httpx==0.23.3",
        "hyperframe==6.0.1",
        "idna==3.4",
        "pycryptodome==3.17",
        "pydantic==1.10.4",
        "rfc3986==1.5.0",
        "sniffio==1.3.0",
        "typing_extensions==4.4.0",
        "urllib3==1.26.14"
    ]
)