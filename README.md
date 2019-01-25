# raspberry-garden

## Description:  
    	Monitor the health and overall status of your garden on the go!  Do your plants need to be watered?  Is it too hot?  Too cold?  Too dry?  Too humid?  Find out all these stats all in one place!

## Tech used:  
    	Garden:  Ambient temperature sensor, soil moisture sensor, relative humidity sensor, 

## Raspberry Pi
    	Website:  Flask/Django hosted on AWS EC2, AWS Timestream(time series) or RDS PostgreSQL(relational) database, auto-deployed via AWS Elastic Beanstalk and/or CircleCI.

## Technical general concept:  
    	Using a Raspberry Pi and multiple sensors, get data about our garden in regular intervals and push it up to Amazon Timestream, which is our time series database service.  
   
	Using AWS Beanstalk, host our Flask/Django website on an EC2 instance in a fast CI/CD workflow.  
    	Our website would have a dashboard with the weather via the Dark Ski API and displays our health info about our garden that would grab data from our database in regular intervals (most likely a cron job).

### Stretch goal:   
    	Want alerts if your garden is unhealthy?  Sign up for email alerts, or text alerts via Twilio!
    	If we have lots of data, present it via Jupyter notebook.
