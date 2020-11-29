---
id: installation
title: Installation
sidebar_label: Installation
---

multimodelity has been tested on Python 3.7+ and PyTorch 1.6. We recommend using a conda environment to install multimodelity.

## Creating a conda environment [Optional]

Assuming you have [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) installed, run:

```bash
conda create -n multimodelity python=3.7
conda activate multimodelity
```

## Install from source [Recommended]

To install from source do:

```bash
git clone https://github.com/facebookresearch/multimodelity.git
cd multimodelity
pip install --editable .
```

## Install using pip

multimodelity can be installed using pip with the following command:

```bash
pip install --upgrade --pre multimodelity
```

Use this if:

- You are using multimodelity as a library and not developing inside multimodelity. Take a look at the extending multimodelity tutorial.
- You want easy installation and don't care about up-to-date features. Note that pip packages are always outdated relative to installing from source.

Alternatively, to install latest multimodelity version from GitHub using pip, use

```bash
pip install git+https://github.com/facebookresearch/multimodelity.git
```

## Windows

If you are on Windows, run the pip install commands with an extra argument like:

```
pip install -f https://download.pytorch.org/whl/torch_stable.html --editable .
```

## Running tests [Optional]

multimodelity uses pytest for testing. To verify everything and run tests at your end do:

```bash
pytest ./tests/
```


## Contributing to multimodelity

We welcome all contributions to multimodelity. Have a look at our [contributing guidelines](https://github.com/facebookresearch/multimodelity/tree/master/.github/CONTRIBUTING.md) to get started.
