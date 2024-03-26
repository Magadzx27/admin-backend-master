

# AI CompuMall Django Backend

## Getting Started

Make  sure you have installed Python3 and XAMPP Server.

2. Install virtualenv if not exist

   ```bash
   py -m pip install --user virtualenv
   ```

3. Clone Backend Django Repo if you donot have the project folder

   ```bash
   git clone https://gitlab.com/filbertdev/ai-compumall/admin-backend.git
   cd admin-backend
   ```

4. Create virtual environment 

   ```bash
   py -m venv env
   ```

5. Activating a virtual environment

   ```bash
   .\env\Scripts\activate
   ```
   
6. Install Requirements 
   
    ```bash
    pip install -r requirements.txt
    ```
   
7. Build your database
    ```bash
    python manage.py migrate
    ```
     
8. Start Django Server and browse localhost:8000 for Swagger 
   
    ```bash
    python manage.py runserver
    ```
        
        
## To activate email on localhost, Please install [Test mail server](https://toolheap.com/test-mail-server-tool/users-manual.html?fbclid=IwAR3gscSCqQ1kRiiCtLx1YU2WQprxxeaS3yl-vRfZb09lt0fIHJwSz5TGnWY) and change listening port to 1025

