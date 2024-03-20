To navigate back to the main README click [here](README.md)

# Functional Testing

## Authentication

Description:

Ensure user is able to sign up to website.

Steps:

1. Click on [Register](https://train-up-pp5-da4fce5b9326.herokuapp.com/accounts/signup/)
2. Fill in form
3. Click Sign Up

Expected:

User is able to follow email confirmation link in recieved email. Confirm their email and log in afterwards

Actual:

User is signed up and info message is displayed and they revcieve a confirmation email and they must follow the link in to confirm their account.

---

Description:

Ensure user is able to sign up to website.

Steps:

1. Folllow the link in the confirmation email
2. Click confirm
3. Sign in at [Login]( https://train-up-pp5-da4fce5b9326.herokuapp.com/accounts/login/)

Expected:

Users email is confirmed and when they log in a success message is displayed informing they are signed in

Actual:

Users email is confirmed and when they log in a success message is displayed informing they are signed in

---

Description:

Ensure user is able to log out of the site 

Steps:

1. Click on [Logoout](https://train-up-pp5-da4fce5b9326.herokuapp.com/accounts/logout/)
2. Click sign out

Expected:

Users is signed out and success message is displayed advising that they have signed out

Actual:

Users is signed out and success message is displayed advising that they have signed out

---

Description:

Ensure user is able to log out of the site 

Steps:

1. Click on [Logoout](https://train-up-pp5-da4fce5b9326.herokuapp.com/accounts/logout/)
2. Click sign out

Expected:

Users is signed out and success message is displayed advising that they have signed out

Actual:

Users is signed out and success message is displayed advising that they have signed out

---

## Shopping Process

Description:

Ensure user is able to view all products and view a individual product and add it to the basket

Steps:

1. Click on [Shop Now](https://train-up-pp5-da4fce5b9326.herokuapp.com/products/)
2. Click on any product
3. From the products page select the qunatity and click add to cart

Expected:

User is able to add a product to the basket and a success message is displayed informing the user of the current basket details

Actual:

Users is able to add a product to the basket and a success message is displayed informing the user of the current basket details

---

Description:

Ensure user is able to view all items in their basket and proceed through checkout process

Steps:

1. Click on [Basket](https://train-up-pp5-da4fce5b9326.herokuapp.com/bag/)
2. Ensure basket details are correct updating quantity if necessary
3. Click secure checkout 
4. Fill in form with details
5. Use Test card details
6. Click complete order

Expected:

User is able to complete the order, recieves a confirmation order email and is directed to the purchase succesful page

Actual:

User is able to complete the order, recieves a confirmation order email and is directed to the purchase succesful page

---

## Profile Testing

Description:

Ensure user is able to edit delivery address

Steps:

1. While logged in Click on [My Profile](https://train-up-pp5-da4fce5b9326.herokuapp.com/profiles/)
2. click on edit Delivery Address
3. Edit Delivery Details
4. Click Update information

Expected:

User is able to update their delivery information and a successs message is displayed informing the user that the profile was updated successfuly 

Actual:

User is able to update their delivery information and a successs message is displayed informing the user that the profile was updated successfuly 

---

Description:

Ensure user is able to view previous orders

Steps:

1. While logged in Click on [My Profile](https://train-up-pp5-da4fce5b9326.herokuapp.com/profiles/)
2. click on edit order History
3. Click on the order number 

Expected:

User is redirected to a order confirmation page and a information is displayed informing them that they are looking at a previous order confirmation

Actual:

User is redirected to a order confirmation page and a information is displayed informing them that they are looking at a previous order confirmation

---

## Session Posting

Description:

Ensure user is able to post a session that they completd
Steps:

1. While logged in Click on [Session Feed](https://train-up-pp5-da4fce5b9326.herokuapp.com/sessionfeed/)
2. click on create post
3. Fill in form details
4. Click Post Session 

Expected:

User is able to see the new post that they created and a message is dispalyed informing that the post was succesful

Actual:

User is able to see the new post that they created and a message is dispalyed informing that the post was succesful

## Admin

Description:

Ensure admin is able to create a new product
Steps:

1. While logged in as admin Click on [Add Product](https://train-up-pp5-da4fce5b9326.herokuapp.com/products/add/)
2. Fill in form 
3. Click add product


Expected:

Admin is redirected to the new product that they created and a message is dispalyed informing that the product was added succesfuly 

Actual:

Admin is redirected to the new product that they created and a message is dispalyed informing that the product was added succesfuly

---

Description:

Ensure admin is able to edit a product
Steps:

1. While logged in as admin Click on [Shop Now](https://train-up-pp5-da4fce5b9326.herokuapp.com/products/)
2. Select product to edit
3. Click edit product
4. Edit form 
5. Click update product

Expected:

Admin is redirected to the product that they edited and a message is dispalyed informing that the product was edited succesfuly 

Actual:

Admin is redirected to the product that they edited and a message is dispalyed informing that the product was edited succesfuly 

---

Description:

Ensure admin is able to delete a product
Steps:

1. While logged in as admin Click on [Shop Now](https://train-up-pp5-da4fce5b9326.herokuapp.com/products/)
2. Select product to delete
3. Click delete product

Expected:

Admin is redirected to the all products page and a message is dispalyed informing that the product was deleted succesfuly 

Actual:

Admin is redirected to the all products page and a message is dispalyed informing that the product was deleted succesfuly 

---
Description:

Ensure admin is able to create a new coach
Steps:

1. While logged in as admin Click on [Coaches](https://train-up-pp5-da4fce5b9326.herokuapp.com/coaching/all_coaches/)
2. Click on add coach
2. Fill in form 
3. Click add Coach


Expected:

Admin is redirected to the all Coaches page and a message is dispalyed informing that the coach was added succesfuly 

Actual:

Admin is redirected to the all Coaches page and a message is dispalyed informing that the coach was added succesfuly 

---

Description:

Ensure admin is able to edit a coach
Steps:

1. While logged in as admin Click on [Coaches](https://train-up-pp5-da4fce5b9326.herokuapp.com/coaching/all_coaches/)
2. Select coach to edit
3. Click edit coach
4. Edit form 
5. Click update coach

Expected:

Admin is redirected to the all coaches and a message is dispalyed informing that the coach was edited succesfuly 

Actual:

Admin is redirected to the all coaches and a message is dispalyed informing that the coach was edited succesfuly 

---

Description:

Ensure admin is able to delete a coach
Steps:

1. While logged in as admin Click on [Coaches](https://train-up-pp5-da4fce5b9326.herokuapp.com/coaching/all_coaches/)
2. Select coach to delete
3. Click delete coach

Expected:

Admin is redirected to the all coaches page and a message is dispalyed informing that the coach was deleted succesfuly 

Actual:

Admin is redirected to the all coaches page and a message is dispalyed informing that the coach was deleted succesfuly 

---

Description:

Ensure admin is able to delete a session
Steps:

1. While logged in as admin Click on [Session Feed](https://train-up-pp5-da4fce5b9326.herokuapp.com/sessionfeed/)
2. Select session to delete
3. Click delete post

Expected:

Admin is redirected to the Session Feed page and a message is dispalyed informing that the session was deleted succesfuly 

Actual:

Admin is redirected to the Session Feed page and a message is dispalyed informing that the session was deleted succesfuly 

## Navigation Links

Each link on the navbar was tested to ensure that they are rendering the correct pages. Each link was selected to test that the correct pages were loading. All links were tested including those that only appeared if logged in or if admin logged in.

- Logo = index.html
- Shop Now = products.html
- Session Feed = all_sessions.html
- Coaches = all_coaches.html
- My account = Dropdown displaying:
    - Register = all auth sign up page
    - Login = all auth login page
    - Add Product = add_product.html
    - My Profile = Profile.html
    - Logout = all auth log out page
- Basket = bag.html

All links were confirmed to be wokking as expected.

## Footer

All links were tested on the footer by clicking on the facebook page link the user was brought to the facebook page in a new tab

When the user inserted their email into the mailchimp form the user was confirmed to be added to the mailing list


## Negative Testing

All links across the site were also tested to ensure they return the expected all tests were succesful.

Tests were performed on all forms to ensure:

- All required fields are filled in to correct specification

## Accessibility

[Wave Accesibility Tool](https://wave.webaim.org/) was used to ensure that all pages were compliant with wave standards.
Due to Django templating developer tools were used in google to get the rendered html and paste

Some issues were found with the footer as the mailchimp form was missing a labek this was not edited as it could effect form success.

## Validator Testing

All pages were run through the [w3 HTML Validator](https://validator.w3.org/). Due to Django templating developer tools were used in google to get the rendered html and pasted into the validator to test the html.
Some issues were found with the mailchimp form which could not be edited.

All pages were run through the official Code Institute Pep8 validator to ensure all code was pep8 compliant. There were some issues found with lines being too long but i was unable to shorten these without breaking the code.

## Responsiveness

All pages were tested to ensure responsiveness from screen sizes 320px and up. This was monitored throughout development and the site took a mobile first approach. Responsiveness was tested on mobile devices and also on Chrome an Firefox.

Steps to test:

- Open browser and navigate to [Train-Up](https://train-up-pp5-da4fce5b9326.herokuapp.com/)
- Open the developer tools (right click and inspect)
- Set to responsive and decrease width to 320px
- Click and drag the responsive window to maximum width

Expected:

Site is responsive on all screen sizes and elements adjust depending on screen size.

Actual:

Site adjusted as expected.