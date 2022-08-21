# Course information scrapper at Fulbright University Vietnam
## Installation
0. `pip install pipenv`

1. Clone this repo and `cd` to this project folder.
2. Install packages:
* Run `pip install pipenv`
* Run `pipenv install` (automatically install all required packages)
3. Download the appropriate driver of your web browser, put it into this project folder. For Chrome, go to https://chromedriver.chromium.org/.
4. Run `cp env_sample.py env.py`, then edit the content of `env.py`. This file contains 3 things: the location of the browser driver (step 3), your Outlook username and password.

## Execution
1. Run `pipenv shell` -> activate virtual environment.
2. Run `python -m src.main [id]`, where `id` is the order of the target term in the dropdown list in the offering page of OneStop.
3. When the browser is at the 2FA page, you have 60s to verify it.