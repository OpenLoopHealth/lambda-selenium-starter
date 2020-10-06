# Lambda Selenium Starter
A simple starter for headless chrome + selenium webdriver in AWS Lambda using Python.

Lambda Selenium Starter provides a framework for seamless development & deployment of web scrapers, for any webpage, to AWS Lambda. To dive right in, check out [Quick Start](#quick-start). Otherwise, visit the Wiki for a more detailed guide.

## How does it work?

This starter was primarily developed in inspiration of the 21 Buttons [guide](https://engineering.21buttons.com/crawling-thousands-of-products-using-aws-lambda-80332e259de1)/[repo](https://github.com/jairovadillo/pychromeless/).

Technologies used are:
* Python 3.6
* [Selenium](https://www.selenium.dev/)
* [Chrome driver](https://sites.google.com/a/chromium.org/chromedriver/)
* [Small chromium binary](https://github.com/adieuadieu/serverless-chrome/releases)
* [Docker](https://docs.docker.com/engine/installation/#get-started)

## How is this unique?

Using this starter, you can develop, test, and write your selenium web scrapers nearly identically to how you would do so without AWS Lambda functionality. This starter makes it possible to develop your selenium web scrapers without learning much about the technologies involved.

## Requirements

Install docker and dependencies:

* `make fetch-dependencies`
* [Installing Docker](https://docs.docker.com/engine/installation/#get-started)
* [Installing Docker compose](https://docs.docker.com/compose/install/#install-compose)

## Quick Start

1. Clone this repo

2. Look at the current scraper in `lambda_function.py`: it navigates to Google and prints some messages.

3. Modify `lambda_function.py` to perform your desired actions (using selenium as you normally would). There are two importance differences: make sure your functions accept the **driver** instance if you need to perform selenium related actions. Make sure your main function call comes from `lambda_handler`.

4. Add any additional dependencies to `requirements.txt`

## Testing locally

Test your web scraper locally with: `make docker-run`. It's highly suggested you test locally before packaging it up to AWS - it's much easier to debug locally! Check out the possible other commands in the `Makefile`

## Building and uploading the distributable package

Once you're ready to upload to AWS, do the following:

* `make build-lambda-package`
* Upload the `build.zip` resulting file to your AWS Lambda function (typically this will involve using S3)
* Set Lambda environment variables (same values as in docker-compose.yml)
    * `PYTHONPATH=/var/task/src:/var/task/lib`
    * `PATH=/var/task/bin`
* Adjust lambda function parameters to match your necessities, for the given example:
    * Timeout: +10 seconds
    * Memory: + 250MB
* Invoke your function using the AWS CLI `aws lambda invoke --function-name YOURFUNCTIONNAME out --log-type Tail`

## Example

To view what modifications a slightly larger web scraper might involve, check out this [gist](https://gist.github.com/noahsburroughs/37f5746ea55f0bc9a9228cea164fec52)

## Shouts to
* [PyChromeless](https://github.com/jairovadillo/pychromeless/)
* [Docker lambda](https://github.com/lambci/docker-lambda)
* [Lambdium](https://github.com/smithclay/lambdium)
* [Serverless Chrome repo](https://github.com/adieuadieu/serverless-chrome) & [medium post](https://medium.com/@marco.luethy/running-headless-chrome-on-aws-lambda-fa82ad33a9eb)
* [Chromeless](https://github.com/graphcool/chromeless)