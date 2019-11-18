# difs-quad

Base project for L2 DIFS TP QuaD.

Please, use the GitHub Classroom invitation link to setup your project.

# Create dev env

Run the following command: `pip install -r requirements.txt`

Restart any IDE in order to work properly.

# Run for development

Run the following command: `FLASK_ENV=development flask run`

The dev server will be listenning on the port 5000. So, open a web browser and go to the following url: `http://localhost:5000/`

# Run unit tests

Just run the following command: `pytest`

If you want to have the report coverage, we must run the following command: `pytest --cov-report html --cov=.`.
This will create a folder. In order to see the report, please open the `htmlcov/index.html` into your favorite browser.

# Run selenium tests

Must have Chrome install with the latest version.

Must have a running server on localhost:5000

Run the following command: `behave tests/features`
