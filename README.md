# 🚀 Data Redundancy Removal System

A cloud-hosted Flask web application that detects and prevents duplicate or false-positive user data entries using intelligent validation techniques.

## 🌐 Live Demo

https://data-redundancy-removal-system-98bz.onrender.com

---

# 📌 Project Overview

The **Data Redundancy Removal System** is designed to improve database accuracy and efficiency by preventing duplicate and similar user records from being stored in the system.

The application validates user data before insertion and classifies entries as:

* ✅ Unique Data
* ❌ Duplicate Data
* ⚠️ False Positive / Similar Data

This project was developed as part of the **CodeAlpha Cloud Computing Internship**.

---

# ✨ Features

## ✅ User Registration System

* Register users using name and email.

## ✅ Duplicate Detection

* Prevents exact duplicate email entries.

## ✅ False Positive Detection

* Detects highly similar email usernames using Python similarity matching.

## ✅ Cloud Deployment

* Hosted live on Render cloud platform.

## ✅ Registered Users Dashboard

* Displays all registered users dynamically.

## ✅ Delete User Functionality

* Remove users from database.

## ✅ Registration Timestamp

* Stores date and time of registration.

## ✅ Dynamic Flash Messages

* Success and error notifications using Flask flash messaging.

## ✅ Responsive UI

* Bootstrap-based professional user interface.

## ✅ Custom Branding

* Integrated custom logo and favicon.

---

# 🛠️ Technologies Used

| Technology   | Purpose             |
| ------------ | ------------------- |
| Python       | Backend Programming |
| Flask        | Web Framework       |
| SQLite       | Database            |
| HTML5        | Frontend Structure  |
| CSS3         | Styling             |
| Bootstrap 5  | Responsive UI       |
| Jinja2       | Template Rendering  |
| Render       | Cloud Deployment    |
| Git & GitHub | Version Control     |

---

# 🧠 False Positive Detection Logic

The system uses Python's `SequenceMatcher` from the `difflib` library to compare email usernames and identify highly similar records.

### Example:

| Existing Email                        | New Email                                   | Result         |
| ------------------------------------- | ------------------------------------------- | -------------- |
| [het@gmail.com](mailto:het@gmail.com) | [het123@gmail.com](mailto:het123@gmail.com) | False Positive |
| [abc@gmail.com](mailto:abc@gmail.com) | [xyz@gmail.com](mailto:xyz@gmail.com)       | Unique         |

---

# 📂 Project Structure

```bash
Data_Redundancy_Removal_System/
│
├── app.py
├── requirements.txt
├── Procfile
├── README.md
│
├── static/
│   ├── style.css
│   └── logo.png
│
├── templates/
│   ├── index.html
│   └── users.html
│
└── database.db
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/HetGangani/CodeAlpha_DataRedundancyRemovalSystem.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd CodeAlpha_DataRedundancyRemovalSystem
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Application

```bash
python app.py
```

---

# ☁️ Deployment

The application is deployed using:

* Render Cloud Platform

Live Deployment:
https://data-redundancy-removal-system-98bz.onrender.com

---

# 📸 Screenshots

## 🏠 Homepage

<img width="1920" height="1079" alt="Screenshot 2026-05-19 115249" src="https://github.com/user-attachments/assets/70d8cb9b-e4e8-4642-9699-678ecae6ba0e" />


## 👥 Registered Users Dashboard

<img width="1916" height="1080" alt="Screenshot 2026-05-19 115824" src="https://github.com/user-attachments/assets/376972f6-f4aa-4204-8f95-5e496c4990d6" />


## ⚠️ False Positive Detection

<img width="1920" height="548" alt="Screenshot 2026-05-19 115919" src="https://github.com/user-attachments/assets/748e9753-b630-42c9-a52d-341d5e903102" />
<img width="1920" height="640" alt="Screenshot 2026-05-19 115928" src="https://github.com/user-attachments/assets/2cacd584-27cb-4bc6-ae22-b096a6232215" />



---

# 🎯 Future Improvements

* PostgreSQL Integration
* User Authentication System
* Search & Filter Functionality
* Export Users to CSV
* Machine Learning Based Similarity Detection
* REST API Integration

---

# 👨‍💻 Developer

**Het Gangani**

GitHub:
https://github.com/HetGangani

---

# 📜 License

This project is developed for educational and internship purposes.
