# nba_salary_predictor

This project is meant to predict the salary of NBA players. It uses machine learning and XGBoost to come to these predictions. This project also shows how to pull data from an API and save it to an SQL database. You can submit whichever season you'd like, but I specifically chose the 2017-2018 season. The API used is https://www.balldontlie.io/

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed the latest version of the python modules requests, time, csv, xgboost, json, and jupyter notebook modules

## Installing nba_salary_predictor

To install nba_salary_predictor, simply fork the files in this repository.

## Using nba_salary_predictor

To use the nba_salary_predictor, make sure you have a salary csv file, as the API doesn't contain salaries. Compile the python files in this order:
* pull_name.py
* api_to_sql.py
* nba_salary_xgboost.ipynb

## Contributing to nba_salary_predictor

To contribute to nba_salary_predictor, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the following people who have contributed to this project:

* Andres Advincula (https://github.com/an288705)
