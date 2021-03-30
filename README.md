# Ontario Schools COVID Twitter Bot

A Python bot that automatically collects, formats, and tweets the latest updated data regarding COVID-19 cases in the Ontario public schools populations.

## Motivation

After hearing from several parents and teachers, I discovered an issue where there was very little clarity regarding how protected school populations were from COVID-19. Various decisions made by the government caused further confusion and fear as parents were unaware of how safe their kids would be and staff being worried for their personal health and safety as well as their students. With Twitter being a key platform for the spread of information, especially during the pandemic, I came up with the idea to collect and publish the data for all to see and comment on.

## Technology Used

- [Plotly/Dash](https://plotly.com/): python library that can be used to create visualizations of data
- [Tweeply](https://docs.tweepy.org/en/latest/): python library that allows for access to the Twitter API
- [Twitter API](https://developer.twitter.com/en/docs/twitter-api): API for Twitter that gives detailed access to data regarding tweets and accounts
- [Ontario Data API](https://data.ontario.ca/dataset/summary-of-cases-in-schools): Data API from Ontario government that holds information including number of cases in schools, number of schools with cases, number of schools closed, etc.

## Usage

Usage requires running two scripts every day once the province releases the daily numbers at approximately 10:30 AM on weekdays. Currently, the scripts have to be run manually as the time the data becomes public is not consistent and requires manual checking.

Running the schoolsData.py script requires authentication keys provided by Twitter. If you would like to use this script, retrieve your own authentication keys from Twitter by creating a developer account. The keys should then be placed in a file (the script uses a file called "config.py") that should not be uploaded for security purposes. Once the program is able to log in, it will automatically retrieve the data from the API link, format it appropriately, and publish the tweet to the logged-in account. The tweet currently tags the province's premier Doug Ford, education minister Stephen Lecce, Ontario Health, and Ontario Education.

Refer to the image below for an example tweet.

Running the downloadSchoolData.py script will create charts using Plotly. The same data as the Twitter Bot is used to create two different charts - Total School Related Cases (line chart) and New Daily School Related Cases (bar graph). The bar graph includes a 5-day rolling average line to display a weekly trend in the number of cases. This script will also send these charts to the attached Plotly account. This account is attached in the same way as the Twitter Bot - account credentials located in a config.py file, the file being referred to in the script. The charts are then used to be tweeted out as well as added to the [website](https://ontarioschoolscovid.netlify.app/) I've created as well.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Feel free to use the program for your own region.
