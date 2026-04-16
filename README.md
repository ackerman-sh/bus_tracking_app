# Bus Tracking and Transit Assistant

Bus Tracking and Transit Assistant is a Flask-based bus navigation prototype that combines session-based access, live bus location sharing, route planning, nearby bus stop discovery, and nearby place search in a single dashboard. Flask mainly handles routing, session state, and live location updates, while most of the application behavior is implemented in the frontend using JavaScript, Leaflet maps, browser geolocation, OSRM routing, and Overpass API queries.

> This project is an early interactive transit prototype focused on map-based travel assistance and live bus tracking.

---

## Preview

The app follows this flow:

1. Log in with basic user and location details
2. Open the dashboard
3. Select a source and destination using live location or map clicks
4. Generate a route with estimated distance and travel time
5. Find nearby bus stops within a selected radius
6. Track a live-updating bus location
7. Search for nearby places such as hotels, hospitals, restaurants, banks, and more

---

## Features

* Flask-based routing and session handling
* Frontend-heavy dashboard built with HTML, CSS, and JavaScript
* Interactive maps powered by Leaflet
* Source and destination selection using live GPS or map click
* Route generation using OSRM
* Live bus location sharing and tracking using Flask-SocketIO
* Nearby bus stop search using Overpass API
* Nearby place discovery using OpenStreetMap data
* Responsive dashboard layout for desktop and mobile use

---

## How It Works

### 1. Login and session flow

The user enters personal and location details through the login page. Flask stores the session and redirects the user to the dashboard.

### 2. Route planning

The dashboard allows the user to choose a source and destination using live location or manual map selection. The app then requests route data from OSRM and displays:

* distance
* estimated travel time
* route line on the map

### 3. Nearby places search

The app uses browser geolocation and Overpass API queries to search for nearby locations such as:

* hotels
* hospitals
* restaurants
* supermarkets
* fuel stations
* libraries
* universities
* airports

### 4. Nearby bus stops

Users can search for bus stops within a selected distance. Matching bus stops are displayed on the map and listed for generated arrival and departure timing display.

### 5. Live bus tracking

The location-sharing page continuously sends GPS updates to the backend. The dashboard fetches the latest location and displays the live bus position on the tracking map.

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/ackerman-sh/FINISHED_NAVIGATION_SYSTEM.git
cd FINISHED_NAVIGATION_SYSTEM
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python app.py
```

Then open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Project Structure

```text
FINISHED_NAVIGATION_SYSTEM/
├── app.py
├── requirements.txt
├── templates/
│   ├── dashboard.html
│   ├── login.html
│   └── ShareLocation.html
├── README.md
└── .gitignore
```

---

## Author

**ackerman-sh**
GitHub: `https://github.com/ackerman-sh`
