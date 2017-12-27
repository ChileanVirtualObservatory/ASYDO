﻿

# ASYDO (Astronomical Synthetic Data Observations) #

The objective of this project is to generate synthetic cubes of spectral data, similar to those that ALMA generates.

Authors:

 * Mauricio Araya
 * Teodoro Hochfärber


## Introduction ##
The size and quantity of the data that is being generated by large astronomical projects like ALMA, requires a paradigm change in astronomical data analysis. Complex data, such as highly sensitive spectroscopic data in the form of large data cubes, are not only difficult to manage, transfer and visualize, but they also turn unfeasible the use of traditional data analysis techniques and algorithms. Consequently, the attention have been placed on machine learning and artificial intelligence techniques, to develop approximate and adaptive methods for astronomical data analysis within a reasonable computational time.

### The Problem ###

Unfortunately, these techniques are usually sub-optimal, stochastic and strongly dependent of the parameters, which could easily turn into "a ghost in the machine" for astronomers and practitioners. Therefore, a proper assessment of these methods is not only desirable but mandatory for trusting them in large-scale usage. The problem is that positively verifiable results are scarce in astronomy, and moreover, science using bleeding-edge instrumentation naturally lacks of reference values.

### Our Proposal ###

We propose an Astronomical Synthetic Data Observatory (ASYDO), a virtual service that generates synthetic spectroscopic data in the form of data cubes. The objective of the tool is not to produce accurate astrophysical simulations, but to generate a large number of labeled synthetic data, to assess advanced computing algorithms for astronomy and to develop novel Big Data algorithms. The synthetic data is generated using a set of spectral lines, template functions for spatial and spectral distributions, and simple models that produce reasonable synthetic observations. Emission lines are obtained automatically using IVOA's SLAP protocol (or from a relational database) and their spectral profiles correspond to distributions in the exponential family. The spatial distributions correspond to simple functions (e.g., 2D Gaussian), or to scalable template objects. The intensity, broadening and radial velocity of each line is given by very simple and naive physical models, yet ASYDO's generic implementation supports new user-made models, which potentially allows adding more realistic simulations. The resulting data cube is saved as a FITS file, also including all the tables and images used for generating the cube. We expect to implement ASYDO as a virtual observatory service in the near future.


## Downloading and Installing ##

ASYDO is a free software (GPL) mostly in Python by the LIRAE group. Any contribution, including comments, ideas, criticism, code or complains are very welcome.
ASYDO's development is managed by GitHub's [ChileanVirtualObservatory platform](https://github.com/ChileanVirtualObservatory/ASYDO) . Feel free to contact us through GitHub!

### Getting the sources

For obtaining the ASYDO source code you can download it via web (Download ZIP link), or you can download the repository using git:

> git clone https://github.com/ChileanVirtualObservatory/ASYDO.git

The current version of the development branch is `0.1.2`

### Installing

Currently we have the following installation methods:

 * pypi package:

    Install with the command `pip install asydo-dev` and it will resolve all the dependencies automatically.

 * conda package:

    TODO

This will also install a `dbCreator.py` script that we will use in the next step.

### Database ###

To create the database, run `dbCreator.py` in your terminal. By default, this it will download a .csv from our server, and import it to a SQLITE database.

If you want to import your spectral lines, we currently support 2 ways of doing this:
  * By Custom `file.csv`: To use this option, you must run `dbCreator.py -C /path/to/file.csv`

  * By Query to a `SLAP` service: To use this option, you must run `dbCreator.py -T [ServiceURL]`

By default, the script will download the lines in range from **88 Ghz to 720 Ghz** (the ALMA spectral Band)

If you want to use a custom range you must add to the previous instruction: ` -R minfreq:maxfreq`
