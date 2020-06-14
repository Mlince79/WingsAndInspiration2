# Wings And Inspiration 3 Data-Centric Development Milestone Project- Code Institute

This project is a continuation of the second milestone. The reasons for my decision to continue with the previous development are:
 Improve my result; I did not get a good outcome on several topics. Having a work that was not good enough to be presented as part of my portfolio is something I was unwilling to keep. So I decided to check the weak areas and learn from that improving them. 
Create the areas that were missing. The Blog section was missing, and I saw that the requirements for this milestone fit very well. 
I have added an SQLAlchemy Flask project for a web application that allows users to store and manipulate data records about a particular domain. 
I did get the recommendation from my mentor to do it with MONGO DB. Nevertheless, I was very interested in learning and applying the SQLAlchemy; I find it very easy and appealing. In our last revision, he was ok with it. 
This website will offer all women the opportunity to get in contact with a great companion. Under the umbrella of Wings and Inspiration project, Denisse will provide her Coaching to help them adapt to their new country the best way and live their Expat life to the fullest.

## UX
She started her website on WordPress but struggled and did not get it the way she wanted. She did not have a clear objective of what she wanted to accomplish with her site.
Her original website check [here](https://github.com/Mlince79/WingsAndInspiration/blob/master/uxStrategy/Original%20home.jpg).

Denisse has a personal call, and she is passionate about helping women. She wants to teach them to find their inner purpose. 
Through Yoga exercises and meditation, she helps them to listen to something higher than their thoughts. 

Going through this process is like going through the process of becoming a butterfly. 

Denisse will be close to every single woman all the way long, and the blog section's idea is to create a safe space to share and inspire other women. 

### Website design and style :
- Approachable
- Caring
- Natural/Organic
- Helpful

The design is by Marcela Ruiz Barba, a professional illustrator https://www.instagram.com/marcelatepetonga/

## Features
- The users will be able to book a session from the home website section and with all the other pages. 
- Social media contacts will be present within all the sections. 
- In the blog section users would be able to:
    * Register
    * Login
        - Remember me option will be not working at the moment. 
        - Forgot password would be not working later.
    Once the user is login will be able to:
        - Create a new post
        - Update their account:
        - Change the username, email, and default picture. 

    The post will display up to 5 posts per page. 

### Existing Sections

The scope level in phase 2 will be:
- Home - where the user can read a callout and book a first 30 min free session.
- About Me - the user will get to know Denisse's biography.
- My Coaching - the user will get to know about Denisse's Coaching.
- The blog - is a space for women to share their journey.


### Sections Left to Implement

- Events - will describe whats a women's circle and, in the future, will display a calendar with events showing the map of Stockholm and the place.


## Technologies
- HTML
- CSS
- Bootstrap (3.3.7)
- Javascript
- EmailJS.com
- Flask
    - Flask-Bcrypt
    - Flask-Login
    - Flask-Mail
    - Flask-SQLAlchemy
    - Flask-WTF
- Python
- itsdangerous
- SQLAlchemy
- WTForms


## Testing
HOME 
    - Page responsive on laptop, ipad and phone considering a good layout of:
        - javascript message
        - navbar
        - image
        - social media
        - book session button
    - Funtionality of (this was check on all single page):
        - book session button
        - social media links 
        - navbar links 
ABOUT ME 
    - Display photo and text
MY COACHING 
    - 


All links will open in a new tab using 'target="_blank"'

It is a responsive website.
This site tested across multiple browsers (Chrome, Safari, Internet Explorer, FireFox) and on various mobile devices (iPhone 4, 5, 7: Chrome and Safari, iPad, Samsung Galaxy)

HTML and CSS code were both validated at the following pages:
- https://validator.w3.org/#validate_by_uri+with_options
- https://jigsaw.w3.org/css-validator/

The test was conducted on gitpod and then on github. 

## Deployment

This site is hosted using GitHub pages, deployed directly from the master branch. 
1: GitHub repository
2: click on the Settings tab at the top
3: scroll down to GitHub Pages
4: select 'master' branch from the drop-down
5: page should reload.
6: scroll down again to GitHub Pages
7: allow about 1-2 minutes for GitHub to build the site, but you should have the link available there now.

To run locally, the user can clone this repository directly into the editor of their choice by pasting git clone https://github.com/Mlince79/WingsAndInspiration.git into their terminal.

## Credits
Syed mohamed aladeen https://stackoverflow.com/questions/56800892/how-to-make-javascript-code-loop-to-repeat-text for the HOME animation loop
I got the code from https://repl.it/@ArnavBulani/OutlandishEnragedTechnician for the quiz
https://favpng.com/ For the background image in the quiz


### Content
- The sections were planed based on the exercises done on the course.

### Media
- The photos used in this site are from the owner of the project.

### Acknowledgments

- I have received inspiration for this project, Denisse Olsson, Mentors and Tutors from Code Institute. Expericed developers as Syed Mohamed Aladeen, Arnav Bulani.
