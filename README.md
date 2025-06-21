# basic_flask_arch

# Blog Website Deployment Guide

This guide provides step-by-step instructions to set up and deploy the blog website on a Linux server (Ubuntu/Debian). It covers installing dependencies, setting up Python and Docker, configuring Nginx, and enabling SSL.

---

## 1. Prerequisites

Update your package list and install required packages:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git docker.io nginx
sudo apt install docker-compose
sudo systemctl enable docker
sudo systemctl start docker
```

---

## 2. Nginx Setup

Install and start Nginx (if not already done):

```bash
sudo apt install nginx
sudo systemctl start nginx
```

---

## 3. Clone the Repository

Clone the project repository:

```bash
sudo git clone https://github.com/dutta-Piyush/blogWebsite.git
# If the repo is private, add your SSH key to the instance and use the SSH URL
```

---

## 4. Python Virtual Environment Setup

Create and activate a Python virtual environment:

```bash
sudo python3 -m venv .venv
source .venv/bin/activate
```

**Note:**
- Check the ownership of the `.venv` folder. If it is owned by `root`, change ownership to your user:
  ```bash
  sudo chown -R $USER:$USER .venv
  ```

---

## 5. Install Python Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## 6. Docker Setup

Start the Docker containers:

```bash
docker-compose -f docker-compose.dev.yml up -d
```

**Note:**
- Ensure you have the proper permissions to run Docker commands. You may need to add your user to the `docker` group:
  ```bash
  sudo usermod -aG docker $USER
  ```
  Then log out and log back in.

---

## 7. Database Initialization

Create the tables in the database:

```bash
python3 -m src.utils.db_init
```

---

## 8. Running the Application

### Development Mode
```bash
python3 app.py
```

### Production (Linux)
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Production (Windows)
```bash
waitress-serve --listen=0.0.0.0:5000 app:app
```

---

## 9. Nginx Configuration

Edit the default Nginx site configuration:

```bash
cd /etc/nginx
sudo nano /etc/nginx/sites-available/default
```

Set your `server_name`:
```
server_name piyushdutta.moo.com.mooo.com www.piyushdutta.moo.com.mooo.com;
```

Replace everything inside the `location {}` block with:

```
location / {
    proxy_pass http://localhost:5000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_cache_bypass $http_upgrade;
}
```

Reload Nginx:
```bash
sudo systemctl reload nginx
```

---

## 10. Domain & DNS

Check your domain DNS resolution:

```bash
nslookup piyushdutta.mooo.com
```

Expected result:
```
Non-authoritative answer:
Server:  UnKnown
Address:  2a02:8100:c0:249::4:1101

Name:    piyushdutta.mooo.com
Address:  63.177.241.93
```

---

## 11. SSL Certificate Setup (Let's Encrypt)

Add the Certbot repository and install Certbot for Nginx:

```bash
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python3-certbot-nginx
```

Obtain and install your SSL certificate:

```bash
sudo certbot --nginx -d piyushdutta.mooo.com -d www.piyushdutta.mooo.com
```

**Renewal:**
Certificates are valid for 90 days. Test renewal with:
```bash
sudo certbot renew --dry-run
```

---

## Notes
- Always check file and directory permissions, especially for your virtual environment and Docker.
- If using a private repository, ensure your SSH keys are set up on the server.
- Adjust the `server_name` and proxy settings in Nginx as needed for your domain.
- For any issues, check the logs for Docker, Nginx, and your Flask app.