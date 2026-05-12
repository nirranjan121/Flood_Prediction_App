from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load scaler & model
scaler = joblib.load("scaler.pkl")
model = joblib.load("best_flood_model.pkl")

# Clean feature names IN TRAINING ORDER
FEATURES = [
    "latitude",
    "longitude",
    "rainfall_mm",
    "temperature_c",
    "humidity_pct",
    "river_discharge_m3s",
    "water_level_m",
    "elevation_m",
    "land_cover",
    "soil_type",
    "population_density",
    "infrastructure",
    "historical_floods"
]

@app.route("/")
def home():
    return "Flood Risk Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        payload = request.get_json()

        if "instances" not in payload or not payload["instances"]:
            return jsonify({"error": "Missing 'instances' in request body"}), 400

        rows = []
        for inst in payload["instances"]:
            row = []
            for col in FEATURES:
                if col not in inst:
                    return jsonify({"error": f"Missing required feature: {col}"}), 400
                row.append(inst[col])
            rows.append(row)

        df = pd.DataFrame(rows, columns=FEATURES)
        scaled = scaler.transform(df)
        preds = model.predict(scaled).tolist()

        # Try to get probabilities (optional)
        try:
            proba = model.predict_proba(scaled).tolist()
        except Exception:
            proba = None

        return jsonify({
            "predictions": preds,
            "probabilities": proba
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # For local testing; Cloud Run will override host/port
    app.run(host="0.0.0.0", port=8080, debug=True)
