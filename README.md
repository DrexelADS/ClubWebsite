# Drexel ADS Website - README

## Instructions:

### Run locally:
1. If you are running the project for the first time:
    - Make sure you have ```python3``` installed.
    - Create a virtual environment using: ```python3 -m venv drexel_ads_website```.
    - Install the project dependencies using: ```pip3 install -r requirements.txt```.
2. If the virtual environment already exists:
    - You should see a directory named ```drexel_ads_website``` in your current working directory.
    - If yes, run: ```source drexel_ads_website/bin/activate``` to activate the virtual environment.
3. Run: ```export DJANGO_SETTINGS_MODULE=ClubWebsite.settings``` in your terminal.
4. If all the steps were done correctly, you should be able to run the following commands without any error:
    - ```python3 manage.py makemigrations```
    - ```python3 manage.py migrate```
    - ```python3 manage.py runserver 0.0.0.0:8084```
5. If the commands are executed successfully, the project would serve locally at ```0.0.0.0:8084``` and should be accessible using your browser.
6. <b>Note</b>: SQLite will be used in the development mode. We will be using a Postgres instance when we put it in prod. Don't worry about it for now. Everything will be handled by settings file.


Send a message to Vivek Khimani
