# Image_Q: A Probabilistic Neural Network Inspired by Quantum Mechanics

## Project Overview

**Image_Q** is a Python-based project that implements a probabilistic neural network for image classification, inspired by concepts in quantum mechanics such as probabilities and superposition. The goal is to explore how stochastic layers can introduce randomness, akin to quantum phenomena, into the neural network's behavior.

The project uses the MNIST dataset of handwritten digits for training and evaluation.

---

## Features

- Load and preprocess the MNIST dataset.
- Implement a probabilistic neural network with stochastic layers.
- Train the model on handwritten digit images.
- Visualize training results and model predictions.
- Save trained models for later use.

---

## Directory Structure

image_q/ ├── venv/ # Virtual environment ├── q_img.py # Main Python script ├── data/ # Dataset storage ├── models/ # Folder for trained models ├── plots/ # Visualizations and result plots └── README.md # Project documentation

yaml
Copy code

---

## Prerequisites

- Python 3.x
- Virtual environment tools (e.g., `venv`)
- Installed libraries:
  - TensorFlow
  - NumPy
  - Matplotlib

---

## Quick Start

1. **Set up the environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install tensorflow numpy matplotlib
Run the project:

bash
Copy code
python q_img.py
Explore results:

Check the plots/ directory for visualizations.
View saved models in the models/ directory.
Future Improvements
Implement dropout layers for better generalization.
Explore alternative datasets.
Compare the performance of the probabilistic neural network with a standard neural network.