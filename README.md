# When2STEM:  automated scheduler for a student club

## Description

For the context, Fulbright STEM Club need to find common free time of the members for club meeting. Therefore, we collect data of (1) courses that members take and (2) schedule of all courses. Then we run algorithm to find the common free time slots. This repo contains the code for those tasks.

## Installation

### For beginners (using Thonny)

1. In Github, download the code by clicking in `Code` and `Download ZIP`. (like [this](https://github.com/npnkhoi/When2STEM/blob/master/assets/how%20to%20download%20code.png))

2. Install the libraries

   We will install 2 packages: `selenium` and `pandas`. For each of these, in Thonny, go to `Tools -> Packages` and search the name of each package, then install them.

3. You're done. Now move to the **Execution** part.

### For pros

1. Clone this repo

2. Install packages:

* In your terminal, `cd` to this project folder
* `pip install pipenv` (for package management)
* `pipenv install` (automatically install all required packages shown in `pipfile.lock`)

### For both

1. Download the appropriate driver of your web browser. For Chrome, go to https://chromedriver.chromium.org/.

2. Create a env.py file following the format of env_sample.py. This file contains 3 things: the location of the driver, your outlook username and password.

## Execution

1. Launch `main.py` in your favorite way. For Thonny, click `Run` (or press `F5`). 
2. Accept any pop up about permission blabla. There's no virus here.
3. Enjoy the automation!

![when2stem demo](https://github.com/npnkhoi/When2STEM/blob/master/assets/when2stem_demo.gif)
