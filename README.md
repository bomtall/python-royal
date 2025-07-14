# Python Royal

[![Project management: uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)  
[![Code style & Static analysis: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)  
[![Type check: Mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)  
[![Pipeline status](https://gitlab.com/jgaffiot1/python-royal/badges/app-demo/pipeline.svg)](https://gitlab.com/jgaffiot1/python-royal/-/commits/app-demo)  
[![Coverage report](https://gitlab.com/jgaffiot1/python-royal/badges/app-demo/coverage.svg)](https://gitlab.com/jgaffiot1/python-royal/-/commits/app-demo)  
[![Latest release](https://gitlab.com/jgaffiot1/python-royal/-/badges/release.svg)](https://gitlab.com/jgaffiot1/python-royal/-/releases)

## Description

Support material for the Python Royal workshop at SnowCamp 2025.

## Objectives

Learn how to write stylish and robust Python code!

Python has a reputation for not being focused on software quality.  
That may have been true 20 years ago, but today, major companies are built on this language:  
Instagram, Spotify, Reddit, Dropbox...

To achieve **reliability**, **maintainability**, **scalability**, and **security** (i.e., true *quality*), you need to understand how the language and its ecosystem work.

Let’s discover together the structure of a Python project, the language principles to follow, the tools to set up, and the practices to adopt in order to work with Python at an industrial level of quality.

## Prerequisites

- Basic knowledge of Python  
- Ability to install software on your machine (network access and permissions)  
- A shell/terminal  
- Ideally, a GitLab or GitHub account  

## Workflow

This repo includes X/gamma ray detector files — let’s display them!

- [ ] Fork the project on [GitLab](https://gitlab.com/jgaffiot1/python-royal)  
      or [GitHub](https://github.com/Lenormju/python-royal) to your personal account  
- [ ] Clone your fork to your local machine  
- [ ] Install `uv`  
- [ ] Initialize a new project with `uv`  
- [ ] Fill in the `pyproject.toml`  
- [ ] Add a dependency: [Streamlit](https://streamlit.io/)  
- [ ] Display the Streamlit Hello World  
- [ ] Add more dependencies: `pandas` and `plotly`  
- [ ] Load a file and display a plot with Streamlit  

Now for some tooling.

- [ ] Install `ruff`, `mypy`, and `pytest` as dev dependencies  
- [ ] Format your code with `ruff`  
- [ ] Analyze your code with `ruff`  
- [ ] Check types with `mypy`  
- [ ] Write a test using `pytest`  
- [ ] Integrate these practices into your IDE/workflow  

Let’s publish this code.

- [ ] Create a release and tag it on Git(Hub|Lab)  
- [ ] Build a package (both `sdist` and `wheel` formats) with `uv`  
- [ ] Integrate the tag into the package using `versioningit`  
- [ ] Publish the code to Git(Hub|Lab)'s package registry  
- [ ] *(Optional: Build a Docker image containing the code and publish it)*  

Let’s automate things a bit.

- [ ] Run checks before committing using `pre-commit`  
- [ ] Standardize the workflow with `Doit` (or even `Make`)  
- [ ] Trigger automatic checks using GitLab CI / GitHub Actions  

And of course, document everything.

- [ ] Install `sphinx` as a dev dependency  
- [ ] Build the base of your documentation  
- [ ] Extract docstrings and integrate them using `apidoc`  

Continue developing the app as far as possible!

- [ ] Add a field to load a data file  
- [ ] Extract acquisition time and display curves in impacts/second  
- [ ] Add a peak-search page for the curves  
- [ ] Calibrate the curves in energy using reference curves  
  (Na22, Cs137, Co60)  
- [ ] Refactor by separating display, data reading, and processing  
- [ ] Store calibration values in the app state and apply them to all curves  
- [ ] Add an optional field to load a second file to subtract from the first  
- [ ] Adjust colors, add a logo (optional CSS styling)  

## Data

The data comes from an X-ray and gamma radiation sensor (gamma being the more energetic version of X-rays), used to measure residual radioactivity in samples that are hopefully very pure — so, with very low levels of radioactivity.

It works similarly to solar panels, but instead of being exposed to tons of optical photons, it receives just the occasional X-ray or gamma photon.  
The sensor doesn't output a continuous current like a solar panel; it produces small spikes each time a photon hits it.  
The height of each spike gives us the energy of the impacting photon.

However, the sensor records these spike heights in a very raw format:  
It simply counts the height levels on a scale from 1 to 16,384. These aren’t even volts or energy units, just ADC (analog-to-digital converter) channels encoded on 14 bits (16,384 = 2¹⁴).  
Because the sensor only counts impacts, we must manually consider the recording time to determine how radioactive a sample is (e.g., how many impacts in one hour?).

To retrieve the energy scale, we place known radioactive elements in front of the sensor — we know the expected energy of their peaks (in keV, a unit of energy):

- Cobalt 60 (Co60): 2 peaks at 1173.2 keV and 1332.5 keV  
- Sodium 22 (Na22): 2 peaks at 511 keV and 1274.5 keV  
- Cesium 137 (Cs137): 1 peak at 661.7 keV  

Also, the X or gamma photons can come from either the sample or the environment, which is always slightly radioactive.  
To account for this, we subtract the environmental measurement (called **background**) from the sample’s measurement.  
We have measurements for two samples: `"pmt"` and `"steel"`, and two background measurements: `"bkg"` and `"bkg2"`.

**Time to code!**
