# A.I. Shop

Hello there! Welcome to the wonderful world of A.I. art.
There is no better place then to buy completely unique computer generated art works to have as mintable NFTs!

A live version can be found [here](https://artificial-intelligence-shop.herokuapp.com/).

# UX

This project tries to create a Django application for a NFT store service.

The website is clean and intuitive, making navigation easy. 

## User Stories

 **As a Visitor**
 - As a Visitor, I want to easily understand the main purpose of the site.
 - As a Visitor, I want to be able to view NFTs available before buying one.
 - As a Visitor, I want to be able to purchase a NFT.
  
 **As a User**
 - As a User, I want to easily understand the how to navigate through the site.
 - As a User, I want to be able to update and edit my profile.
 - As a User, I want to search all NFTs on the store.

 **As a Staff Member**
 - As a Staff Member, I want to easily understand the how to navigate through the site.
 - As a Staff Member, I want to be able to update and edit my profile.
 - As a Staff Member, I want to search all NFTs on the store.
 - As a Staff Member, I want to edit categories, courses and lessons through the admin panel.

## MVP

✅ Fully responsive.<br>
✅ Purchase a NFT. <br>
✅ Register a new account and login.<br>
✅ Edit profile. <br>
✅ Staff users can create and edit categories, products. <br>


### Existing Features

- **New Account** <br>
To access the page the user must first create a new account by clicking on the "Signup" link on the navbar or button on landing page form. Will receive an e-mail verification on creation.

- **Login** <br>
To access the page the user must use their credentials to login. In the case of this build there is also an option to login as a "Demo User" or "Demo Staff" which allows the user experience the application utilizing a premade account. (refer to testing section) 

- **Profile** <br>
Shows your account information such as username, name, email and pre saved delivery options.

- **Edit Profile** <br>
Allows the user to close or edit account information such as name, email, password and delivery options.

- **NFT Category** <br>
NFTs are divided into different categories. 

- **Mintable NFTs** <br>
NFTs that are avalibile for users to purchase and sell else where. Known as 'mintable', which is referred to as avalibile to flip for profits. 

- **Prints** <br>
Prints of such NFTs, not as exclusive as it is made from paper. For site purposes and lack of product fixtures, the developer re-used some of the NFT data to act as prints also, so not as well presented.


## Design
The whole UI is made utilizing Bootstrap 4. For further information, please refer to the official documentation [here](https://getbootstrap.com/docs/4.0/getting-started/introduction/).


## Technologies Used

Throughout the project, the following technologies were used.

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [jQuery](https://jquery.com/)
- [Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
- [Stripe](https://stripe.com/en-ie)

	 
## Testing
Detailed tests can be found attached to this repo. 

## Test Accounts
For testing purposes these accounts can be used (admin + testerforai). Or feel free to create your own.

### Regular user
- Username: testerforai
- Password: tester123

### Staff user
- Username: admin
- Password: superuserpass


## Deployment

The website is hosted and deployed by [Heroku](https://www.heroku.com/home).
Everything is deployed from the master branch and updates automatically whenever the branch is updated in GitHub.

1.  Log in Heroku (or create a new one if you don't have one.);
2.  Go to your dashboard.
3.  Click on the "New"  -> "Create new app" button located right under the navbar.
4.  Choose a unique name for your app.
5.  Choose a region (preferably close to where you are located).
6.  If everything works fine you should see the overview page of your app.
7.  Click on Settings tab.
8.  Reveal Config vars.
9.  Here we configure the SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, DATABASE_URL, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, EMAIL_HOST_USER, EMAIL_HOST_PASS, USE_AWS values (thoose are  not public and are the same values on my env.py file(which is also private)).
10. Click on deploy tab.
11. In the case of this project I chose to conect my app to my repository in GitHub, so it auto updates my heroku app whenever the project is pushed. 
12. Click on the Deploy Branch button. 
13. DONE!

### Forking
If you want to fork the repository to your own GitHub account you can by clicking on the “fork” button under the navbar with your profile.

### Cloning

 1. If you want to clone the repository into a local file you can by:
 2. Clicking on the green button “Code” and copying the url showed.
 3. Open GitBash
 4. Change directory to the desired location where you want to clone the
    files to.
 5. Type “git clone” and paste the copied URL
 6. Press enter and you should have your local file cloned and ready.
 7. After opening the folder you should create a new file in the root directory, name it env.py
 8. In env.py you can set your environment variables.  
    ```
      import os

        os.environ["SECRET_KEY"] = "<your_value>"
        os.environ["STRIPE_PUBLIC_KEY"] = "<your_value>"
        os.environ["STRIPE_SECRET_KEY"] = "<your_value>"
        os.environ["DATABASE_URL"] = "<your_value>"
        os.environ["AWS_ACCESS_KEY_ID"] = "<your_value>"
        os.environ["AWS_SECRET_ACCESS_KEY"] = "<your_value>"
        os.environ["EMAIL_HOST_USER"] = "<your_value>"
        os.environ["EMAIL_HOST_PASS"] = "<your_value>"
        # os.environ["DEVELOPMENT"] = "True" --> uncoment to use DEBUG MODE
        os.environ["USE_AWS"] = "True" --> set True or False to use AWS S3 Buckets

## Credits

### Content

- All content on the page was improvised by me, following along Code Insititutes' Boutique Ado mini project.
So credits go to https://github.com/ckz8780

### Acknowledgements

-   The wonderful tutors at C.I. but most importantly Chris Z for the mini project walkthrough.