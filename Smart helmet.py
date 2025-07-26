# ---------------- SMART HELMET PROJECT SIMULATION ----------------

# Function to check if helmet is worn using human detection sensor
def is_helmet_worn(human_detected):
    return human_detected

# Function to detect alcohol using MQ3 sensor simulation
def detect_alcohol(alcohol_level):
    limit = 200  # hypothetical safe limit in ppm
    return alcohol_level < limit

# Function to check if body temperature is in safe range
def is_temperature_normal(temp):
    return 36.0 <= temp <= 37.5  # Normal temperature range in °C

# Function to get GPS location (simulated)
def get_gps_location():
    return "12.9716° N, 77.5946° E"  # Sample coordinates

# Function to simulate GSM alert system
def send_alert(message):
    print(f"\n🚨 GSM ALERT: {message}")

# Main function to simulate the decision to start the bike
def start_bike(human_detected, alcohol_level, temperature):
    print("\n--- SMART HELMET CHECKS ---")

    if not is_helmet_worn(human_detected):
        send_alert("Helmet not worn. Engine Locked.")
        return "❌ Bike won't start."

    if not detect_alcohol(alcohol_level):
        send_alert("Alcohol detected! Engine Locked.")
        return "❌ Bike won't start."

    if not is_temperature_normal(temperature):
        send_alert("Fever detected! Engine Locked.")
        return "❌ Bike won't start."

    print("✅ All checks passed.")
    return "✅ Bike started successfully."

# ------------------ SIMULATION INPUTS ------------------

# These values simulate sensor data (in real system, get from hardware)
human_detected = True           # True if helmet is worn
alcohol_level = 180            # Simulated value in ppm
temperature = 36.5             # Simulated body temperature in °C

# ------------------ RUN SYSTEM ------------------

print(start_bike(human_detected, alcohol_level, temperature))
print("📍 Helmet Location:", get_gps_location())
