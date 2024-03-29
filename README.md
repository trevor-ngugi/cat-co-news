# cat-co-news

## Author
[tevor ngugi](https://github.com/trevor-ngugi), 

## Versioning
cat-co-news version 1.0
Future releases should have the following features:
* Ability to search news.
* Ability to favorite specific articles
* Pagination.

## Description
An application which lists and previews news articles from various sources using the [News API](https://newsapi.org/), made by python web framework, Flask.

## Features
Here are the features in summary:
* A minimalistic landing page showing trending world news and a variety of news sources
* Clickable news sources which direct the user to a page with article highlights from the particular source.

## Behaviour Driven Development (BDD)
|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
|Page loads, user arrives in the landing page, is greeted to a list of all available news sources.                        |  The user can click on any particulr list group item to be directed to a separate page containing news highlights curated by the same publisher.          | On clicking the "read more" button, the user is redirected to the main article to read the full story.    |                       |

## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
* Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
* Example: 
    * **`pip install flask`**

## Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/trevor-ngugi/cat-co-news.git`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`pip install virtualenv`**
    * **`virtualenv venv`**
    * **`source venv/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Download the all dependencies in the requirements.txt using **`pip install <name>`**
* **Step 5** : Go to the [news API]() WEBSITE, sign up for a free account and generate an API key. 
    * Create a file in your root directory called start.sh and store the API key like so **`export API_KEY="<your-key>"`**
    * On the same file write down the command **`python3 manage.py server`** 
* **Step 6** : On your terminal, run the following command, **`chmod a+x start.sh`**
    * You can now launch the application locally by running the command **`./start.sh`** 
    * Open your preferred browser and view the app by opening the link **http://127.0.0.1:5000/**.

## Known Bugs
* Not able to deploy to heroku 

## Technologies Used
* Python 3.7.4
* HTML  
* CSS
* Animate.css
* MDB 4.8.10

## Support and contact details
You can provide feedback or raise any issues/ bugs through the following means:
* ngugitrevor@gmail.com



## License
MIT License

Copyright (c) [2020] [trevorngugi]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

