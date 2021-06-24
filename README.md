# pictures_API

## Endpoints
* admin/

    Django admin 

* users/

    Displays list of all users. Accessible only for admin user
   * method: get
 
* pictures/upload/
    
    Allows to upload a picture
    * method: post
    * data: image file
    * returns: image id
* pictures/
    
    Lists all pictures of currently logged in user
    * method: get
    * returns list of user's picutres in the following format:
    
       {
        "id": numeric,
        
        "image": image file,
        
        "sizes": [
        
            {
        
                "id": numeric,
                
                "name":  string,
                
                "size": numeric
            },
            
            {
                
                "id": numeric,
                
                "name": string,
                
                "size": numeric
            
            }
        
        ]
    
    }
    
    where id in the outer dictionnary is the picture id
    
    sizes is a list of thumbnail sizes availables for a current user
    
    id and sizes[index] id would be used to generate a thumbnail

* pictures/<int:pic_pk>/<int:size_pk>/
    
    Allows generating a thumbnail
    * method: post
    * query params: 'pic_pk': id of picture returned by `pictures/`, 'size_pk': id of size returned by `pictures/`
    * data: {'link_validity': an integer between 300 and 30000, defaluts to 300}
    * returns a link to the generated thumbnail in the following format: 
    
      {
        "id": numeric,
        
        "link_validity": numeric,
        
        "url": url to image thumbnail   
      }
     
* auth/login
    
    Allows user to log in
  
* auth/logout

    Allows user to log out


## Technologies
Project is created with:
* Python 3.6
* Django 
* Django Rest Framework

For further details see `requirements.txt`

## Setup
To run the project locally:
* clone the repository locally
* create virtual environment using Python 3.6.9
* install `requirements.txt`
* replace placeholders in `pictures/example_settings.py` using your own creditentials
  * if you want to use sqlite3 database, comment DATABASES dictionnary
* rename `pictures/example_settings.py` to `pictures/local_settings.py` 
* run `python manage.py migrate`
* run `python manage.py make_plans` to create default plans
* if you want to create fake users to test the project, run `python manage.py fake_users`. Users names and passwords will display in terminal.
* run `python manage.py createsuperuser` to access Django admin endpoint
* run `python manage.py runserver`
