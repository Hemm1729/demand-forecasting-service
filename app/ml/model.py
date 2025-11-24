import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler

def build_gru_model(input_shape: tuple) -> Sequential:
    """Build GRU-based time series model"""
    model = Sequential([
        GRU(units=64, activation='relu', input_shape=input_shape, return_sequences=True),
        Dropout(0.2),
        GRU(units=32, activation='relu', return_sequences=False),
        Dropout(0.2),
        Dense(units=16, activation='relu'),
        Dense(units=1)
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

def prepare_sequences(data: np.ndarray, window_size: int):
    """Prepare sequences for training"""
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i+window_size])
        y.append(data[i+window_size])
    return np.array(X), np.array(y)

def scale_data(data: np.ndarray):
    """Scale data to [0, 1] range"""
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(data.reshape(-1, 1))
    return scaled, scaler

def inverse_scale(scaled_data: np.ndarray, scaler):
    """Inverse scale predictions back to original range"""
    return scaler.inverse_transform(scaled_data.reshape(-1, 1)).flatten()
