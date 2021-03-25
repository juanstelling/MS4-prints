<h1 align="center">Testing</h1>

---

## Index 
- <a href="#manual-testing">1. Manual testing</a>
    - <a href="#visitor-goals">1.1 Visitor goals</a>
    - <a href="#consumer-goals">1.2 Consumer goals</a>
    - <a href="#returning-goals">1.3 Returning customers goals</a>
    - <a href="#admin-goals">1.4 Admin goals</a>
- <a href="#automated-testing">2. Automated testing</a>
- <a href="#validators">3. Code validators</a>
- <a href="#responsiveness">4. Responsiveness</a>
- <a href="#browser-compatibility">5. Browser compability</a>
- <a href="#other">6. Other</a>
- <a href="#bugs">7. Bugs</a>
- <a href="#future-testing">8. Future testing</a>

---

<span id="manual-testing"></span>

## 1. Manual testing

**All User Stories are tested with manual testing.**

<span id="visitor-goals"></span>

### 1.1 Visitor goals

1. As a visitor, I want to access the website from any device, so that I can go to the website on desktop, mobile and tablet.

    **Testing**
    - The visitor can visite the website on any device. The website is designed for computer, mobile and tablet. The test for the responsiveness with different devices can be found <a href="#responsiveness">here</a>
    - **Result:** Test passed
2. As a visitor, I want to be able to navigate easily through the website, so I can find everything easily. 

    **Testing**
    - A visitor can navigate throug the website with the navbar on top of the website and through the footer. There is a hamburger menu for mobile visitors, where they can easily can go to every relevant page.
    - The main navigation is through the navbar and contains the following: 
        - Search functionality, where visitors can search for products. The search functionality is based on the title or descriptin of a product. 
        - The profile icon where all profile related pages are places such as the profile page, the login, logout and sign up links. A visitor who is logged in can go to their profile and can logout through the profile icon. Visitors who aren't logged in can login or signup through the profile icon.
        - The shopping bag icon is a link to the shopping bag and you see the amount of dollars that are in your shoppingbag. 
        - A link to the prints. The visitor can go to all prints or can search prints based on category. 
        - A link the the about page of the company. 
        - A link to the sustainability of the company. 
    - The footer contains the following: 
        - Links to the prints. The visitor can go to all prints or can search prints based on category.
        - Links to profile related pages. A visitor sees relevant links based on whether they are logged in or not. (the same as the profile icon in the navbar) 
        - Links to important information about the order such as return policy and the FAQ. 
        - Link to the contact page, where visitors can contect the owners of the website. 
    - **Result:** Test passed. All links are working and the links are connected to the right page. The search functionality and the profile functionality with showing the right links whether a visitor is logged in or logged out are working correct.

3. As a visitor, I want to access the social media accounts of the company, so I can follow them and see the latest trends and news.

    **Testing**
    - Social media icons are standing at the bottom of the footer where visitors can click on. The social media icons are Pinterest, Facebook and Instagram. 
    - **Result:** Test passed: all social media icons are visible for any device and the links lead to the social media websites.

4. As a visitor, I want to sign up for the newsletter, so I can be up to date about the latest news and trends. 

    **Testing**
    - A visitor can sign up of the newsletter at the home and products page. 
    - A visitor can signup with a email. If the email is new the email is saved in the database and the email enters the mailinglist in Mailchimp. If the email already exists, there is a notification that the email already subscribed. 
    - **Result:** Test passed. The newsletter is standing on the home page and products page. And the functionality of checking if the email already exists works good. 

5. As a visitor, I want to know more about the company, so I know what the company is about.

    **Testing**
    - There is a about page with information about the company, the product and sustainability. 
    - **Result:** Test passed. The page contains company information, product information and information about sustainability.

6. As a visitor, I want to be able to contact the owners of the website, so I can easily ask a question. 

    **Testing**
    - The contact page is found in the footer of the website. 
    - There is a contact page where visitors can send their questions. 
    - On the contact page stands contact information such as the email address and phonenumber. 
    - **Result:** Test passed. Visitors can fill in the form with any questions or can contact the company through email of phone.

