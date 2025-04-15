import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    return pd.read_csv('data/latency_data.csv')

def plot_latency():
    df = load_data()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    plt.plot(df['timestamp'], df['latency_ms'], label='Latency (ms)')
    plt.xlabel('Time')
    plt.ylabel('Latency (ms)')
    plt.title('Internet Latency Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    plot_latency()
