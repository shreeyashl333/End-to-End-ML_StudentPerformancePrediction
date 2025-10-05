#  End-to-End ML Project: Student Performance Prediction

###  Objective  
Predict student scores using various **regression techniques** and identify the most accurate model for performance prediction.

---

##  Dataset  
**File:** `stud.csv`  
Contains student-related data used to build and evaluate regression models.

### 2. Dataset information

- gender : sex of students -> (Male/female)

- race/ethnicity : ethnicity of students -> (Group A, B,C, D,E)

- parental level of education : parents' final education ->(bachelor's degree,some college,master's degree,associate's degree,high school)

- lunch : having lunch before test (standard or free/reduced)

- test preparation course : complete or not complete before test

- math score

- reading score

- writing score

---

## 🧩 Project Workflow  

### **1. Environment Setup**  
- Created a local environment  
- Defined dependencies in `setup.py` and `requirements.txt`  

### **2. Repository Setup**  
- Initialized and structured the project in **GitHub**

### **3. Core Utilities**  
- Implemented **Logging**, **Custom Exceptions**, and a **Utils** module (helper functions)

### **4. EDA and Model Training**  
- Performed **Exploratory Data Analysis (EDA)**  
- Trained multiple regression models within Jupyter notebooks  

### **5. Modular Code Implementation (Pipelines)**  
- **Data Ingestion** – Loading and splitting raw data  
- **Data Transformation** – Handling missing values, encoding, scaling  
- **Model Trainer** – Model selection, training, and **hyperparameter tuning**  
- **Prediction Pipeline** – Generating predictions on unseen data  

### **6. Flask Web Application**  
- Built a simple **Flask app** for real-time prediction

### **7. Containerization (Docker)**  
- Created a **Dockerfile** for deployment on:
  - **AWS ECR**
  - **Azure ACR**

### **8. Deployment**  
- **Localhost** testing  
- **AWS Elastic Beanstalk** (via GitHub → CodePipeline → Elastic Beanstalk)  
- **AWS EC2** with ECR integration  
- **Azure** deployment using ACR → Web App with Container  

---

##  Tech Stack  
- **Languages:** Python  
- **Frameworks/Libraries:** Scikit-learn, Flask  
- **Tools:** Docker, AWS, Azure  
- **Version Control:** Git & GitHub  
