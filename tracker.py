from skyfield.api import load, EarthSatellite
import matplotlib.pyplot as plt
import requests

def get_tle():
    url = "https://celestrak.org/NORAD/elements/starlink.txt"
    r = requests.get(url)
    with open('data/tle.txt', 'w') as f:
        f.write(r.text)
    return r.text

def plot_positions():
    ts = load.timescale()
    tle_lines = get_tle().split('\n')
    satellites = []
    for i in range(0, len(tle_lines) - 2, 3):
        name = tle_lines[i].strip()
        sat = EarthSatellite(tle_lines[i+1], tle_lines[i+2], name, ts)
        satellites.append(sat)

    fig, ax = plt.subplots()
    for sat in satellites[:10]:  # Plot only a few for clarity
        geocentric = sat.at(ts.now())
        subpoint = geocentric.subpoint()
        ax.plot(subpoint.longitude.degrees, subpoint.latitude.degrees, 'bo', markersize=2)

    ax.set_title("Starlink Positions (Sample)")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_positions()