7. As a visitor, I want to see an overview of all the wall art, so I can see what the website is offering.

    **Testing** 
    - The products page gives an overview of all products. All products are standing on this page. 
    - The page shows a back to top button in case the website has a lot of products and the visitor has scrolled down a lot.
    - There is also a navigation of the products page for the different category. Visitors can sort the products on all, black and white, landscape, streetart and paint.
    - **Result** Test passed. All products are on the products page, the back to top button works and  the category links are showing the right results.

8. As a visitor, I want to be able to search and filter the wall art, so I can find specific wall art quick and easy.
    
    **Testing**
    - Visitors can sort the products based on price from low to high or from high to low. 
    - And visitors can sort the products based on alphabet from A - Z or Z - A
    - **Results:** Test passed. The sort functionality is working on the products page and on the category sections.

9. As a visitor, I want to be able to read more information about the wall art (size, price, image, description), so I can see if the product suits my preferences. 

    **Testing**
    - Visitors can visit the product detail page by clicking on the image of the product. 
    - The product detail page will shows the following information: category, if the product is in stock, price, size and description. 
    - Visitors can buy the product and set the quantity of the product if the product is in stock. Visitors can see if the product is in stock when they see the green text: in stock and they are seeing the add to shoppingbag button and the quantity functionality.
    - If the product isn't in stock there is a red text with: sold out. The quanity functionality and add to bag button are not visible. Instead there is a text that says to contact the company for more information. 
    - **Result:** Test passed: All product information is on the detail page and the in stock or not in stock functionality works good. 
    - *Note: Only product: Abstract no. 092 is not in stock! 

<span id="consumer-goals"></span>

### 1.2 Consumer goals 

10. As a consumer, I want to add products to my basket, so I can buy products. 

    **Testing**
    - The consumer can choose quantity of the product and can add the product to the basket by clicking on the add to bag button. 
    - The quantity can be set from 1 - 99. 
    - The quantity can be modified by typing in the number or by using the -/+ functionality. 
    - The add to bag button will put the product on the shoppingbag. 
    - A succes toast message shows when the product is added to the shoppingbag.
    - The amount in the navbar changes to the total price of the shoppingbag.
    - **Result:** Test passed. All functionalities of the toastmessage, add to bag and quantity are working good. 

11. As a consumer, I want to modify my order, so I can make last changes before I order the products.
    
    **Testing**
    - The consumer can modify the quantity of the order on the shoppingbag. The consumer can do this by changing the quantity and by clicking update.
    - **Result:** Test passed. The quantity updated when the consumer set another quantity and clicks on update.

12. As a consumer, I want to be able to delete products in my order, so I can remove products that I no longer wish to purchase. 

    **Testing**
    - The consumer can delete the product in the shoppingbag by clicking on the trash icon. 
    - **Result:** Test passed. The product is deleted when a consumer clicks on the trashbag.

13. As a consumer, I want to see the total price and shipping costs of my order, so I can see how much I have spent in total. 

    *Testing**
    - The consumer sees the price, shipping costs and the total price of the order. 
    - Free delivery is provided at $45,- or highter. The delivery costs are otherwise 10% of the order. 
    - The total price is automatically deducted from the product price and any shipping costs.
    - **Results:** The product price, shipping costs and total price are automatically calculated and are correct.

14. As a consumer, I want to pay with a card in a safe and secure way, so I know that my payment goes well. 

    **Testing**
    - Consumers can pay with credit card and the payment goes via Stripe payments. 
    - The stripe setup is based on a test environment. A consumer can fill in the number 4242 4242 4242 4242  to make a succesful payment. 
    - A Stripe webhook is implemented for extra secure payments. 
    - The consumer has to fill in personal information and delivery information. 
        - The required fields are full name, email address, phone number, country, town or city and street address 1. 
        - The email has a validator where someone has to use a @. 
        - The country field is a dropdown with all countries. 
    - **Result:** Test pass. The Stripe payments are working fine. And the checkout form is valid. 

