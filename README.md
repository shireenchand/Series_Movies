# Series_Movies  
This repository contains 3 different scripts using the TMDb api:  
• Upcoming Movies  
• Similar Movies  
• Similar TV Shows  

Here is the official API Documentation of TMDb ---> https://developers.themoviedb.org/3/getting-started/introduction

### Contents of this README:  
- [How to get TMDb API Key](#how-to-get-tmdb-api)
- [Upcoming Movies](#upcoming-movies)
- [Similar Movies](#similar-movies)
- [Similar TV Shows](#similar-tv-shows)  

## How to get TMDb API Key  
First you need to make an account in TMDb  
Go here -----> https://www.themoviedb.org  

Click on Join TMDb if you don't have an account. If you do, then click on Login and fill your details.

![Screenshot 2021-02-26 at 8 05 22 PM](https://user-images.githubusercontent.com/72601697/109314926-f316e900-786f-11eb-959a-a7b5d9598aac.png)  

If clicked on Join TMDb fill in the fields and click on Sign Up.

![Screenshot 2021-02-26 at 8 24 31 PM](https://user-images.githubusercontent.com/72601697/109315588-b26b9f80-7870-11eb-8455-db87e751f720.png)  

Now it may tell you to verify your mail, so do that.  

On your dashboard, there is an option to see your profile and settings click on that.


![Screenshot 2021-02-26 at 8 31 23 PM](https://user-images.githubusercontent.com/72601697/109316690-e2677280-7871-11eb-8eca-bd667c979865.png)

Then click on the Settings option. After clicking on that, there is a list of options. Select the one that says API. 

![Screenshot 2021-02-26 at 8 34 00 PM](https://user-images.githubusercontent.com/72601697/109316859-0cb93000-7872-11eb-9fe4-ecfb09625465.png)  

After that you get an option to request an API Key. Fill the required details. The API is free only for developer use and not commercial use. If you want to use for commercial use, then you will have to pay.(**NEVER SHARE YOUR API KEY WITH ANYONE**)  

Once you get the API Key, you are good to go.  
Note: These scripts use version 3 of the API. So make sure to use the v3 API key.  


## Upcoming Movies  

This script gives you a list of Upcoming Movies.  

##### Changes you can make:  
In line 11, intialize "api_key" to your API Key.  
In line 10, you can change your region, but these are the rules according to the documentation - "Specify a ISO 3166-1 code to filter release dates. Must be uppercase." Here is a link to the ISO 3166-1 code of each country --> https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes  

Now you are good to go. Once you run the program, you get output like this.  
![Screenshot 2021-02-26 at 7 40 15 PM](https://user-images.githubusercontent.com/72601697/109320263-d5e51900-7875-11eb-96c6-82065f553f23.png)  

![Screenshot 2021-02-26 at 7 40 40 PM](https://user-images.githubusercontent.com/72601697/109320303-e1d0db00-7875-11eb-8fe2-bf2843f82024.png)

## Similar Movies  

This script gives a list of movies similar to the one you entered.  

##### Changes you can make:  
In line 10, intialize "api_key" to your API Key.  

Now you are good to go. Once you run the program, you get output like this.  
![Screenshot 2021-02-26 at 9 07 07 PM](https://user-images.githubusercontent.com/72601697/109321020-b0a4da80-7876-11eb-8783-70abdd7b4ca0.png)  

![Screenshot 2021-02-26 at 9 07 22 PM](https://user-images.githubusercontent.com/72601697/109321055-bbf80600-7876-11eb-95d5-523c0a53b416.png)  

## Similar TV Shows  

This script gives a list of series similar to the one you entered.  

##### Changes you can make:  
In line 10, intialize "api_key" to your API Key.  

Now you are good to go. Once you run the program, you get output like this.   
![Screenshot 2021-02-26 at 9 16 41 PM](https://user-images.githubusercontent.com/72601697/109322172-fada8b80-7877-11eb-8268-4d8d999c0688.png)  

![Screenshot 2021-02-26 at 9 16 50 PM](https://user-images.githubusercontent.com/72601697/109322265-18a7f080-7878-11eb-8357-0e8294b594fe.png)  

## Conclusion  

The 3 scripts also use an amazing module called Texttable which allows to print data in a nice, neat table. Also the pprint module was used just to pretify the json data.  
Hope you enjoy using these scripts cuz I personally love them and use them a lot. If you do like it, don't hold back from giving it a star ⭐️.


