# NestHumidity
Update Nest Thermostat Humidity based on outsite temprature automatically.  

Based on the Nest API written by FiloSottile here: https://github.com/FiloSottile/nest_thermostat

Takes the future weather or current temperature and updates your Nest thermostats humidity.  A feature lacking in the stock firmware.  

This was also written to run out of AWS lambda.  You can replace the username/password fields with strings to run locally and add in the min/max/multipier variables too.

I only tested this to add humidity to the air in cold weather.  You could probably use it to dehumidify but you would need to adjust the variables.
