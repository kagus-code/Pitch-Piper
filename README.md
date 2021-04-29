# Pitch-Piper Web App

#### This application will allow you to submit and view Pitches based on different categories , 24/04/2021

#### By **Eston Kagwima**

## Description
Imagine, you only have 1 minute to impress someone which can make or break you. Here at Pitch-Piper we provide you with an opportunity to make sure you actually say something meaningful?

This application will allow you to use that one minute wisely. You can  submit your  one minute pitches and other users will vote on them and leave comments to give their feedback on them.

The pitches are organized by category. Namely (Product,Investment and Competition)


### User stories Specification

- As a user, I would like to see the pitches other people have posted.
- As a user, I would like to vote on the pitch they liked and give it a downvote or upvote.
- As a user, I would like to be signed in for me to leave a comment
- As a user, I would like to receive a welcoming email once I sign up.
- As a user, I would like to view the pitches I have created in my profile page
- As a user, I would like to comment on the different pitches and leave feedback.
- As a user, I would like to submit a pitch in any category.
- As a user, I would like to view the different categories.




## Setup/Installation Requirements
- install Python3.9
- Clone this repository `git clone https://github.com/kagus-code/Pitch-Piper.git`
- Change directory to the project directory using  the `cd` command
- Open project on VSCode
- If you want to use virtualenv: `virtualenv ENV && source ENV/bin/activate`
- Install dependencies with pip: `pip install -r requirements.txt`
- Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app    ('development')
- Edit the export configurations `export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}`
- finally run `./start.sh`


## Technologies Used

- Python3.9
- Flask
- Flask-Bootstrap
- HTML
- CSS


## link to live site on  HEROKU

https://pitchpiper.herokuapp.com/

## Support and contact details

| Eston | ekagwima745@gmail.com |
| ----- | --------------------- |


### Known bugs 
- App May break during sign up on the deployed site due to Gmail security features that prevent heroku from signing in and sending a welcome email

### License

License
[MIT License](https://choosealicense.com/licenses/mit/)
Copyright (c) 2021 Eston Kagwima