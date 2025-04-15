# 🔭 Starlink-Insight

**Starlink-Insight** is a real-time satellite tracker that overlays Starlink positions with internet performance metrics (latency/speed) in remote regions.

## 🚀 Features

- Fetches and updates TLE data for Starlink
- Plots real-time satellite paths on a map
- Correlates satellite overhead times with internet speed test data
- Optional Flask dashboard for visual insights

## 📦 Tech Stack

- Python
- `skyfield`, `matplotlib`, `requests`, `flask` (optional)
- Starlink TLE data (from Celestrak or Space-Track)

## 📊 Example

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Starlink_Train_2021.gif/800px-Starlink_Train_2021.gif" width="400" />
</p>

## 📁 Run It

```bash
pip install -r requirements.txt
python app/tracker.py
python app/internet_analysis.py
