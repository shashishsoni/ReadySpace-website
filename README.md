<h1>ReadySpace-website</h1>

<h2>BigProject is a Django-based web application utilizing Wagtail CMS for content management. The project is set up with a variety of features, including flexible page management, user authentication, and dynamic forms.</h2>

<h3>Features</h3>

    Django 5.0.1 for backend functionality
    Wagtail CMS for content management and admin interface
    Custom models integrated with Wagtail ModelAdmin
    Responsive design using SCSS and static file management
    SQLite as the database (can be updated for production)

<h3>Installation</h3>

++Prerequisites++

    Python 3.x
    Django 5.x
    Wagtail CMS
    Virtual environment (optional but recommended)
    
++Steps++

Clone the repository:

    git clone https://github.com/shashishsoni/BigProject.git
    cd BigProject
    
Set up a virtual environment:

    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies: Install the necessary packages using the requirements.txt file.

    pip install -r requirements.txt
    
Run migrations: Apply Django and Wagtail migrations to set up the database.

    python manage.py migrate
    
Create a superuser: You need a superuser to access the Wagtail admin interface.

    python manage.py createsuperuser
    
Run the server: Start the development server and open the site in your browser.

    python manage.py runserver
    
Access the admin: Visit http://localhost:8000/admin to log in to the Wagtail admin interface.

++++++++Wagtail ModelAdmin Integration++++++++ !Imp

Important Notice:

The built-in wagtail.contrib.modeladmin is deprecated. This project uses the updated version from wagtail-nest/wagtail-modeladmin.

Steps to Use Wagtail ModelAdmin:

Install Wagtail ModelAdmin from the forked repository:

    pip install git+https://github.com/wagtail-nest/wagtail-modeladmin.git

Update INSTALLED_APPS in settings.py or base.py:

    INSTALLED_APPS = [
        'wagtail_modeladmin',  # Instead of wagtail.contrib.modeladmin
        # Other apps...
    ]
    
Set up your model with ModelAdmin: Define your ModelAdmin class for any custom models you want to manage via Wagtail.

++Project Structure++

    home/: Contains templates for the homepage and core pages.
    search/: Implements site-wide search functionality.
    services/: For service-related pages and models.
    flex/: Flexible content pages that can be edited by admins.
    static/: Static files like SCSS, JavaScript, and images.
    templates/: The Django and Wagtail template files.
    
++Database++

The project uses SQLite for development, which can be changed for production environments. To switch databases, update the DATABASES section in settings.py.

++Static and Media Files++

Static files: All CSS, JavaScript, and images are served from the static directory.

Media files: Uploaded media files are served from the media directory.

To collect static files for production:

    python manage.py collectstatic
    
++Wagtail Settings++

Wagtail Site Name: The site name is set to "BigProject". You can change this in the Wagtail admin under the settings section.

Deployment

For production:

    Set up a secure environment with a robust database (e.g., PostgreSQL).
    Use whitenoise for static file management.
    Set DEBUG=False in settings.py and configure allowed hosts.
    
++Contributing++

Contributions are welcome! To contribute:

Fork the repository.

    Create a new branch for your feature (git checkout -b feature-branch).
    Commit your changes (git commit -m 'Add new feature').
    Push to the branch (git push origin feature-branch).
    Open a pull request.

<h1>This is the final rendering Output of the Code</h1>

![Rocket Maintenance - ReadySpace](https://github.com/user-attachments/assets/9c187da8-1b28-47da-bc62-0d22349c01e0)
![Services - ReadySpace](https://github.com/user-attachments/assets/f48f3ac5-b8c7-400a-813b-07db24fbe13d)
![ReadySpace  Igniting Dreams, Exploring the Cosmos - ReadySpace](https://github.com/user-attachments/assets/503a9fd3-b8a5-43f1-90bb-c5c9c639c653)
![Contact Us - ReadySpace](https://github.com/user-attachments/assets/dd1385cf-0099-4b19-b03b-61aa7dc65c75)