15. As a consumer, I want to receive a confirmation email of the order, so I know that the order is successfully received. 

    **Testing**
    - When the purchase is succeeded the consumer is redirected to the checkout success page. On the page is a order summary and it will mention that the consumer will receive an email confirmation. 
    - A email confirmation is sent to the consumer. The email is connected with gmail and when a purchase is made, a automatic confirmation is send from juan.stelling@gmail.com to the consumer.
    - **Result:** Test passed. When a consumer makes a purchase a confirmation email is send.

16. As a consumer, I want to create an account, so I can see my profile details and order history. 

    **Testing**
    - A consumer can create an account by signing up. 
    - The consumer can see the personal information, delivery information and the order history. 
    - The consumer can change the delivery information by updating the details and the consumer can change the password or manage email.
    - **Results:** Test passed. 

17. As a consumer, I want to know more about shipping, delivery, etc., so I know more about when and how my package arrives. 

    **Testing** 
    - The consumer can go the FAQ page where all information is displayed. The information is displayed in different sections, such as delivery and returns.
    - **Result:** Test passed. The consumer can find all relevant information in the FAQ. Otherwise the consumer can contact the company through the contact page if there are any questions left.

18. As a consumer, I want to know how I can return my package, so I know how I can return my packages if I want to. 

    **Testing**
    - The consumer can visit the returning policy page where all information about returns are showed.
    - **Result:** Test passed. The returning policy is displayed with the returing information.

<span id="returning-goals"></span>

### 1.3 Returning consumer goals 

19. As a returning consumer, I want to login and logout at my account anytime, so I can make an order quickly and so I can see my order history. 

    **Testing**
    - The returning consumer can login and logout through the links in the footer or profile icon in the navbar. 
    - The consumer has a double check for logging out.
    - **Result:** Test passed. The consumer can login and logout easily. 

20. As a returning consumer, I want to reset/change my password (if I forgot it), so I can get access to my profile. 

    **Testing**
    - The password can be changed by clicking the button on the profile page or by the login page. 
    - **Result:** Test passed. The password change functionality is working.

21. As a returning consumer, I want to be able to change my email, so I can have access to the profile with another email address.

    **Testing**
    - The returning consumer can change the email, add more emails and set a other primary email by clicking on the manage email button on the profile page. 
    - **Result:** Test passed. The consumer can manage the email through the allauth functionality.

<span id="admin-goals"></span>

### 1.4 Admin goals

23. As admin, I want to add, modify and delete products, so I manage the assortment of all products on the website. 

    **Testing**
    - The admin can add a product by clicking on the profile icon and add product. The admin gets a form to fill in and can add a product to the website. 
    - The admin can edit a product by clicking on the product detail page of the product and click on the edit link. The admin gets a filled in form with the details of the product. The details of the product can be updated and be saved. 
    - The admin can remove products by clicking on the product detail page of the product and click on the delete link. A notification will show if the admin is sure to delete the item. The product is deleted by clicking on delete again. 
    - **Results:** Test passed. The add, edit and delete functionallity is working as it should be.


<span id="automated-testing"></span>

## 2. Automated testing

### Testing apps
Automated testing is used to support the manual testing. The manual testing helped by testing mostly the back-end code with views, models and forms.
The unit tests can be found in the apps in the `test_models.py`, `test_views.py` and  `test_forms.py` files.

The tests provide an overall coverage of 41%. For in the future with more time and knowledge about Django testing, I would like to improve the coverage to a minimum of 80%.

### Lighthouse testing

I used the automated tool Lighthouse to test the quality of the web pages. 

**The result:** 
![Lighthouse testing](readme_img/lighthouse-testing.png)

- Note: The performance is rated with a score of 61.
    - The Largest Contentful Paint is coloured red and takes the most seconds. This metrics marks the time at which the largest text or image is painted. The score of this is so hight because loading the images is very slow. 
    - The images are the biggest issue. This has the most to do with the sizes of the original images. The original images are very different in size then on the website and the images are manipulated in a other size. Besides that the images don't have explicit width and height and the cache policy isn't effective.
    - Other issues are sources that are blocking the view, primary tread operations.  

