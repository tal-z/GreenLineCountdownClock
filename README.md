
# Making a Countdown Timer!

## Ideas for pairing:

1) Talk through options for front ends
2) Explore the relationship between a form and a countdown timer
3) Figure out how to display a countdown timer based on a user completing a form
4) Explore user accounts in Django? Make a way for users to create, log in/log out of an account, create and save timers, etc.

  - Improve the set_display() method to utilize schedule data
  - Try to find and fix the bug where predictions exist but don't get displayed
  - Code review of the javascript/html to make sure it does what I think it does
  - Build a frontend?
  - Anything else


Here are some things we need to do:
  - Get data about trains in space and time to produce arrival times.
    - Predictions
    - Schedules
    - Real-time Locations
  - Have a way to count down in seconds, from a given arrival time. This lets us keep track of time.
  - Have a way to convert time (or status) into a useful display message
   
###### Endpoint for Chestnut Hill Ave B Station predictions:
https://api-v3.mbta.com/predictions/?filter[stop]=place-chill&filter[route]=Green-B

###### Endpoint for Cleveland Circle C Station predictions:
https://api-v3.mbta.com/predictions/?filter[stop]=place-clmnl&filter[route]=Green-C

###### Endpoint for Reservoir D Station predictions:
https://api-v3.mbta.com/predictions/?filter[stop]=place-rsmnl&filter[route]=Green-D

###### MBTA Best Practices (Including for Countdown Clocks!)
https://www.mbta.com/developers/v3-api/best-practices

###### MBTA API Documentation
https://api-v3.mbta.com/docs/swagger/index.html