# Project 4: Continuous Delivery of FastAPI Data Engineering API on AWS

## Project Description:

The goal of this project is to create a microservice that returns a JSON payload and performs a data enginerring related task. Then push tested code to GitHub and perform Continuous Integration with Github Actions. Configure Build Servicer to Deply changes on build as Continuous Delivery. And finally, create a realistic API. 

I have built an API that randomly drafts an NBA team based on data of player statistics from last season (2021). The API was built on FastAPI and returns a JSON payload. It also has additional functions that let you sub out certain positions from your team and recalculate team statistics. I have employed Github actions for continuous integration and hosted a version of the API on AWS AppRunner (currently paused). Any changes made to the API will be updated and seen on the version in AWS AppRunner. 

![app-deploy-lifecycle](https://user-images.githubusercontent.com/55010363/205759076-99d97788-8f80-44ae-b38a-eb5ae216edcd.png)



