# Phalcon KIT Documentation

Welcome to the documentation for Phalcon KIT. This documentation project is built using MkDocs and serves as a
comprehensive guide to understanding and utilizing the features provided by Phalcon KIT.

## Official Documentation

Visit the [official documentation site](https://github.com/phalcon-kit/docs) for detailed information, tutorials, and examples on
using Phalcon KIT.

## Phalcon KIT Website

For more information about Phalcon KIT and its features, visit the [official website](https://github.com/phalcon-kit/core).

## Installation

To build and install the documentation locally, follow these steps:

Clone the repository:

```bash
git clone https://github.com/phalcon-kit/docs.git
```

Navigate to the project directory:

```bash
cd docs
```

Use the Dockerfile:
```bash
docker build -t phalcon-kit-mkdocs .
```

Build the documentation:

```bash
docker run -e CD=true --rm -it -v ${PWD}:/docs phalcon-kit-mkdocs build
```

Start a local development server to view the documentation:

```bash
docker run -e CI=true --rm -it -p 8000:8000 -v ${PWD}:/docs phalcon-kit-mkdocs
```

Open your web browser and visit http://localhost:8000 to view the documentation.

## Contributing

Contributions to the documentation are welcome! If you would like to contribute, please fork the repository, make your
changes, and submit a pull request. Refer to
the [Contribution Guidelines](https://github.com/phalcon-kit/core/blob/master/CONTRIBUTING.md) for more information.

## License

This documentation is licensed under
the [BSD 3-Clause License](https://github.com/phalcon-kit/core/blob/master/LICENSE.txt). You are free to use, modify, and
distribute the documentation as per the terms of the license.
