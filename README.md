# Python wrapper for the [UberDuck](https://uberduck.ai) API
This is a python wrapper for the uberduck api. You must have api access to use.

# How this works?
Well you first initialize a job by sending a request with your api key, secret, text, and voice name.\
After sending the request uberduck will issue a response with the status of the job.
So the api will poll this endpoint till a result is produced. the result is another url to the sound file that was created

Check the example.py for code

