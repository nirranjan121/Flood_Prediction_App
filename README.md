# Flood Risk Prediction System 🌧️🌍

## Overview
AI-powered flood risk prediction system using Flask, XGBoost, Vertex AI, and Cloud Run.

## Features
- Flood prediction using ML
- Interactive Earth visualization
- Real-time API prediction
- Cloud Run deployment
- Vertex AI training
- Browser frontend

## Tech Stack
- Python
- Flask
- XGBoost
- Scikit-learn
- Vertex AI
- Google Cloud Run
- HTML/CSS/JavaScript

## Architecture
Frontend → Cloud Run API → ML Model → Prediction

## Deployment
Hosted on Google Cloud Run + Cloud Storage

## API Example
```bash
curl -X POST https://flood-risk-backend-v2-597320691578.us-central1.run.app/predict \
  -H "Content-Type: application/json" \
  -d '{
        "instances": [
          {
            "latitude": 9.97,
            "longitude": 76.28,
            "rainfall_mm": 120.5,
            "temperature_c": 28.3,
            "humidity_pct": 82,
            "river_discharge_m3s": 350.2,
            "water_level_m": 4.5,
            "elevation_m": 12.7,
            "land_cover": 3,
            "soil_type": 2,
            "population_density": 450,
            "infrastructure": 1,
            "historical_floods": 2
          }
        ]
      }'
