# Fastapi-as-Service-Reverse-proxy
# Deployed the app as a service 
1. create the main.py using fatsapi
2. sudo nano /etc/systemd/system/fastapi.service
   [Unit]
    Description=FastAPI Service
    After=network.target
    [Service]
    User=ubuntu
    Group=ubuntu
    WorkingDirectory=/var/www/html/fastapi
    ExecStart=/usr/bin/python3 /home/ubuntu/.local/bin/uvicorn main:app --host 0.0.0.0  --port 8000 --reload
    
    [Install]
    WantedBy=multi-user.target
3. sudo systemctl enable fastapi.service
4. sudo systemctl start fastapi.service
5. point ip:8000 in browser
 For Reverse Proxy
1. sudo nano /etc/apache2/site-available/fastapi.conf
<VirtualHost *:80>
    ServerName domain_name

    ProxyRequests Off
    ProxyPreserveHost On

    <Proxy *>
        Require all granted
    </Proxy>

    ProxyPass / http://52.66.235.82:8000/
    ProxyPassReverse / http://52.66.235.82:8000/
</VirtualHost>








