import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import tensorflow
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
model = Sequential()
# model.add(Dense(8, activation="relu", input_dim=x.shape[1]))
model.add(Dense(8, activation="relu", input_dim=23))
model.add(Dense(16, activation="relu"))
model.add(Dropout(0.1))
model.add(Dense(8, activation="relu"))
model.add(Dense(3, activation="softmax"))

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])


def build(df):
    x = df.drop("Level", axis=1)
    y = pd.get_dummies(df["Level"])
    x_scaled = scaler.fit_transform(x)
    history = model.fit(x, y, epochs=40, validation_split=0.3)
    plot(history)


def predict(dp):
    pred = model.predict(dp)
    print(pred)
    return np.argmax(pred)


def plot(history):
    plt.figure(figsize=(8, 5))
    plt.plot(history.history["loss"], color="r", label="Training loss", marker="o")
    plt.plot(history.history["val_loss"], color="b", label="Validation loss", marker="o")
    plt.title("Training VS Validation loss", fontsize=20)
    plt.xlabel("No. of Epochs")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(history.history["accuracy"], color="r", label="Training accuracy", marker="o")
    plt.plot(history.history["val_accuracy"], color="b", label="Validation accuracy", marker="o")
    plt.title("Training VS Validation Accuracy", fontsize=20)
    plt.xlabel("No. of Epochs")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.show()