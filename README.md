# Smart Home Energy Monitoring System

## Overview

The Smart Home Energy Monitoring System is an IoT-inspired project that monitors and visualizes household energy consumption through a user-friendly dashboard. The project helps users track energy usage, analyze consumption trends, and promote efficient energy management.

## Features

* Real-time energy consumption monitoring
* Interactive dashboard built with Streamlit
* Energy usage trend visualization
* Daily and monthly consumption analysis
* User-friendly interface for data monitoring
* Simulated sensor data for demonstration purposes
* Insights to support energy-saving decisions

## Project Structure

```text
Smart-Home-Energy-Monitor/
│
├── dashboard/
│   └── dashboard.py
├── data/
│   └── energy_data.csv
├── outputs/
├── circuit_diagram/
├── main.py
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Matplotlib

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd Smart-Home-Energy-Monitor
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

Run the Streamlit dashboard using:

```bash
streamlit run dashboard/dashboard.py
```

After execution, the dashboard will open in your browser and display energy consumption data, trends, and analytics.

## Expected Output

* Display of energy consumption values
* Interactive graphs and charts
* Energy usage trends over time
* Dashboard-based monitoring interface
* Insights for energy optimization

## Applications

* Smart homes
* Residential energy monitoring
* Energy consumption analysis
* Educational IoT and data visualization projects
* Energy efficiency awareness

## Future Enhancements

* Integration with real IoT energy meters
* Cloud-based data storage
* Mobile application support
* AI-based energy consumption prediction
* Automated energy-saving recommendations

## Author

Thanuja Bantanur

## Acknowledgment

Special thanks to Umesh Yadav Sir for his valuable guidance and support throughout the development of this project.
