# Sensor Fault Detection

This project implements a machine learning solution for detecting faults in sensors used in industrial processes. The system analyzes sensor data to identify potential malfunctions and anomalies, helping prevent equipment failures and optimize maintenance schedules.

## Video Demo

Here's a video demo of the project:

https://github.com/user-attachments/assets/503d0c0f-02df-4679-8804-612f46901744

## Table of Contents
- [Problem Statement](#problem-statement)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Pipeline](#data-pipeline)
- [Contributing](#contributing)

## In summary
The project aims to build a classification model that can accurately detect faults in sensors based on various readings and measurements. Early detection of sensor faults can help prevent costly equipment failures and reduce downtime in industrial processes.

### Sensor Fault Detection Project

**Introduction:**
In electronics, a wafer (also called a slice or substrate) is a thin slice of semiconductor, such as crystalline silicon (c-Si), used for the fabrication of integrated circuits and, in photovoltaics, to manufacture solar cells. The wafer serves as the foundation for the construction of other components and microelectronic devices.

**Fabrication:**
The process of creating integrated circuits (ICs) on semiconductor material, typically silicon, involves multiple steps to build the tiny electronic circuits used in almost all modern electronic devices, such as computers, smartphones, and other gadgets.

**Multiple Wafers for Mass Production:**
In semiconductor manufacturing, many wafers are processed simultaneously to produce a large number of integrated circuits. Each wafer typically contains hundreds or even thousands of identical circuits (chips) that are later cut out and used in electronic devices.

### Problem Statement

**Objective:**
Develop a machine learning model to predict the quality of semiconductor wafers as either "Good" or "Bad" based on sensor readings collected during the fabrication process.

**Details:**
- **Inputs (Features):** The dataset consists of 590 sensor readings (Sensor-1, Sensor-2, ..., Sensor-590) for each wafer. These readings capture various environmental and process parameters during the wafer's fabrication.
- **Output (Target):** The target variable is labeled as "Good/Bad," where 1 indicates a "Good" wafer, and -1 indicates a "Bad" wafer.
- **Goal:** Build a classification model that can accurately predict whether a wafer is good or bad based on sensor readings, helping in the early detection of defective wafers, improving yield, and reducing waste in semiconductor manufacturing.

### Machine Learning Task

**Type:** Supervised Learning (Classification)  
**Model Type:** Binary Classification Model

### Approach

1. **Post-Production Inspection:**
   - **Manual or Automated Testing:** Without real-time prediction, rely on manual or automated inspection and testing of wafers after the entire fabrication process is completed.
   - **Delays in Detection:** Faults are detected only after the wafer has passed through all production stages, potentially leading to wasted resources if a large batch is found defective late in the process.

2. **Batch Testing:**
   - **Stopping Production:** Halt production for sample testing if a fault is suspected, involving detailed inspection and testing of a wafer batch.
   - **Production Downtime:** Stopping production for testing can lead to significant downtime, reducing overall efficiency and potentially causing delays in product delivery.

3. **Real-Time Data Collection and Monitoring:**
   - **Sensor Integration:** Install sensors at various stages of the wafer fabrication process to collect real-time data on critical parameters like temperature, pressure, gas flow, chemical composition, and other relevant metrics.
   - **Data Infrastructure:** Set up a robust data infrastructure to collect, store, and process sensor data in real time using cloud-based systems or on-premise solutions with sufficient processing power and low latency.

4. **Model Development and Training:**
   - **Data Preprocessing:** Clean and preprocess the sensor data to remove noise and outliers. Feature engineering may be necessary to extract meaningful features from raw sensor data.
   - **Model Selection:** Choose appropriate machine learning algorithms for the classification task. Options include: 
     - **Logistic Regression:** For a simple and interpretable model.
     - **Random Forest or Gradient Boosting:** For handling complex interactions between features.
     - **Neural Networks:** For capturing intricate patterns in large datasets.
   - **Model Training:** Train the model on historical data where the quality of the wafers (good or bad) is already known. Use techniques like cross-validation to ensure the model generalizes well to new data.
   - **Hyperparameter Tuning:** Optimize the model's hyperparameters to improve accuracy, precision, and recall.

5. **Real-Time Prediction:**
   - **Deploy the Model:** Deploy the trained ML model in the production environment where it can receive real-time sensor data.
   - **Real-Time Decision Making:** The model continuously analyzes incoming sensor data and predicts whether each wafer is likely to be good or bad. Immediate actions based on predictions include:
     - **Flagging Faulty Wafers:** Automatically flagging wafers predicted to be faulty for further inspection or removal from the production line.
     - **Adjusting Process Parameters:** Triggering adjustments in the manufacturing process to prevent defects in subsequent wafers.

6. **Feedback Loop and Continuous Improvement:**
   - **Continuous Monitoring:** Monitor the model's performance in real time and compare predictions with actual outcomes to identify any drifts in model accuracy.
   - **Model Retraining:** Regularly retrain the model with new data to keep it up-to-date with any changes in the production process or sensor behavior, ensuring the model remains accurate over time.
   - **Anomaly Detection:** Implement an additional ML model for anomaly detection that continuously monitors sensor data to detect any unusual patterns that might indicate sensor faults or process anomalies.

### Conclusion
This project involves the development of a comprehensive machine learning system for real-time monitoring and prediction of wafer quality in semiconductor manufacturing. By implementing this system, you can significantly improve production yield, reduce waste, and enhance overall efficiency in the manufacturing process.



## Tech Stack
- Python 3.8+
- MongoDB
- Machine Learning Libraries:
  - scikit-learn
  - pandas
  - numpy
- Web Framework:
  - Flask
- Development Tools:
  - Git
  - pytest (for testing)
  - Docker (for containerization)

## Project Structure
```
sensor_fault_detection/
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   └── train_pipeline.py
│   ├── exception.py
│   └── utils.py
├── tests/
├── config/
├── artifacts/
├── notebooks/
├── app.py
├── requirements.txt
└── README.md
```

![Model Trainer code flow](https://github.com/thatritikpatel/sensor_fault_detection/blob/main/Model%20Trainer%20code%20flow.png)

![Sensor Fault Detection High Level Flow](https://github.com/thatritikpatel/sensor_fault_detection/blob/main/Sensor%20Fault%20Detection%20High%20Level%20Flow.png)

![Training Pipeline code flow](https://github.com/thatritikpatel/sensor_fault_detection/blob/main/Training%20Pipeline%20code%20flow.png)

![data Transformation code flow](https://github.com/thatritikpatel/sensor_fault_detection/blob/main/data%20Transformation%20code%20flow.png)

![data ingestion code flow](https://github.com/thatritikpatel/sensor_fault_detection/blob/main/data%20ingestion%20code%20flow.png)

![prediction pipeline code flow](https://github.com/thatritikpatel/sensor_fault_detection/blob/main/prediction%20pipeline%20code%20flow.png)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/thatritikpatel/sensor_fault_detection.git
cd sensor_fault_detection
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure MongoDB:
- Set up a MongoDB Atlas account or local MongoDB instance
- Update the connection string in your configuration

5. Set up environment variables:
```bash
export MONGO_DB_URL="your-mongodb-connection-string"
# On Windows:
# set MONGO_DB_URL="your-mongodb-connection-string"
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Access the web interface:
- Open your browser and navigate to `http://localhost:5000`
- Use the interface to upload sensor data and view predictions

3. API Endpoints:
- `/train`: Trigger model training
- `/predict`: Get predictions for new sensor data

## Data Pipeline

The project implements a comprehensive data pipeline:

1. Data Ingestion:
   - Collects sensor data from MongoDB
   - Performs initial data validation
   - Creates train/test splits

2. Data Transformation:
   - Handles missing values
   - Performs feature scaling
   - Encodes categorical variables

3. Model Training:
   - Trains the classification model
   - Evaluates model performance
   - Saves the trained model

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make changes and commit (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request


## Contact
- Ritik Patel - [ritik.patel129@gmail.com]
- Project Link: [https://github.com/thatritikpatel/sensor_fault_detection/tree/main]