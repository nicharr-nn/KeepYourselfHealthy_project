# Keep Yourself Healthy Project

## Team Members
Software and Knowledge Engineering, Faculty of Engineering

Nicha Ruangrit 6510545411

Phavida Rattanamongkolkul 6510545675

## Description
Sitting for too long at the computer can lead to stress and physical strain, so we should go exercise. 
But before heading out, there are several factors to consider, such as the AQI (Air Quality Index) 
in your area and the temperature, to avoid heat stroke and danger from dust. Our project will help you decide whether 
to exercise indoors or outdoors based on the AQI and temperature in your area.

## Features
- Visualize the average AQI and temperature in this week for each day
### API
- Get the AQI and temperature in the area (minimum, maximum, average, average for each day)
- Get the Heat Stroke Level (Low, Moderate, High)
- Get the AQI Level (Good, Moderate, Unhealthy for Sensitive Groups, Unhealthy, Very Unhealthy, Hazardous)

## Libraries and Tools
- FastAPI
- Python

## Primary Data
- Temperature Sensor from KidBright

## Secondary Data
- AQI from [AQICN](https://aqicn.org/)

## Reference
- [AQI Scale](https://aqicn.org/scale/)
- [Heat Stroke Scale](https://hia.anamai.moph.go.th/web-upload/12xb1c83353535e43f224a05e184d8fd75a/m_magazine/35644/3243/file_download/97d591f4485c568d39dffe07f00e3575.pdf)

## Installation
1. Clone this repository
```bash
git clone https://github.com/nicharr-nn/KeepYourselfHealthy_project.git
```
2. change directory to the project
```bash
cd KeepYourselfHealthy_project
```
3. Initialize the virtual environment

Window:
```bash
python -m venv venv
```

MacOS/Linux:
```bash
python3 -m venv venv
```
4. Activate the virtual environment

Window:
```bash
venv\Scripts\activate
```
MacOS/Linux:
```bash
source venv/bin/activate
```

5. Install the required packages
```bash
pip install -r requirements.txt
```
6. Start the app
```bash
uvicorn app:app --port 8000 --reload
```
### To access the API Documentation
Run the server and go to the following link
```bash
http://127.0.0.1:8000/docs
```

### To see the Data Visualization
Run the server and go to the following link
```bash
http://localhost:63342/KeepYourselfHealthy_project/index.html
```