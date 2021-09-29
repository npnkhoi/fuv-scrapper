# When2STEM:  Course information scrapper at Fulbright University Vietnam.
## Installation

1. Clone this repo
2. Install packages:
* In your terminal, `cd` to this project folder
* Run `pip install pipenv` (install `pipenv` for package management)
* Run `pipenv install` (automatically install all required packages)
3. Download the appropriate driver of your web browser, put it into this project folder. For Chrome, go to https://chromedriver.chromium.org/.
4. Run `cp env_sample.py env.py`, then edit the content of `env.py`. This file contains 3 things: the location of the browser driver (step 3), your Outlook username and password.

## Execution
1. Run `pipenv shell` -> activate virtual environment.
2. Run `python -m src.main`
3. Enjoy the automation!