# Sensor Fault Detection

This project implements a machine learning solution for detecting faults in sensors used in industrial processes. The system analyzes sensor data to identify potential malfunctions and anomalies, helping prevent equipment failures and optimize maintenance schedules.

## Table of Contents
- [Problem Statement](#problem-statement)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Pipeline](#data-pipeline)
- [Contributing](#contributing)

## Problem Statement
The project aims to build a classification model that can accurately detect faults in sensors based on various readings and measurements. Early detection of sensor faults can help prevent costly equipment failures and reduce downtime in industrial processes.

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

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sensor_fault_detection.git
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