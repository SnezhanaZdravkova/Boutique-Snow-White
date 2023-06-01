![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


# [WELCOME TO BOUTIQUE SNOW WHITE SITE](https://boutique-snow-white.herokuapp.com/)
This is a full-stack framework project, B2C e-commerce store, built using Django, Python, HTML and CSS. My goal is to create a functioning and responsive website, that allows users to view, select and buy products.
The site's objective is to allow users to browse/view or buy products weather they are a Registered user or not.
The payment system uses Stripe. This project has been built for educational purposes.
GitHub name repository [here](https://github.com/SnezhanaZdravkova/Boutique-Snow-White)

<!-- # Contents

- [User Experience(UX)](#user-experience-ux)
- [Languages](#languages) -->

# User Experience (UX)
- A visitor to Boutique Snow White would be someone who is most likely an adult who is interested in buying Fashion products and high-end interior or Trendy Clothing design services.

## User Stories
### Epic 1 - Viewing and Navigation
* As a/an Shopper I want to be able to view a list of products so that I can select some to purchase.
* As a/an Shopper I want to be able to view individual product details so that I can identify the price, description, product rating, product image and available sizes.
* As a/an Shopper I want to be able to quicly identify deals, clearance items and special offers so that I can take advantage of special savings on products I'd like to purchase.
* As a/an Shopper I want to be able to easily view the total of my purchases at any time so that I can avoid spending too much.
### Epic 2 - Registration and User Accounts
* As a/an Site User I want to be able to easily register for an account so that I can have a personal account and be able to view my profile.
* As a/an Site User I want to be able to easily login and logout so that I can access my personal account information.
* As a/an Site User I want to be able to easily recover my password in case I forget it so that I can recover access to my account.
* As a/an Site User I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful.
* As a/an Site User I want to be able to have a personalized user profile so that I can view my personal order history and order confirmations, and save my payment information.
### Epic 3 - Sorting and Searching
* As a/an Shopper I want to be able to sort the list of available products so that I can easily identyfy the best rated, best priced and categorically sorted products.
* As a/an Shopper I want to be able to sort a specific category of pruducts so that I can find the best-priced or best-rated product in a specific category, or sort the products in that category by name.
* As a/an Shopper I want to be able to sort multiple categories of products simultaneously so that I can find the best-priced or the best-rated products across broad categories, such as "shirts" or "dresses".
* As a/an Shopper I want to be able to search for a product by name or description so that I can find a specific product I'd like to purchase.
* As a/an Shopper I want to be able to easily see what I have searched for and the number of results so that I can quickly deside whether the product I want is available.
### Epic 4 - Purchasing and Checkout
* As a/an Shopper I want to be able to Easily select the size and quantity of a product when purchasing it so that I can ensure I don't accidentally select the wrong product quantity or size.
* As a/an Shopper I want to be able to view items in my bag to be purchased so that I can identify the total cost of my purchas and all items that I will receive.
* As a/an Shopper I want to be able to adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout.
* As a/an Shopper I want to be able to easily enter my paiment information so that I can check out quickly and with no hassles.
* As a/an Shopper I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
* As a/an Shopper I want to be able to view an order confirmation after checkout so that I can veryfy that I haven't make any mistakes.
* As a/an Shopper I want to be able to receive an email confirmation after checkout so that I can keep the confirmation of what I've purchased for my records.
### Epic 5 - Admin and Store Management
* As a/an Store Owner I want to be able to add a product so that I can add new items to my store.
* As a/an Store Owner I want to be able to edit/update a product so that I can change product prices, descriptions, images, and other product criteria.
* As a/an Store Owner I want to be able to delete a product so that I can remove items that are no longer for sale.
* As a/an Store Owner I want to be able to add services so that I can users can see if there is new service.
* As a/an Store Owner I want to be able to edit/delete services so that I can update or remove service if it no longer practice.
* As a/an Store Owner I want to be able to remove testimonial so that I can when we a no longer providing the services they are about.
* As a/an Store Owner I want to be able to add project images so that I can so users can see our previous work or products.
### Epic 6 - User Interaction
* As a Site User I can submit an enquiry form so that I can enquire about a design consultation.
* As a Site User I can add / edit / delete a testimonial in relation to a consultation I received so that I can give my feedback.
* As a Site User I can sign up for the website's newsletter so that I can keep up to date with new products and promotions.

## Data Model
- I used principles of Object-Oriented Programming throughout this project and Django's Class-Based Generic Views.

-  Django AllAuth was used for the user authentication system.

-  The diagram below details the database schema: (to be added)

## User Story Testing
> Testing Users Stories form (UX) Section

## Superuser / Admin

> As a site Admin I can create, edit and delete products so that I can manage the site content
> As a site Admin I can access the admin panel so that I can manage categories and products
> As a site Admin I can log out of the admin panel so that I can disconnect from the website
This was tested by accessing the Django Admin Panel. By creating a Superuser we can access the Django Admin Panel where the administrator can perform all the CRUD functionalitis

## User Interaction

> As a logged-in User I can wiew all the categories, products and services
> As a User I can view the rating on the products so that I can see which product is the most popular
> As a User I can view the price, description and the image on the product
> As a User I can celect and buy the products I like

### Login/Register

> As a User I can register for an account so that I can interact with the site content
> As a User I can log in/out off my account if I wish so that I can connect or disconnect from the website
> As a User I can easily see if I'm logged-in or logged-out so that I can be sure what my status is

## Navigation

> As a User I can easily navigate through the site so that I can view desired content
> As a User I can see the most loved producs so that I can quickly find inspiration and see which product is most famous

## Balsamiq Wireframes
Wireframes are extremely basic and did not incorporate all App pages. Wireframes were used as boiler plates to start the app design many updates and alterations have been made after the basic Wireframes were used to get started on the App.
<details><summary>Balsamiq Wireframes</summary>

Home Page ![home page](../Boutique-Snow-White/media/readme-images/home-page-sw-2.jpg)

All Products ![all products image](../Boutique-Snow-White/media/readme-images/all-products-sw_10.png)

Services ![Servises](../Boutique-Snow-White/media/readme-images/services-page-2.jpg)

Testimonials ![Testimonials](../Boutique-Snow-White/media/readme-images/testimonials-2.jpg)

Contact Us Form ![Contact Us Form](../Boutique-Snow-White/media/readme-images/contact-form-1.jpg)

Mobile Phone ![Mobile Phone](../Boutique-Snow-White/media/readme-images/mobile-sw-2.jpg)

</details>

## Bugs and Issues

## Deployment - Heroku
This project was deployed using Github, Heroku and ElephentSQL.

### Github
To create a new repository I took the following steps:

> Logged into Github.
> Clicked over to the 'repositories' section.
> Clicked the green 'new' button. This takes you to the create new repository page.
> Once there under 'repository template' I chose the code institute template from the dropdown menu.
> I input a repository name then clicked the green 'create repository button' at the bottom of the page.
> Once created I opened the new repository and clicked the green 'Gitpod' button to create a workspace in Gitpod for editing.

## Create the Heroku App:
> Log in to Heroku or create an account.
> On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
> Enter a unique and meaningful app name.
> Next select your region.
> Click on the Create App button.

## Attach the ElephentSQL database:
> Copy the DATABASE_URL located in Config Vars in the Settings Tab.
> Prepare the environment and settings.py file:
> In your GitPod workspace, create an env.py file in the main directory.
> Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
> Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
> Comment out the default database configuration.
> Save files and make migrations.

> Link the file to the templates directory in Heroku
> Change the templates directory to TEMPLATES_DIR
> Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']
> Create files / directories
> Create requirements.txt file
> Create three directories in the main directory; media, storage and templates.
> Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi
> Update Heroku Config Vars
> Add the following Config Vars in Heroku: (to be added)

# AWS Set Up

## AWS S3 Bucket
### Create an AWS account.
> From the 'Services' tab on the AWS Management Console, search 'S3' and select it.
> Click 'Create a new bucket', give it a name(match your Heroku app name if possible), and choose the region closest to you.
> Under 'Object Ownership' select 'ACLs enabled' and leave the Object Ownership as Bucket owner preferred.
> Uncheck block all public access and acknowledge that the bucket will be public.
> Click 'Create bucket'.
> Open the created bucket, go to the 'Properties' tab. Scroll to the bottom and under 'Static website hosting' click 'edit' and change the Static website hosting option to 'enabled'. Copy the default values for the index and error documents and click 'save changes'.
> Open the 'Permissions' tab, locate the CORS configuration section and add the following code:
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
> In the 'Bucket Policy' section and select 'Policy Generator'.
> Choose 'S3 Bucket Policy' from the type dropdown.
> In 'Step 2: Add Statements', add the following settings:
>> Effect: Allow
>> Principal: *
>> Actions: GetObject
>> ARN: Bucket ARN (copy from S3 Bucket page)
>> Click 'Add Statement'.
> Click 'Generate Policy'.
> Copy the policy from the popup that appears
> Paste the generated policy into the Permissions > Bucket Policy area.
> Add '/*' at the end of the 'Resource' key, and save.
> Go to the 'Access Control List' section click edit and enable List for Everyone (public access) and accept the warning box.

## IAM
> From the 'Services' menu, search IAM and select it.
> Once on the IAM page, click 'User Groups' from the side bar, then click 'Create group'. Choose a name and click 'Create'.
> Go to 'Policies', click 'Create New Policy'. Go to the 'JSON' tab and click 'Import Managed Policy'.
> Search 'S3' and select 'AmazonS3FullAccess'. Click 'Import'.
> Get the bucket ARN from 'S3 Permissions' as per above.
> Delete the '*' from the 'Resource' key and add the following code into the area:
"Resource": [
    "YOUR-ARN-NO-HERE",
    "YOUR-ARN-NO-HERE/*"
]
> Click 'Next Tags' > 'Next Review' and then provide a name and description and click 'Create Policy'.
> Click'User Groups' and open the created group. Go to the 'Permissions' tab and click 'Add Permissions' and then 'Attach Policies'.
> Search for the policy you created and click 'Add Permissions'.
> You need to create a user to put in the group. Select users from the sidebar and click 'Add user'.
> Give your user a user name, check 'Programmatic Access'.
> Click 'Next' and select the group you created.
> Keep clicking 'Next' until you reach the 'Create user' button and click that.
> Download the CSV file which contains the AWS_SECRET_ACCESS_KEY and your AWS_ACCESS_KEY_ID needed in the  Heroku variables as per above list and also in your env.py.

## Connecting S3 to Django
> Go back to your IDE and install 2 more requirements:
- pip3 install boto3
- pip3 install django-storages
> Update your requirements.txt file by typing pip3 freeze --local > requirements.txt and add storages to your installed apps.
> Create an if statement in settings.py
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

> Then add the line

- AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.eu-west-1.amazonaws.com' to tell django where our static files will be coming from in production.
> Create a file called custom storages and import both our settings from django.con as well as the s3boto3 storage class from django storages.

- Create the following classes:

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
> In settings.py add the following inside the if statement:
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

- and then add the following at the top of the if statement:
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
> Go to S3, go to your bucket and click 'Create folder'. Name the folder 'media' and click 'Save'.
- Inside the folder, click 'Upload', 'Add files', and then select all the images that you are using for your site.
- Then under 'Permissions' select the option 'Grant public-read access' and click upload.
Your static files and media files should be automatically linked from django to your S3 bucket.

## Deploy
> NB: Ensure in Django settings, DEBUG is False
> Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
> Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
> Click View to view the deployed site.
The site is now live and operational.

## Languages
- HTML
- CSS
- PYTHON
- JavaScript
- Frameworks - Libraries - Programs Used
- Django: Main python framework used in the development of this project
- Django-allauth: authentication library used to create the user accounts
- ElephentSQL was used as the database for this project
- Heroku - was used as the cloud based platform to deploy the site on
- Chrome Dev Tools - Used for overall development and tweaking, including testing responsiveness and performance
- Font Awesome - Used for icons
- GitHub - Used for version control and agile tool
- Google Fonts - Used to import and alter fonts on the page
- W3C - Used for HTML & CSS Validation
- PEP8 Online - used to validate all the Python code
- Crispy Forms used to manage Django Forms
- AWS: the image hosting service used to upload images
- Bootstrap 4: CSS Framework for developing responsiveness and styling

## Credits
>-  Code Institute - 'Boutique Ado' project helped me with product details page and pagination
>-  Django documentation - also helped me with pagination and other problems
>-  To get the Django framework installed and set up I followed the Code institutes Django Blog cheatsheet
>-  W3Schools
>-  Django Docs
>-  Stack Overflow
>-  Bootstrap

## Acknowledgements
- Many thanks to my mentor Ronan McClelland for his support and advice
- Thanks to The Code Institute slack community
- Thanks to my colleague Tara Helberg for helping and inspiring
- Thanks AliOKeeffe for helping and inspiring me!