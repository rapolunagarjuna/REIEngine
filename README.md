# REIEngine
## Backend for Real Estate Investment Project CS682

API documentation: https://github.com/rapolunagarjuna/REIEngine/blob/main/documentation_for_REIEngine.pdf

### Setup a virtual environment
python3 -m venv venv

### start the virtual environment
source venv/bin/activate

### Run server
flask run

## while deploying on to the cloud, create a ngnix server
## use the flask_app.config file to configure the ngnix server
sudo nano /etc/nginx/conf.d/flask_app.conf

## Now, your Nginx configuration is set up to forward requests to Gunicorn, and Gunicorn is running your Flask application.
sudo systemctl restart nginx


## then run the nohup, gunicorn command to create the processes in the background
nohup gunicorn -w 4 -b 127.0.0.1:5000 app:app &

## in order to stop the processes do 
pgrep -f "gunicorn -w 4 -b 127.0.0.1:5000 app:app"

## now using the PID Kill them one by one
kill <PID>
