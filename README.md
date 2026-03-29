# 🛡️ Real-Time Intruder Detection System

A lightweight **webcam-based security system** that detects unauthorized viewers using computer vision and sends real-time alerts.

---

## 🚀 Features

* 🎥 Real-time webcam monitoring
* 🧠 Face detection using OpenCV (Haar Cascade)
* ⚠️ Detects multiple/unauthorized users
* 📸 Captures intruder images
* 📧 Sends email alerts with image attachment
* 🔒 Secure credential handling using `.env`

---

## 🧰 Tech Stack

* Python
* OpenCV
* NumPy
* smtplib (Email alerts)
* python-dotenv

---

## 📂 Project Structure

```
project/
│── main.py
│── alert.py
│── intruders/        # (ignored - stores captured images)
│── .env              # (ignored - stores credentials)
│── .gitignore
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/yourusername/repo-name.git
cd repo-name
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Create `.env` File

```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

### 4. Run the Project

```
python main.py
```

---

## 🔐 Security Note

* Do NOT push `.env` file to GitHub
* App password should be used instead of Gmail password

---

## 🧠 How It Works

1. Webcam continuously captures frames
2. OpenCV detects faces in each frame
3. If multiple faces are detected:

   * Image is captured
   * Email alert is triggered

---

## 📸 Future Improvements

* Face Recognition (known vs unknown users)
* Telegram / WhatsApp alerts
* Cloud deployment (AWS / Docker)
* Deep learning-based detection
* Web dashboard (MERN stack)

---

## 💡 Use Cases

* Laptop security
* Personal workspace monitoring
* Exam monitoring system
* Office surveillance prototype

---

## ⭐ Acknowledgements

* OpenCV Library
* Python Community

---

## 👨‍💻 Author

Dhruv Patel

---

## 📌 License

This project is for educational purposes.