<span id="validators"></span>

## 3. Validators

 - **[HTML Validator](https://validator.w3.org/):** No big errors to show.
    - I tested the HTML code by running my server locally and used view page source. This code I passed through the validator.

    **The following errors/warnings are showing**
    - Error Stray start tag tr, th and td: This error point to the newsletter form. The tr, th and td are automatically placed in the code from the `{{ form }}`.
    - Error Diplicate attribute name: This error point to the newsletter form. The name is double and is automatically set by `{{ form }}`.
    - Warning: the type attribute is unnecessary for JavaScript resource.

    **Result:** De rest of the code passed and there where no errors.

- **[CSS Validator](https://jigsaw.w3.org/css-validator/):** No big errors found.

    **Results:**
    - base.css: 1 error was found: .btt-button: invalid number: padding-right. The input for padding-right is: `calc(var(--bs-gutter-x)/ 2)`. I think this error occurs because I used the calc method.
    - checkout.css: no errors found
    - profiles.css: no errors found


- **[JS Hint](https://jshint.com/):** No errors found.
    
    **Results:**
    - Warnings 
        - 'template literal syntax' is only available in ES6 (use 'esversion: 6')
        - 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
    - Undefined variable: $

- **[Python validator | PEP8](http://pep8online.com/):** No errors found

    **Results:** No errors found!

---

<span id="responsiveness"></span>

## 4. Responsiveness 
- Responsiveness of the game is tested with [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).
- The game is tested on the following devices: 
    - Desktop: 1024px, 1366px, 1440px, 1600px and 1680px. 
    - Mobile & Tablet: Galaxy S5, iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 plus, iPhone x, iPad and  iPad Pro

![Responsiveness testing](readme_img/responsiveness_part1.png)
![Responsiveness testing  ](readme_img/responsiveness_part2.png)

### Notes
- The credit card input field is small in in mobile devices. The input consists of the creditcard number, the month, the CVC and the postcode. The creditcard number collapses to full in the other detauls in the input field.

---

<span id="browser-compatibility"></span>

## 5. Browser compatibility
![Browser compatibility](readme_img/browser-compatibility.png)

### Notes
- In Firefox and Safari are small bold words slightly less legible. The bold text is bolder than other browsers. I think this is due to the default boldness of the browsers Firefox and Sarafi.

--- 

<span id="other"></span>

## 8. Other

- During developing the website the debugger in `settings.py` was set to `debug=True`. The **debugger** showed errors and allowed me to find the errors quickly and to fix it.
- Custom error pages for error 400, 403, 404 and 500 are showing up in the same design as the website. 
- Url access/ security is test. The results: 
    - Pages that not exists are headed to a 404 page. 
    - Users who visit pages that require login while the user is not logged in will be directed to the login page.
    - Users who want to visit superuser access pages are getting redirected to the login page.

--- 

<span id="bugs"></span>

## 7. Bugs 

1. A bug was found in the interactive elements of the website. Certain elements didn't works especially collapse and dropdown elements.
    - I checked the links of Bootstrap and found out that I was using two versions of Bootstrap (Version 4 and version 5) at the same time. That why some elements didn't interact on the website. I fixed this bug to change every element to Bootstrap 5. 
2. A bug was found in with a unexpected 404 message on the products page in my 8000 port. 
    - This problem sometimes occurs when I added a product to the cart and then delete the product from the database. This action causes my 404 error. I have solved this bug by opening the Dev Tools and cleaned the site data. 

---

<span id="future-testing"></span>

## 8. Future testing 

Testing is a big part that has to be done after you created the project. For in the future with more time and knowlegde I would like to impove testing and make the quality of the project better. 
For in the future I would like to improve mostrly two things: 
- I would like to improve the automated testing with testing the apps looking at `views`, `models`, and `forms'. My coverage at this moment is 41% and I would like to impove this to a minimum of 80%.
- I would like to improve the results of the lighthouse scores, especially the performance score. The performance score is 66 and I would like to improve that to a minimum score of 90. Therefore I have to dive into the requirements and improve these elements.

---

[Go to README.md file](README.md).