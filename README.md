# [Calisthenics Project](https://calisthenics-project.herokuapp.com/)
The main purpose of this project is to motivate people to a healthier lifestyle through information, training videos and images.
Users will have the possibility to interact with the data-driven web application enabling them to carry out basic
CRUD(**C**reate, **R**ead, **U**pdate, **D**elete) functionalities.




## UX

Users are welcome to the main page with a video introduction on what calisthenics can look like.
Information is displayed and you can click on "Read More" if youre visiting through mobile or tablet, desktop version
shows the entire paragraph.

This web application consists of three main colored icons, **View Programs**, **Add Programs** and
**Exercises**. These icons can be found on the home page, they will redirect
the user to their choice of option.

#### Wireframes/Mockups

* [Mobile Home](https://github.com/Ario124/calisthenics-project/blob/master/wireframes/mobile_home.png)
* [Mobile Programs](https://github.com/Ario124/calisthenics-project/blob/master/wireframes/mobile_add_program.png)
* [Mobile Exercises](https://github.com/Ario124/calisthenics-project/blob/master/wireframes/mobile_exercises.png)
* [Tablet Home](https://github.com/Ario124/calisthenics-project/blob/master/wireframes/tablet_home.png)
* [Desktop Home](https://github.com/Ario124/calisthenics-project/blob/master/wireframes/desktop_home.png)
* [Desktop Add Programs](https://github.com/Ario124/calisthenics-project/blob/master/wireframes/desktop_add_program.png)
* [Desktop View Programs](https://github.com/Ario124/calisthenics-project/blob/master/wireframes/desktop_view_programs.png)
* [Desktop Exercises](https://github.com/Ario124/calisthenics-project/blob/master/wireframes/desktop_exercises.png)
* [Desktop Contact](https://github.com/Ario124/calisthenics-project/blob/master/wireframes/desktop_contact.png)


#### User Stories

* As a user I can navigate through the menu and click on the different pages displayed on the navigation bar.
* As a user I can access basic information about Calisthenics through the main home page.
* As a user I am presented with a video that gives me an introduction to the site content.
* As a user I can click on **View Programs** to access a list of programs.
* As a user I can click on a program to extend it, and get more information about that particular program.
* As a user I am able to click on a video link that redirects me to Youtube for further demostration.
* As a user I have the possibility to **C**reate, **R**ead, **U**pdate and **D**elete a program.
* As a user I can click on "Exercises" to get more information about basic exercises and expert level exercises.
* As a user I can find the "Contact" page easily, through the navigation bar.
* As a user I can click on the "Calisthenics" title or Home icon to return to the main page.

## Features

#### Website features

These are all of the features that will be available for any visitor.

* Users are able to use the "burger" icon as a way to bring up the navigation (Mobile & Tablet only).
* Users can easily browse through the website and go back by clicking on the button "back" that is at
the bottom of the page.
* Users can enjoy the styles that were evenly applied throughout the website.
* Users can click on the Github Icon by the footer, This will redirect the user to my github.


#### CRUD features

These are the features that users can interact with.

* Users can Create programs.
* Users can Read programs.
* Users can Update programs.
* Users can Delete programs.
* Users can also submit a youtube link while making a program, this will be displayed when reading the program.

#### Features that can be implemented

* Login system, where users can register and use their own account.
* Possibility to add categories
* Vote system, to give users the oportunity to give a thumbs up or thumbs down.
* Option to change the style (color) of the programs created.


## Technologies used

This web application uses the following technologies:

* [HTML](https://www.w3schools.com/html/) - I have used HTML to put everything in place, It was used to build the structure and content.
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - The use of CSS came into play when styling the web application, I focused on
 making sure to keep the styles clean and even to give a good lively experience. 
* [Javascript](https://www.javascript.com/) - The Javascript used was mostly to interact with Materialize and to interact with the navigation
 bar on scroll.
* [Materialize CSS](http://materializecss.com) - The structure and layout of the web application was accomplished through the use of Materialize CSS.
* [Python](https://www.python.org/) - Most of the logic comes from the backend use of Python. 
* [Flask](https://palletsprojects.com/p/flask/) - I used Flask to render templates and handle the routing.
* [Google Fonts](https://fonts.google.com/) - The use of Google Fonts was mainly for the Icon used on the footer.
* [Heroku](https://www.heroku.com/) - The deployment and host of this project was done through Heroku.
* [Github](https://github.com) - I used Github to add & commit my changes, and push to my main page.
* [Balsamiq Mockups 3](https://balsamiq.com/) - Mockups were made from the use of Balsamiq Mockups 3.
* [MongoDB Atlas](https://www.mongodb.com/) - The Database structure for this project was created through MongoDB Atlas.


## Testing

These tests below are to confirm that the website is working fine, and that it has been properly tested
to avoid bugs and errors.

Tests mainly for devices:

* Samsung Galaxy S8 & S9
* Iphone 6/7/8
* Tablet devices
* Desktop

On the following browsers:

* **Google Chrome**
* **Mozilla Firefox**
* **Microsoft Edge**
* **Internet Explorer**

#### Testing website

User Stories:

1. Load the home page and verify that the video is automatically played with sound muted.
2. Verify that the navbar dissapears when scrolling down and reappears when scrolling up, should work on any of the pages available.
3. Load the web application on Google Chrome, open Dev tools to check if there are any errors showing up.
4. Load the web application on Chrome and try different resolutions through Dev tools to verify that the website is responsive on different resolutions.
5. Verify that the color of the navigation bar and footer changes to indicate different resolutions.
6. Verify that the Favicon is working and is shown on the tab once the web application has been loaded.
7. Load index.html and make sure that the 3 icons **View Programs**, **Add Program** and **Exercises** are working properly by clicking,
 This should redirect the user to the chosen page.
8. Load the home page on mobile or tablet resolution and check to see that there is a "Read More" button that expands on click. 
This should only be shown on these resolutions and not on desktop.
9. Load any page on mobile or tablet resolution to see if the navbar is responsite to the resolutions, the 'hamburger' icon should be shown.
10. Verify that the navbar for mobile is working properly, links should be clickable and the navbar should close if needed. 
11. Navbar tabs should respond when the mouse is over, turning on a darker color to highlight the menu.
12. Load "View Programs" click on a program to activate and extend the collapsible, click again to close.
13. Load "View Programs" and scroll to the bottom, click on "Go Back" to confirm that it redirects to the previous page.
14. Load "Add Program" and click on 'Program Category' and 'Difficulty' to verify that the categories and difficulty levels are displayed.
15. Load "Add Program" and proceed to add the program without filling the forms. This should give out a warning that reminds the user that the 
forms should be filled first.
16. Verify that the program is added once the forms are filled properly.
17. Verify that the program can be edited by loading "View Programs" choosing a program and clicking on "Edit Program"
18. Verify that the program can be deleted.
19. Load "Exercises" on desktop and on mobile resolution to verify that the images not displayed the same way.
20. Load "Exercises" click on the images available, it should zoom in on click.
21. Load "Add Program" and create 3 programs with different difficulty levels, verify that this is displayed in different colors.

#### Validation

Tests to verify that the code is clean.

* **HTML** - I have used [HTML Validator](https://validator.w3.org/) and found some errors due to the fact that
the validator does not recognize Jinja. Errors such as "Bad value {{url_for('home')}}" and "Illegal character in path segment: { is not allowed."
are therefore shown.



* **CSS** - I have used [CSS Validator](https://jigsaw.w3.org/css-validator/) - No errors found.


#### Browsers



* [Google Chrome](https://www.google.com/intl/en/chrome/)
* [Mozilla Firefox](https://www.mozilla.org/)
* [Microsoft Edge](https://www.microsoft.com/en-us/windows/microsoft-edge)
* [Internet Explorer](https://en.wikipedia.org/wiki/Internet_Explorer) - problem with the video on the main page that is not displayed.

## Deployment

The project was deployed to Heroku, and it can be achieved by following these steps:

Start by cloning the project typing this:

```git clone https://github.com/ario124/calisthenics-project```

Make sure the content is located in the root of the enviroment.

Create a new application through Heroku and connect to your local repository.

**Next part has to be followed correctly**

Proceed to install all the necessary requirements for the project through the command line by typing:

```
sudo pip3 install flask
sudo pip3 install pymongo
sudo pip3 install flask_pymongo
sudo pip3 install dnspython
```
By this point it is time to add the Requirements.txt file and the Procfile by typing:

```
sudo pip3 freeze --local > requirements.txt
echo web: python app.py > Procfile
```
Note that this step has to be done **after** installing the previous requirements, if not done properly you might
encounter errors when running the app on Heroku.

If you have followed these steps correctly you can proceed to the creation of enviroment variables on Heroku
such as the MONGO_URI so they are kept hidden.

* Load Heroku and go to your application, proceed to click on 'Settings' and then click on 'Reveal Config Vars'
 This is where you can add IP, PORT and MONGO_URI variables.
* Once this is done you are ready to commit and push your changes to Heroku, use:
```git push heroku master```

If you've followed these steps incorrectly and you can't get it to work you might want to try uninstalling and trying again, if thats the case
try this:

```
sudo pip3 uninstall -r requirements.txt -y

```
At this point you can try to install the necessary requirements in the correct order.

## Media

The [video](https://www.youtube.com/watch?v=FHBtLAvNGo4) found on the main page comes from Youtube: **GRAVITAS (Simonster x Sebastian Linda)**

Filmed by: Sebastian Linda

Athlete: Simonster

Images on the 'Exercises' page come from:

[Human Flag](https://www.t-nation.com/training/how-to-perform-the-human-flag)

[One Arm Handstand](https://prioritieshapeyou.tumblr.com/image/48344192182)

[Planche](https://en.wikipedia.org/wiki/Planche_(exercise))


## Credits

* The README file was written with the help of research through [Slack](https://code-institute-room.slack.com/)
* The idea to colorize the different difficulty levels come from my tutor Juan Monetti.

### Disclaimer

The contents of this website are for educational purposes only.