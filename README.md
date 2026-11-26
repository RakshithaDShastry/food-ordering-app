# 🍕 Food Ordering App – Flask + Docker + Jenkins

A small food ordering web app built with **Flask (Python)**, containerised with **Docker**, and built as a hands-on **CI/CD practice project** using **Git** and **Jenkins**.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerised-2496ED?logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?logo=jenkins&logoColor=white)

---

## 📌 Features

- Browse a menu of 10 food items (Pizza, Burger, Pasta, Sandwich, French Fries, Noodles, Manchurian, Dosa, Ice Cream, Cold Drink) with prices and images
- Add items to a cart (stored in the user's session)
- Checkout page showing the ordered items and the total amount
- Cart is cleared automatically after checkout

## 🛠️ Tech Stack

| Area | Tools |
|------|-------|
| Backend | Python 3.11, Flask |
| Frontend | HTML (Jinja2 templates), CSS |
| Containerisation | Docker |
| CI/CD | Git, GitHub, Jenkins |

## 📁 Project Structure

```
food-ordering-devops/
├── app.py              # Flask app: routes for home, add to cart, checkout
├── requirements.txt    # Python dependencies (Flask)
├── Dockerfile          # Docker image definition
├── .gitignore
├── static/
│   ├── style.css       # Styling
│   └── images/         # Food item images
└── templates/
    ├── index.html      # Menu + cart page
    └── success.html    # Order confirmation page
```

## 🌐 Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Shows the menu, current cart and total |
| POST | `/add_to_cart` | Adds the selected item to the cart |
| GET | `/checkout` | Shows the order summary and clears the cart |

## 🚀 Getting Started

### Option 1: Run with Docker (recommended)

Prerequisite: [Docker](https://www.docker.com/get-started) installed.

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/food-ordering-devops.git
cd food-ordering-devops

# Build the image
docker build -t food-ordering-app .

# Run the container
docker run -p 5000:5000 food-ordering-app
```

Open **http://localhost:5000** in your browser.

### Option 2: Run locally with Python

Prerequisite: Python 3.11+

```bash
git clone https://github.com/YOUR-USERNAME/food-ordering-devops.git
cd food-ordering-devops

pip install -r requirements.txt
python app.py
```

Open **http://localhost:5000** in your browser.

## 🔄 CI/CD Pipeline (Jenkins)

The goal of this project was to automate the build and deployment of the app:

```
Git push ──▶ Jenkins pulls code ──▶ Docker image is built ──▶ Container is run
```

Below is a sample `Jenkinsfile` that implements this flow. Adjust it to match your own Jenkins setup.

```groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YOUR-USERNAME/food-ordering-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t food-ordering-app .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh 'docker rm -f food-ordering-app || true'
                sh 'docker run -d --name food-ordering-app -p 5000:5000 food-ordering-app'
            }
        }
    }
}
```

### Jenkins setup notes

1. Install Jenkins and make sure the Jenkins user can run Docker commands (`sudo usermod -aG docker jenkins`, then restart Jenkins).
2. Install the **Git** and **Pipeline** plugins.
3. Create a new **Pipeline** job and point it at this repository (or paste the pipeline script above).
4. Click **Build Now**, or add a GitHub webhook to trigger builds on every push.

## 📸 Screenshots

_Add screenshots here: the menu page, the cart, the checkout page, and a successful Jenkins build._

## ⚠️ Notes

- This is a learning project. There is no database or payment system; the menu is hardcoded in `app.py`.
- Before using it anywhere real, move the Flask `secret_key` into an environment variable and turn off `debug=True`.

## 🔮 Future Improvements

- Push the image to Docker Hub from the pipeline
- Add automated tests as a pipeline stage
- Add a database for menu items and orders
- User login and order history

## 📄 License

This project is for educational purposes.
