# E-store
<img src="static/images/logo.png" alt="Logo" width="350px" height="250px">
<br>
<br>
<img src="static/images/responsive1.png" alt="responsive" width="550px" height="350px">
<br>
:globe_with_meridians: [Live Website](https://tranquil-temple-81228.herokuapp.com/),
<br>
<img src="https://img.shields.io/badge/github-%23181717.svg?&style=for-the-badge&logo=github&logoColor=white" /> [Github repository](https://github.com/bmcdonald2000/e-commerce)

## What is E-store ? :bulb:
E-store is a fictional e-commerce sports retailer based in England. Founded in August 2022, E-store specialises in buying high quality sporting goods and selling them at affordable prices online. 

As this website is for educational purposes the credit card payment functionality is not set up to accept real payments. You will need to use stripe testing details if you are testing interactively, feel free to use card details below. Further information can be viewed via [Stripe documentation](https://stripe.com/docs/testing) test page. 

4242424242424242 (Visa)
Expiration date = Any future date (Example: 12/27)
CVN = any 3 digits (Example: 592)
Postcode = any valid 8 characters (Example: SE25 4EX)

<img src="static/images/payment.png" alt="responsive" width="350px" height="150px">

<details>
<summary><strong>Table of contents:</strong></summary>
<br>

[User Experience (UX)](##-user-experience-(UX))

[Architecture](##-architecture)

[Data Security](##-data-security)

[Features](##-features)

[Future Features](##-future-features)

[Web Marketing Strategies](##-web-marketing-strategies)

[Technologies used](##-technologies-used)

[Testing](##-testing)

[Deployment](##-deployment)

[Known bugs](##-known-bugs)

[Credits](##-credits)
</details>

## User Experience (UX) 

### User Stories :scroll:

When designing my user stories I used the Agile MoSCoW prioritisation technique and designed the user story table to help keep the project on track. The meaning of each label can be found in the key below. :point_down:

**Key:**

|Label| Definition|
|-----------------|-----------|
| <img src="https://img.shields.io/badge/-Must%20Have-green">|Requirement is necessary for the project to be conisdered as successfully completeted.|
|<img src="https://img.shields.io/badge/-Should%20Have-blueviolet"> |Requirement is important but not neccessary for the project to be conisdered as successfully completeted.
|<img src="https://img.shields.io/badge/-Could%20Have-yellow"> |Requirement is a bonus to the project and if not included the impacts are less significant that a 'must have' or 'should have'.|
|<img src="https://img.shields.io/badge/-Wont%20Have-red">| Requirement are not considered as a priority for the project, given the timeframe but may be revistited when implementing future features.|

**Table:**

The Table below shows the user stories for this project. These user stories ID links to the issue number displayed in the Kanban board (can be found in the projects sectiion) and does not reflect the order in which these stories where completed.

The Stories in the Kanban board contain the agreed acceptance criteria in the form of tasks so that an agile technique is used to track the development of the user stories and the project itself.


|User Story ID|User Type|User Story|Priority| 
|-----|-----|-----|-----|
|01|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to view reviews, without logging in or signing up|<img src="https://img.shields.io/badge/-Must%20Have-green">| 
|02|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to view popular products from the home page| <img src="https://img.shields.io/badge/-Must%20Have-green">
|03 |<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to view product details easily| <img src="https://img.shields.io/badge/-Must%20Have-green">|
|04|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to add my own reviews| <img src="https://img.shields.io/badge/-Must%20Have-green">|
|05|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to edit my own reviews|<img src="https://img.shields.io/badge/-Must%20Have-green">|
|06|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to delete my own reviews| <img src="https://img.shields.io/badge/-Must%20Have-green">|
|07|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to leave ratings for a product| <img src="https://img.shields.io/badge/-Should%20Have-blueviolet">|
|08|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to sign up | <img src="https://img.shields.io/badge/-Must%20Have-green">|
|09|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to login/logout | <img src="https://img.shields.io/badge/-Must%20Have-green">|
|10|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be notified when an action is successful/unsuccessful| <img src="https://img.shields.io/badge/-Should%20Have-blueviolet">|
|11|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to create my own profile | <img src="https://img.shields.io/badge/-Must%20Have-green">|
|12|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to view/edit my profile| <img src="https://img.shields.io/badge/-Must%20Have-green">|
|13|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to report offenesive content|<img src="https://img.shields.io/badge/-Wont%20Have-red">|
|14|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to recieve newsletter email |<img src="https://img.shields.io/badge/-Should%20Have-blueviolet">|
|15|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to view my order history |<img src="https://img.shields.io/badge/-Should%20Have-blueviolet">|
|16|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to checkout securely|<img src="https://img.shields.io/badge/-Must%20Have-green">|
|17|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to add/update the quantity of my items in my cart|<img src="https://img.shields.io/badge/-Must%20Have-green">|
|18|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to view related items when I am looking at a product|<img src="https://img.shields.io/badge/-Should%20Have-blueviolet">|
|19|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to view my recently viewed products in the homepage|<img src="https://img.shields.io/badge/-Should%20Have-blueviolet">|
|20|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to search for a particular product|<img src="https://img.shields.io/badge/-Must%20Have-green">|
|21|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to filter my searches |<img src="https://img.shields.io/badge/-Should%20Have-blueviolet">|
|22|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to view the status of my order in my account|<img src="https://img.shields.io/badge/-Must%20Have-green">|
|23|<img src="https://img.shields.io/badge/-Site%20Admin-lightgrey">| I want to be able to add products from the UI|<img src="https://img.shields.io/badge/-Must%20Have-green">|
|24|<img src="https://img.shields.io/badge/-Site%20Admin-lightgrey">| I want to be able to edit products from the UI|<img src="https://img.shields.io/badge/-Must%20Have-green">|
|25|<img src="https://img.shields.io/badge/-Site%20Admin-lightgrey">| I want to be able to delete products from the UI|<img src="https://img.shields.io/badge/-Must%20Have-green">|
|26|<img src="https://img.shields.io/badge/-Site%20Admin-lightgrey">| I want to have my own admin area|<img src="https://img.shields.io/badge/-Must%20Have-green">|
|27|<img src="https://img.shields.io/badge/-Site%20Admin-lightgrey">| I want to be able to add my own reviews|<img src="https://img.shields.io/badge/-Must%20Have-green">|
|28|<img src="https://img.shields.io/badge/-Site%20Admin-lightgrey">| I want to be able to send newsletter emails from the admin|<img src="https://img.shields.io/badge/-Must%20Have-green">|
|29|<img src="https://img.shields.io/badge/-Site%20Admin-lightgrey">| I want to be able to update order status from the admin|<img src="https://img.shields.io/badge/-Must%20Have-green">|
|30|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to use other social media to login|<img src="https://img.shields.io/badge/-Wont%20Have-red">|
|31|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to see what products are coming soon without subscribing to the newsletter|<img src="https://img.shields.io/badge/-Wont%20Have-red">|
|32|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to post sports related articles and connect with other sports enthusiasts|<img src="https://img.shields.io/badge/-Wont%20Have-red">|
|33|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able delete contact/address details from my profile | <img src="https://img.shields.io/badge/-Must%20Have-green">|
|34|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able view featured products | <img src="https://img.shields.io/badge/-Should%20Have-blueviolet">|
|35|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able view product variants | <img src="https://img.shields.io/badge/-Should%20Have-blueviolet">|
|36|<img src="https://img.shields.io/badge/-Site%20User-blue">| I want to be able to receive email confirmation of my order | <img src="https://img.shields.io/badge/-Must%20Have-green">|

**Kanban Board**

Below :point_down: are screenshot of the Kanban board, all stories within the scope of this project have been completed. The Stories that will not be implemented in this release have been closed as wont fix and moved to the backlog, where they may be reconsidered for future releases.

<img src="static/images/Kanban_Board.png" alt="Kanban Board" width="450px" height="250px">


### Overall Goals :dart:
Create an e-commerce cloud-hosted Full-Stack web application to sell sports related products online.
Allow superusers access to full CRUD (create, read, update and delete) functionality on reviews and products.
Allow Site Users access to full CRUD (create, read, update and delete) functionality on reviews
To provide users with an evolving product selection and smooth customer experience when shopping on E-store.

### Strategy :bulb:
E-store is primarily focused on selling B2C products to end users. Consumers habits have changed post Covid and more consumers than ever before are turning to online shopping versus traditional brick-and-mortar store purchases. This is where E-store aims to benefit consumers by offering quality products and a resonable cost, without shipping fees, so that consumers can enjoy the perks of traditional shopping from the comforts of their own home. 

### Site User / Target Audience / Demographic :busts_in_silhouette:
Target market is anyone between 18 - 40
Particuarly sports enthusiasts who are looking for the best quality sports equipment and accessories

### Site Goals :desktop_computer:
The site's main purpose is immediately clear
Simple navigation that allows the user to find information and resources intuitively
User authentication
CRUD functionality for superuser(s) and Site Users where appropriate


### Design :art:

The main goal was to make an intuitive UX, so that the user is not confused when visiting the Website. To achieve this, I created a simple, succinct, web application. The navabar is present on every page with clear icons for easy navigation.

The user experience should be tailored. To ensure this navbar items vary based on whether the user is authenticated, so that users who are not logged in aren't shown features that are not available to them.

If a user tries to access a page they are not auhtorised to, they are informed why they can't see the page and a link is provided so that they can rectify the issue in one click. 

All user actions shoud return a response. To ensure this is possible there are specific success and error messages displayed as result of a user action. Page redirects are also used to make it obvious that an action has been successfully completed.

**• Colour scheme** 

   ° I have gone for a simple monochrome theme to enusre accessibility for all users. All  text and Icons are displayed in black  (#ffffff) or white (#000000) subject to what offers the best contrast.

   ° Messages and Buttons do not conform to the monochrom theme to ensure that they stand out to the user. 
        • I have used red for delete buttons (:point_down:) as red is associated with danger making it an obvious alert for the user, promitng them to stop and think before taking further action. Red is also used for the background of error messages to alert the user that something has gone wrong.

<img src="static/images/delete_button.png" alt="delete button" width="450px" height="250px">

        • I have used green for buttons that are immediate calls to action (an example can be seen below :point_down:) as green has positive connotation thus encourages the user to take these actions.

<img src="static/images/call_to_action.png" alt="call to action examples" width="450px" height="250px">

        • I have used blue for buttons or messages that provide information as blue is associated with information again further encouraging the desired behaviour from the user as can be seen in the image below. :point_down:

<img src="static/images/info.png" alt="view product button" width="450px" height="250px">

        • I have used yellow for buttons or messages that should be approached with caution as yellow is associated with warning. Hence why this is the button colour for editing product as seen in the image below :point_down:

**• Typography**

   ° In keeping with the minimalistic style of the website, I have chosen to use an open sans type family font 'Roboto' as it is popular font used by more than 25 million websites, including Google. By using Roboto E-store provides a better user experience and improves readability making it easy for the user to navigate the site.

**• Imagery**

   ° The icons used throughout the site are [Boostrap](https://unpkg.com/boxicons@2.0.9/css/boxicons.min.css') icons

   ° The logo was created using [Tailor Brands](https://www.tailorbrands.com/logo-maker) 

**• Wireframes**

   ° Wireframes were created using figma. To meet my UX objective of creating a simple and intuitive User Interface (UI), I took a minimalisitic approach with the wireframes, to provide flexibility so that the project can evolve in accordance with user feedback. Without straying from the minimalistic theme.


## Architecture

### Database Schema

20 tables have been used for this website, I created the following 10 tables: coupon, newsletter, subscriber, ProductReview, Userprofile, ProductImages, Product, Item, Order and Category. The other 10 are django generated. 

A relational database was created. SQLite database was used in development as this is the default django database and ElephantSQL was used in production. More information on how I confired my databse will be prodived in the [deployment](##-deployment) section of my README.

Below is a database schema for my database :point_down: 

<img src="static/images/Schema.png" alt="database schema" width="750px" height="550px">


Below is an Entity relationship diagram (ERD) for my database :point_down: 

<img src="static/images/ERD.png" alt="entity relationship diagram" width="750px" height="550px">

Below I have explained the relevance of each table to the website. The table Name in brackets is refrence to the table name seen in the ERD diagram (:point_up: ) and the table name outside of the brackets is refrence to the schema diagram (:point_up: ).

### **Coupon (coupon_coupon)**

**Is used by the Admin to:**

    • generate a coupon that can be used by the site user. 

    • set a Coupon value to be applied at checkout 

    • limit the number of coupons available 

    • monitor the number of coupons that have been used coupons 

    • check how many valid coupons remain 

**Is used by the Site user to:**

    • apply a discount at checkout

### **Newsletter (newsletter_newsletter)**

**Is used by the Admin to:**

    • generate and send newsletters.

### **Subscriber (newsletter_subscriber)**

**Is used by the Admin to:**

    • create a newsletter mailing list

    • monitor the users that have confirmed newsletter subscription

**Is used by the Site user to:**

    • subscribe to newsletter mailing list

### **Product (store_product)**

**Is used by the Admin to:**

    • create, edit and delete products 

**Is used by the Site user to:**

    • to view products

## **ProductImages (store_productimages)**

**Is used by the Admin to:**

    • upload and display multiple product images

**Is used by the Site user to:**

    • view product images

### **ProductReview (store_productreview)**

**Is used by the Site user to:**

    • create, edit, delete and view product reviews

### **Item (order_item)**

**Is used by the admin to:**

    • view individual items in a order
 

**Is used by the Site user to:**

    • view individual items in the cart

    • view the total number of items in the cart

    • increase/decrease the number of items in the cart

    • view the quantity of each item in the cart

    • view the price of each item in the cart

    • view the total price of the cart


### **Category (store_category)**

**Is used by the Admin to:**

    • categorise products

**Is used by the Site user to:**

    • view products by category

### **Userprofile (userprofile_userprofile)**

**Is used by the Site user to:**

    • create, edit, delete and view their profile

### **Order (order_order)**

**Is used by the admin to:**

    • view order details

    • update order status

    • send a confirmation email with order details

**Is used by the Site user to:**

    • view order history

    • view order status

**• Wireframes**

   ° Wireframes were created using figma. To meet my UX objective of creating a simple and intuitive User Interface (UI), I took a minimalisitic approach with the wireframes, to provide flexibility so that the project can evolve in accordance with user feedback. Without straying from the mnimilistic theme. Here is the link to [my wireframes](https://www.figma.com/file/InlAv0zeQRhFP3Lbl9vp0C/E-store?node-id=0%3A1&t=BesByw5kxYm2BUtV-0) for desktop, tablet and mobile. After listening to user feedback during the project; minor amendments were made. However, all [features](##Features) will be discussed later in the README. Below are screenshots of the desktop and mobile Wireframes. :point_down: 

   **Home page** - screenshot for Desktop :desktop_computer: and Mobile :iphone:

   <img src="static/images/Home-Wireframe.png" alt="Home-Wireframe" width="550px" height="350px">
   
   **Category page** - screenshot for Desktop :desktop_computer: and Mobile :iphone:

   <img src="static/images/Category-Wireframe.png" alt="Category-Wireframe" width="550px" height="350px">

   **Forms**  - screenshot for Desktop :desktop_computer: and Mobile :iphone:

   All the forms used in this web application have a uniform style and appear on a seperate page.

   <img src="static/images/Forms-Wireframe.png" alt="Forms-Wireframe" width="550px" height="350px">

   **Products**  - screenshot for Desktop :desktop_computer: and Mobile :iphone:

   All the forms used in this web application have a uniform style and appear on a seperate page.

   <img src="static/images/Forms-Wireframe.png" alt="Products-Wireframe" width="550px" height="350px">

   **My Account**  - screenshot for Desktop :desktop_computer: and Mobile :iphone:

   <img src="static/images/Profile-Wireframe.png" alt="Profile-Wireframe" width="550px" height="350px">

   **Cart**  - screenshot for Desktop :desktop_computer: and Mobile :iphone:

   <img src="static/images/Cart-Wireframe.png" alt="Cart-Wireframe" width="550px" height="350px">

## Data Security

The follwoing steps have been taken to ensure the security of the users data as well as the integrity of the business :

 **env.py file**
    • used to store key variables for accessing secure environments like ElephantSql, cloudinary ect.
        ° This variables ar ealso stored within Heroku's config variables to ensure Gitpod and Heroku can sychronise securely. 

**git ignore**
    • used to ensure the env.py file is never committed to production.

**Cross Site Request Forgery (CSRF) Tokens**
    • All HTML forms have CSRF tokens applied. This provides protection from malicious attacks when sending data (CSRF attacks)

**User Authentication**
    • Django's Authentication has been applied to key areas of the site where login is required. To add a further layer of security only admins (superusers) have full CRUD functioanlity to create, read, update and delete products on the site. Authorised users have limited CRUD functionality as they are only allowed to update and delete reviews they created. 


## Features 

As previously explained (:point_up: ) slight ammendments were made during the project in response to user feedback. I will now be explaining the current features and where I have deviated from the wireframe the rationale for this will be provided to help demostrate the progression of the project, I will also refrence the user story related to each feature. Some future features will also be discussed.

**Site User**

First I will be looking at the features for site users

### **Current Features:** :white_check_mark:

#### **Nav Bar**

• The Navbar is available on every page, this allows seamless navigation across the web application, ensuring the main features are acessible in one click. The order of navbar items has changed slighlty due to user feedback and responsiveness issues on smaller view ports. The standard Navbar is show below. :point_down:

<img src="static/images/Navbar-Logout.png" alt="Standard Navbar">

  ° To ensure responsiveness across a range of view ports a hamburger menu is used on smaller screens as seen in the images below. :point_down:

  <img src="static/images/Navbar-mobile.png" alt="mobile Navbar">

  <img src="static/images/Hamburger-Nav.png" alt="Hamburger Navbar Menu">

• The navbar is also personalised so that the user experience is tailored. 

  ° When logged in the user will see a Navbar that looks similar to the screenshot below. :point_down:

  <img src="static/images/Navbar-Login.png" alt="Navbar Login">

  ° The standard Nav bar is shown when a user is not logged in, this is so that the user is only shown areas they have access to.

  This feature links to user story [#09](https://github.com/bmcdonald2000/e-commerce/issues/9) as it provides access to the buttons to login/logout

#### **Home Page**

• The Homepage, displays  featured products, popular products, recently viewed products and the link to newsletter signup form as seen in the images below. :point_down: The homepage also contains links to view products linking to User story [#3](https://github.com/bmcdonald2000/e-commerce/issues/3)
  
<img src="static/images/Featured.png" alt="Featured products" width="550px" height="350px">

      ° The featured product section :point_up: of the homepage realtes to user story [#34](https://github.com/bmcdonald2000/e-commerce/issues/34)
    

<img src="static/images/Popular.png" alt="Popular products" width="550px" height="350px">

     ° The Popular product section :point_up: of the homepage realtes to user story [#2](https://github.com/bmcdonald2000/e-commerce/issues/2)


<img src="static/images/Recent.png" alt="Recently viewed products" width="550px" height="350px">

       ° The Recent product section :point_up: of the homepage realtes to user story [#19](https://github.com/bmcdonald2000/e-commerce/issues/19)


<img src="static/images/Newsletter.png" alt="Newsletter signup link" width="550px" height="350px">

       ° The Newletter Signup section :point_up: of the homepage realtes to user story [#14](https://github.com/bmcdonald2000/e-commerce/issues/14) The newsletter section is found above the footer on every page as per user feedback.

#### **Signup**

• The signup page can be accessed from the navabr 'signup' link. The signup form is shown below. :point_down: Once the form is filled out successfully the user is send a verfication link by email. Once verified they will be able to leave reviews and can edit their contact details and address. 

this form relates to user story [#08](https://github.com/bmcdonald2000/e-commerce/issues/08) and [10](https://github.com/bmcdonald2000/e-commerce/issues/10)

<img src="static/images/Signup1.png" alt="Signup Form" width="550px" height="350px">

The signup form has two halves the first of which :point_up: is mandatory to generate an account and the second :point_up: that is optional and will be used to populate contact/address details. 

<img src="static/images/Signup2.png" alt="Signup Form" width="550px" height="350px">

this section of the signup page :point_up:  relates to user story [#11](https://github.com/bmcdonald2000/e-commerce/issues/11)

#### **Logout**

• The Logout button can be accessed from the navabr userprofile link as indicated shown below. :point_down: . The user is redirected to the homepage on logout and the navbar is no longer customised. 

this form relates to user story [#09](https://github.com/bmcdonald2000/e-commerce/issues/09) and [#10](https://github.com/bmcdonald2000/e-commerce/issues/10) 

<img src="static/images/Logout.png" alt="Logout Form" width="550px" height="350px">


#### **Category view**

• Users can search products in a particulary category using the navbar. Below is an example of what category pages look like. This feature relates to user story [#03](https://github.com/bmcdonald2000/e-commerce/issues/03)

<img src="static/images/Category.png" alt="Categories" width="550px" height="350px">

° from the navbar the user is directed to the categories section :point_up:  where they can pick the sub category they would like to view and they will see something similar to the image below :point_down: 

<img src="static/images/SubCategory.png" alt="Sub Categories" width="550px" height="350px">

#### **Product deatails view**

• Users can use the view button to get more details about a product. The product details page allow the user to select images where there are multiple images and view product description which relates to user stories  [#03](https://github.com/bmcdonald2000/e-commerce/issues/03), [#07](https://github.com/bmcdonald2000/e-commerce/issues/07). :point_down:

<img src="static/images/ProductPage.png" alt="Product page" width="550px" height="350px">

<img src="static/images/ProductImages.png" alt="Product images" width="550px" height="350px">

• Users can add a product to their cart and they are notified if this is success :point_down: this relates to user stories [#010](https://github.com/bmcdonald2000/e-commerce/issues/10) & [#017](https://github.com/bmcdonald2000/e-commerce/issues/17)

<img src="static/images/AddToCart.png" alt="Add to cart functionality" width="550px" height="350px">

<img src="static/images/AddToCartNotification.png" alt="Add to cart notifiaction" width="550px" height="350px">


• Authenticated users also have full Create, Read, Update & Delete (CRUD) functionality with the reviews section on the product page :point_down: This relates to user stories [#04](https://github.com/bmcdonald2000/e-commerce/issues/04), [#05](https://github.com/bmcdonald2000/e-commerce/issues/05) and [#06](https://github.com/bmcdonald2000/e-commerce/issues/06)

<img src="static/images/Review.png" alt="Reviews" width="550px" height="350px">

• Unauthorised users will be prompted to login or signup if they attempt to use the review CRUD functionality :point_down:

<img src="static/images/UnauthorisedReview.png" alt="Reviews" width="550px" height="350px">

• where a product has variants the user is able to see these and choose which variant to add to the basket. This feature relates to user story [#35](https://github.com/bmcdonald2000/e-commerce/issues/35)

<img src="static/images/Variants.png" alt="Products with variations" width="550px" height="350px">

• where there are related producs these are also displayed below the product reviews like so :point_down: this feature relates to user story [#18](https://github.com/bmcdonald2000/e-commerce/issues/35)

<img src="static/images/related.png" alt="Related product" width="550px" height="350px">

#### **Checkout**

The user can update their basket quantity, view product and checkout securely with stripe from the checkout page. This page relates to user stories [#03](https://github.com/bmcdonald2000/e-commerce/issues/03), [#10](https://github.com/bmcdonald2000/e-commerce/issues/10), [#16](https://github.com/bmcdonald2000/e-commerce/issues/16) , [#17](https://github.com/bmcdonald2000/e-commerce/issues/17) and [#36](https://github.com/bmcdonald2000/e-commerce/issues/36) :point_down:


<img src="static/images/Checkout.png" alt="Cart Checkout page" width="550px" height="350px">

<img src="static/images/StripeCheckout.png" alt="Stripe Checkout" width="550px" height="350px">

<img src="static/images/SuccessHtml.png" alt="Successful Order page" width="550px" height="350px">

<img src="static/images/EmailOrderConfirmation.png" alt="Order Confirmation email" width="550px" height="350px">

#### **Newsletter Signup**

• The newsletetr signup form relates to user stories [#14](https://github.com/bmcdonald2000/e-commerce/issues/14) and [#10](https://github.com/bmcdonald2000/e-commerce/issues/10) . Users can subscribe to the mailing list to recieve newsletters. :point_down:

<img src="static/images/NewsletterNotification.png" alt="Newsletter Sign up form" width="550px" height="350px">

#### **Search**

• The search page allows users to search conduct a filter search on products on the site. This feature relates to user story [#20](https://github.com/bmcdonald2000/e-commerce/issues/20) and [#21](https://github.com/bmcdonald2000/e-commerce/issues/21). :point_down:

<img src="static/images/Search.png" alt="Search" width="550px" height="350px">

#### **My Account**

• This page allows the user to edit and remove their contact/address data, View order history and order status.:point_down: These features relate to user stories [#15](https://github.com/bmcdonald2000/e-commerce/issues/15), [#22](https://github.com/bmcdonald2000/e-commerce/issues/22) and [#33](https://github.com/bmcdonald2000/e-commerce/issues/33). :point_down:


<img src="static/images/Userprofile.png" alt="User Profile" width="550px" height="350px">

• This :point_up: is an account without orders and an account with orders would look like this :point_down:

<img src="static/images/OrderHistory.png" alt="Order History" width="550px" height="350px">

**Admin**

Now I will be documenting the Admin specific site features. The Admin (Super User) has Full CRUD functionality for products within the UI.

#### **Nav Bar**

• There is only a slight differnce in the site user navbar and the Admin Navbar and this is the 'add product' button. Like the standard navabar the Admin Navbar is avaibale on every page and uses a hamburger menu on smaller screens. The Admin Navbar is show below. :point_down: This relates to user stories [#23](https://github.com/bmcdonald2000/e-commerce/issues/23) and [#10](https://github.com/bmcdonald2000/e-commerce/issues/10)

<img src="static/images/AdminNav.png" alt="Admin Navbar">

    ° This navbar allows the Admin to have full Create fucntionality within the UI as demonstarted in the image below :point_down:

<img src="static/images/AddProductForm.png" alt="Admin functionality within UI" width="550px" height="350px">

    ° Once the form has been competed sucessfully the admin is notfied like in the image below. :point_down:

<img src="static/images/AddProductNotification.png" alt="Admin add product sucess notification" width="550px" height="350px">


#### **Homepage**

There is only a slight differnce in the site users homepage and the Admin Navbar and this is the 'edit product' and 'delete product'  buttons. Provided the Admin the Read,Update and Delete aspects of CRUD fucntionality  :point_down: This feature relates to user stories [#24](https://github.com/bmcdonald2000/e-commerce/issues/24) and [#25](https://github.com/bmcdonald2000/e-commerce/issues/25). :point_down:

<img src="static/images/AdminProducts.png" alt="Admin functionality within UI" width="550px" height="350px">

<img src="static/images/editNotification.png" alt="Edit product notification" width="550px" height="350px">

<img src="static/images/deleteNotification.png" alt="Delete product notification" width="550px" height="350px">



#### **Admin Panel**

• All models for the site have been registered in the Admin as seen in the imagee below :point_down:, thus making it easy for the admin to monitor/manage the site data as required by user story [#26](https://github.com/bmcdonald2000/e-commerce/issues/26) 

<img src="static/images/AdminPanel.png" alt="Admin Panel">

    ° Product reviews can be easily viewd from the Admin as seen in the image below :point_down: This relates to user story [#27](https://github.com/bmcdonald2000/e-commerce/issues/27).

<img src="static/images/AdminReviews.png" alt="Admin Reviews section">

    ° The Admin can Send Newsletters directly from the admin as demonstarted in the images below :point_down: This relates to user story [#28](https://github.com/bmcdonald2000/e-commerce/issues/28) and [#14](https://github.com/bmcdonald2000/e-commerce/issues/14)

<img src="static/images/AdminEmailFunction.png" alt="Admin Newsletter Email Function">

<img src="static/images/AdminNewsletterEmail.png" alt="Admin Newsletter Email">


    ° The Admin can filter through orders and update order status as demonstrated in the image below :point_down: This relates to user stories [#26](https://github.com/bmcdonald2000/e-commerce/issues/26) and [#29](https://github.com/bmcdonald2000/e-commerce/issues/29)

<img src="static/images/OrderStatus.png" alt="Admin Newsletter Email Function">

<img src="static/images/AdminFilter.png" alt="Admin Newsletter Email">

**Footer**
• The footer contains social media and policy links as shown below :point_down:

<img src="static/images/footer.png" alt="footer">

<img src="static/images/privacy.png" alt="privacy policy">

<img src="static/images/refunds.png" alt="refund policy">

<img src="static/images/conditions.png" alt="terms and conditions">

<img src="static/images/ContactUs.png" alt="contact us">

**404 page**

<img src="static/images/404.png" alt="custom 404 page" width="550px" height="350px">

## Future Features :rocket:

**Blog**

**Gift Cards**


## Web Marketing/Email Marketing Strategies

### **SEO - Search Engine Optimization**

Google keyword research was used to optimise web pages and content to increase ranking in search engines. Both short-tail & Long-tail keywords are used. The “People also ask” and “Related searches” was also used to identify keywords used.

<img src="static/images/Keywords.png" alt="keywords">


### Social Media Marketing

A Facebook business page was created with the intent of generating growth organically by building a community and enganging with our target market to encourage loyalty. As this is free, quick to set up and Facebook has a large audience it is advantageous. The site can connect with customers directly via the Facebook platform as well a wider global demographic. The primary aim of the Facebook page is to build and maintain a relationship with my target audience. The content created can then be spread across different social media platforms i.e instragram and TikTok to further generate audience engagement.

I have included a screenshot of the business page below as it may be removed by Facebook.

<img src="static/images/FB.png" alt="Facebok Business Page">

### Email Media Marketing

SendGrid is used to gain new customers and retain existing ones. SendGrid enables the business to run and analyse the success of newsletter marketing campaigns. Users who register to receive the newsletter are automatically added to the subscribers list. This strategy was chosen because its free to set up with the current level of business and can be scaled as the business grows. Thus increasing conversions and generating more revenue for the business. The users who sign up have already visited the website making them more likely to become customers, reducing the cost of generating sales.

## Technologies Used

#### Languages, frameworks and librarys used

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Bulma](https://img.shields.io/badge/bulma-00D0B1?style=for-the-badge&logo=bulma&logoColor=white)
![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D)

#### Database Used
In Development I used the Django default database SQLite, this is not compatible with Heroku so I switched to ElephantSql Prior to Deployment as Heroku postgres no longer supports hobby tiers.

![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

#### Programs used
[AmIResponisve](http://ami.responsivedesign.is/#) - I used amiresposive to generate the resposive image at the start of my Readme.
[Google Dev Tools](https://developer.chrome.com/docs/devtools/)- I used google dev tools to test my site performance across a range of devices.
[Tailor Brands](https://studio.tailorbrands.com/) - I used Tailor brands to create my logo.
[Git](https://git-scm.com/) - I used Git to track the changes to my code. Git was also used for version control.
[Github](https://github.com/) - Github was used to host my project files. I then used Gitpages to deploy the website.
[Vs Code](https://code.visualstudio.com/)- VS Code powers gitpod and was used to build the website.
[Slack](https://slack.com/intl/en-gb/) - I used slack to get feedback on my project.
[Google Fonts](https://fonts.google.com/) - The fonts used are google fonts.
[Figma](https://www.figma.com/) - I used figma to design my mockups.
[Gitpod](https://www.gitpod.io/blog/next-chapter-for-gitpod) - Gitpod is powered by VS Code, storing my code in the cloud. I can then commit that code to my Github repository as Gitpod and Github are connected.
[Privacy Policies](https://www.privacypolicies.com/)- Free Returns and Refund Policy Generator.
[Privacy Policies Generator](https://www.privacypolicygenerator.info/)- Free Privacy Policy Generator.
[Terms and Conditions Generator](https://www.termsandconditionsgenerator.com/)- Free terms and conditions generator.
[Lighthouse testing](https://developers.google.com/web/tools/lighthouse) - I used lighthouse testing to test the performance of my webpage.
[Cloudinary](https://cloudinary.com/) - I used cloudinary store media files uploaded by users.
![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white) 
![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)	
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Stripe](https://a11ybadges.com/badge?logo=stripe)
![Twilio](https://a11ybadges.com/badge?logo=twilio)

## Testing

#### Validation Testing

##### Lighthouse Testing

 The overall performance of my webpage is good but there is room for improvement in best practices. As seen in the screenshot below.

<details>
<summary><strong>Lighthouse Report Results</strong></summary>
<br>
<img src="static/images/Lh.png" alt="Lighthouse testing" width="750px" height="350px">
<img src="static/images/LhAbout.png" alt="Lighthouse testing for about us page" width="750px" height="350px">
<img src="static/images/LhContact.png" alt="Lighthouse testing for contact us page" width="750px" height="350px">
<img src="static/images/LhFootaball.png" alt="Lighthouse testing for football poducts" width="750px" height="350px">
<img src="static/images/LhMensW.png" alt="Lighthouse testing for mens watches" width="750px" height="350px">
<img src="static/images/LhPGenerator.png" alt="Lighthouse testing for Privacy policy " width="750px" height="350px">
<img src="static/images/LhPrivacy.png" alt="Lighthouse testing for refunds policy" width="750px" height="350px">
<img src="static/images/LhSports.png" alt="Lighthouse testing sports products" width="750px" height="350px">
<img src="static/images/LhTerms.png" alt="Lighthouse testing for terms and conditions" width="750px" height="350px">
</details>

##### W3C Validator

I have included some vue.js in my html and this caused some errors but the html passes validation as shown below. 

The only errors I recieve are in relation to'@click' and 'class:' which is valid vue.js and duplicate of 'id = options' although this is only declared once in the code, as seen below :point_down:

<img src="static/images/Id.png" alt="w3c validation error" width="750px" height="350px">

As seen in my code above :point_up: options is only used as an Id once however the below error is shown on validation :point_down: this is likely because most pages extend my base.html file where I have assigned the id options. 
<img src="static/images/Id.png" alt="w3c validation error" width="750px" height="350px">

:point_up: The same errors/warning show on all pages, for reason previosuly mentioned. SO I have attached the link to the result for a few pages.

[Cart page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftranquil-temple-81228.herokuapp.com%2Fcart%2F)
[Login page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftranquil-temple-81228.herokuapp.com%2Flogin%2F)
[My account](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftranquil-temple-81228.herokuapp.com%2Fmyaccount)

##### W3C CSS Validator 

My CSS passed validation but the bulma css caused some errors

<img src="static/images/W3C_CSS.png" alt="w3c validation error" width="750px" height="350px">


##### Python validation

PEP8 validator is down so I used flake8. As I have used a variety of django packages there are instances where the code does not conform to coding i.e longer line lengths than disarable for settings and urls but asides from this I have taken all reasonable steps to ensure my code adheres to best practice.


##### JSHint

I used JsHint to validate my Js but again due to the use of vue.js there were some errors. I used the Vue.Js docs to ensure I adeared to vue.js best practice.


##### Manual Testing

I have chosen to perform manual tests as I followed a manual process for developmetn and deployemnt. To ensure my deployed site aligns with the site in development I covered the following areas:

**• User Stories**
    ° To ensure that the user requirements have been delivered for the release. 
        • All user stories have been completed and as evidence earlier in the README have met the acceptance criteria

**• User Acceptance Testing (UAT)**
    ° To ensure the website meets real world expectations I continously sought feedback throughout the project and use this to inform my choices. I also used friends and family to set the acceptance criteria for the user stories and then broke this down into tasks that can be seen in the kanbanboard. 

**• Page/Link validation**
    ° To ensure all the features and links across the site are working as expected. All known issues have know been fixed and everything is working as expected. 

**• Responsiveness**
    ° To ensure each page is responsive across all viewports.

        • To help with this I also used Bulma and Boostrap

**• Performance**
    ° Site performance, best practice, accessibility and SEO have been tested using Chrome's developer tool called Lighthouse Testing which was previosuly documented in the README.

**• Browser**

The following functions were tested on the following browsers using a pass / fail system:

|   Function	    |  Browser 	| Result  	|
|-----------------|-----------|-----------|
| CRUD | ![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white) ![Firefox](https://img.shields.io/badge/Firefox-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white) ![Safari](https://img.shields.io/badge/Safari-000000?style=for-the-badge&logo=Safari&logoColor=white) ![Opera](https://img.shields.io/badge/Opera-FF1B2D?style=for-the-badge&logo=Opera&logoColor=white)|   PASS	
|  View Reviews/Products |  ![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white) ![Firefox](https://img.shields.io/badge/Firefox-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white) ![Safari](https://img.shields.io/badge/Safari-000000?style=for-the-badge&logo=Safari&logoColor=white) ![Opera](https://img.shields.io/badge/Opera-FF1B2D?style=for-the-badge&logo=Opera&logoColor=white)|	 PASS  	|
| Checkout/Cart|  ![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white) ![Firefox](https://img.shields.io/badge/Firefox-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white) ![Safari](https://img.shields.io/badge/Safari-000000?style=for-the-badge&logo=Safari&logoColor=white) ![Opera](https://img.shields.io/badge/Opera-FF1B2D?style=for-the-badge&logo=Opera&logoColor=white)	 	|   PASS	|
| Navbar/Search |  ![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white) ![Firefox](https://img.shields.io/badge/Firefox-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white) ![Safari](https://img.shields.io/badge/Safari-000000?style=for-the-badge&logo=Safari&logoColor=white) ![Opera](https://img.shields.io/badge/Opera-FF1B2D?style=for-the-badge&logo=Opera&logoColor=white) 	|   PASS	|
| Signup/Login/Logout|  ![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white) ![Firefox](https://img.shields.io/badge/Firefox-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white) ![Safari](https://img.shields.io/badge/Safari-000000?style=for-the-badge&logo=Safari&logoColor=white) ![Opera](https://img.shields.io/badge/Opera-FF1B2D?style=for-the-badge&logo=Opera&logoColor=white)	 	|   PASS	|
Footer Links 	  |  ![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white) ![Firefox](https://img.shields.io/badge/Firefox-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white) ![Safari](https://img.shields.io/badge/Safari-000000?style=for-the-badge&logo=Safari&logoColor=white) ![Opera](https://img.shields.io/badge/Opera-FF1B2D?style=for-the-badge&logo=Opera&logoColor=white)	|  PASS 	|                                                                                                          
