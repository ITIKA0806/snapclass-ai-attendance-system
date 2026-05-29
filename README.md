# SnapClass – AI-Powered Attendance Management System

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

SnapClass is an AI-powered classroom attendance management system built with Streamlit and Supabase that helps teachers automate attendance using **face recognition**, **voice verification**, and **QR-based classroom joining**.

Designed to reduce manual attendance effort while improving classroom efficiency, SnapClass provides separate teacher and student portals with a clean and interactive user experience.

---

## Demo Screenshot

### Teacher Dashboard – AI Attendance

![SnapClass Dashboard](assets/Dashboard_picture.jpg)

---

## Features

### Teacher Portal

* Secure teacher login
* Create and manage subjects
* Mark attendance using AI face recognition
* Voice-based attendance verification
* View attendance records by subject
* Generate QR code for classroom joining

### Student Portal

* Student registration
* Upload face image for attendance recognition
* Join class using QR code
* Voice attendance support
* Student dashboard experience

---

## Tech Stack

* Python
* Streamlit
* Supabase
* NumPy
* Pandas
* scikit-learn
* dlib
* librosa
* Resemblyzer
* bcrypt
* Pillow
* Segno QR Generator

---

## How It Works

1. Teacher creates a subject
2. Students join using QR code
3. Student uploads face image during registration
4. Teacher uploads classroom photo
5. AI detects and matches student faces
6. Attendance is recorded automatically
7. Voice verification can be used as an additional attendance method

---

## Getting Started

### Prerequisites

Before running locally, install:

* Python 3.10+
* pip
* Git

> ⚠️ **Note:** `dlib` may require `cmake` and Microsoft C++ Build Tools on Windows. If installation fails, refer to the official dlib installation guide.

---

### Installation

Clone the repository:

```bash
git clone https://github.com/ITIKA0806/snapclass-ai-attendance-system.git
```

Move into project folder:

```bash
cd snapclass-ai-attendance-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## Environment Variables

Create:

`.streamlit/secrets.toml`

Add:

```toml
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

---

## Project Structure

```bash
snapclass-ai-attendance-system/
│
├── assets/
├── src/
│   ├── components/
│   ├── database/
│   ├── pipelines/
│   ├── screens/
│   └── ui/
│
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Future Improvements

* Live attendance analytics dashboard
* Export attendance reports to Excel/PDF
* Email attendance summaries
* Mobile responsive interface
* Advanced attendance insights and analytics

---

## About This Project

SnapClass was built as a portfolio project to explore how AI can be applied in education technology to simplify classroom operations and modernize attendance workflows.

---

## Author

**Itika Singh**

Built with ❤️ using Python, Streamlit, Supabase & AI.

---

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.
