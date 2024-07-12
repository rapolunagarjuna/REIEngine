# REIEngine
## Backend for Real Estate Investment Project CS682

API documentation: https://github.com/rapolunagarjuna/REIEngine/blob/main/documentation_for_REIEngine.pdf
Mobile App GitHub link: https://github.com/KaranChander/RealEstateMobile

![Screenshot 2024-07-12 at 1 25 57 AM](https://github.com/user-attachments/assets/d61e2da4-5d11-4efc-92f9-98bef112999e)
![Screenshot 2024-07-12 at 1 26 20 AM](https://github.com/user-attachments/assets/3a2b0cee-2aa3-4e9b-8568-dcd728b45b9c)
![Screenshot 2024-07-12 at 1 26 31 AM](https://github.com/user-attachments/assets/4988f5a2-2508-4177-ba79-62d3fc2e309b)

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
