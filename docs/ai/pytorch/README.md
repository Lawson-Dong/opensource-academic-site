# PyTorch Tutorial 🚀

This tutorial introduces the basic usage of PyTorch, including tensor operations, automatic differentiation, building neural networks, and training a simple machine learning model.

## What is PyTorch?

PyTorch is an open-source machine learning framework developed by Facebook, widely used for deep learning research and application development. It provides powerful tensor computation and automatic differentiation capabilities, making it easier to build and train deep learning models.

## Environment Setup

### Installing PyTorch

```bash
# Install PyTorch (CPU version) using pip
pip install torch torchvision torchaudio

# Install PyTorch (CUDA 11.8 version) using pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install using uv
uv add torch torchvision torchaudio
```

### Verifying Installation

```python
import torch                                    # Import PyTorch library
print(torch.__version__)                        # Print current PyTorch version
print(torch.cuda.is_available())                # Check if CUDA is available (i.e., if there's an NVIDIA GPU)
```

## Basic Tensor Operations

### Creating Tensors

```python
import torch                                    # Import PyTorch library

# Create a scalar (0-dimensional tensor, single value)
scalar = torch.tensor(5.0)                      # Create a scalar tensor with value 5.0
print(f"Scalar: {scalar}")                      # Output: Scalar: tensor(5.)
print(f"Scalar shape: {scalar.shape}")          # Output: Scalar shape: torch.Size([]), scalars have no dimensions

# Create a vector (1-dimensional tensor)
vector = torch.tensor([1.0, 2.0, 3.0])         # Create a 1D tensor with 3 elements
print(f"Vector: {vector}")                      # Output: Vector: tensor([1., 2., 3.])
print(f"Vector shape: {vector.shape}")          # Output: Vector shape: torch.Size([3]), length 3

# Create a matrix (2-dimensional tensor)
matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]])  # Create a 2x2 2D tensor
print(f"Matrix: {matrix}")                      # Output: Matrix: tensor([[1., 2.], [3., 4.]])
print(f"Matrix shape: {matrix.shape}")          # Output: Matrix shape: torch.Size([2, 2]), 2 rows 2 columns

# Create a 3-dimensional tensor (similar to RGB image, channel×height×width)
tensor_3d = torch.tensor([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]])  # 2×2×2 3D tensor
print(f"3D tensor: {tensor_3d}")                  # Output all elements of the 3D tensor
print(f"3D tensor shape: {tensor_3d.shape}")        # Output: 3D tensor shape: torch.Size([2, 2, 2])

# Create a tensor of zeros (often used for initializing biases or masks)
zeros = torch.zeros((2, 3))                     # Create a 2x3 tensor with all elements 0
print(f"Zeros tensor: {zeros}")                     # Output: tensor([[0., 0., 0.], [0., 0., 0.]])

# Create a tensor of ones (often used for initializing weights or masks)
ones = torch.ones((2, 3))                       # Create a 2x3 tensor with all elements 1
print(f"Ones tensor: {ones}")                       # Output: tensor([[1., 1., 1.], [1., 1., 1.]])

# Create a random tensor (values uniformly distributed between [0, 1), often used for weight initialization)
random_tensor = torch.rand((2, 3))              # Create a 2x3 tensor with random values
print(f"Random tensor: {random_tensor}")              # Output the randomly generated 2×3 tensor
```

### Tensor Operations

```python
import torch                                    # Import PyTorch library

# Create two 1D tensors for demonstration
a = torch.tensor([1.0, 2.0, 3.0])              # Create vector a
b = torch.tensor([4.0, 5.0, 6.0])              # Create vector b

# Element-wise addition: add corresponding elements
c = a + b                                       # Equivalent to torch.add(a, b)
print(f"a + b: {c}")                            # Output: tensor([5., 7., 9.])

# Element-wise subtraction: subtract corresponding elements
d = a - b                                       # Equivalent to torch.sub(a, b)
print(f"a - b: {d}")                            # Output: tensor([-3., -3., -3.])

# Element-wise multiplication (Hadamard product): multiply corresponding elements, not matrix multiplication
e = a * b                                       # Equivalent to torch.mul(a, b)
print(f"a * b: {e}")                            # Output: tensor([ 4., 10., 18.])

# Element-wise division: divide corresponding elements
f = a / b                                       # Equivalent to torch.div(a, b)
print(f"a / b: {f}")                            # Output: tensor([0.2500, 0.4000, 0.5000])

# Matrix multiplication: 2×2 matrix multiplied by 2×1 vector, result is 2×1 vector
g = torch.matmul(torch.tensor([[1, 2], [3, 4]]), torch.tensor([[5], [6]]))
# Calculation process: [[1*5+2*6], [3*5+4*6]] = [[17], [39]]
print(f"Matrix multiplication: {g}")                         # Output: tensor([[17], [39]])

# Broadcasting: automatically expand 1D tensor [10.0, 20.0] to 2×2, then element-wise addition
h = torch.tensor([[1.0, 2.0], [3.0, 4.0]]) + torch.tensor([10.0, 20.0])
# Equivalent to: [[1,2],[3,4]] + [[10,20],[10,20]] = [[11,22],[13,24]]
print(f"Broadcasting operation: {h}")                         # Output: tensor([[11., 22.], [13., 24.]])
```

## Automatic Differentiation

```python
import torch                                    # Import PyTorch library

# Create tensors that require gradient, requires_grad=True tells PyTorch to track all operations on this tensor
x = torch.tensor(3.0, requires_grad=True)       # x = 3.0, marked for gradient calculation
y = torch.tensor(5.0, requires_grad=True)       # y = 5.0, marked for gradient calculation

# Define computation graph: z = 2x + y²
z = 2 * x + y ** 2                             # z = 2*3 + 5² = 6 + 25 = 31
print(f"z = {z}")                               # Output: z = tensor(31., grad_fn=<AddBackward0>)

# Backward pass: automatically calculate partial derivatives of z with respect to x and y
z.backward()                                    # Calculate gradients: dz/dx = 2, dz/dy = 2y = 10

# View the calculated gradients
print(f"Gradient of x: {x.grad}")                     # Output: 2.0, because dz/dx = d(2x+y²)/dx = 2
print(f"Gradient of y: {y.grad}")                     # Output: 10.0, because dz/dy = d(2x+y²)/dy = 2y = 2×5 = 10

# Use torch.no_grad() context manager to disable gradient tracking
# Used during model evaluation to save memory and speed up computation
with torch.no_grad():                           # Enter context where gradients are not tracked
    w = x * y                                   # Calculate w = 3 × 5 = 15, but don't record gradients
    print(f"w = {w}")                           # Output: w = tensor(15.)
    print(f"w.requires_grad = {w.requires_grad}")  # Output: False, w won't track gradients
```

## Building a Simple Neural Network

### Basic Network Structure

```python
import torch                                    # Import PyTorch library
import torch.nn as nn                           # Import neural network module, contains layers, loss functions, etc.

# Define a simple fully connected neural network, inheriting from nn.Module (base class for all PyTorch models)
class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        # Call parent class nn.Module's constructor, must do this
        super(SimpleNet, self).__init__()
        # Define first layer: fully connected layer, maps input from input_size dimensions to hidden_size dimensions
        self.fc1 = nn.Linear(input_size, hidden_size)   # Contains weight matrix W and bias vector b
        # Define activation function: ReLU, introduces non-linearity, f(x) = max(0, x)
        self.relu = nn.ReLU()
        # Define second layer: fully connected layer, maps hidden_size dimensions to output_size dimensions
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    # Define forward pass: process of data passing through the network
    def forward(self, x):
        out = self.fc1(x)                       # Input x passes through first linear transformation: out = Wx + b
        out = self.relu(out)                    # Pass through ReLU activation function, introducing non-linearity
        out = self.fc2(out)                     # Pass through second linear transformation, get final output
        return out                              # Return network output

# Create network instance: input dimension 2, hidden layer dimension 10, output dimension 1
model = SimpleNet(input_size=2, hidden_size=10, output_size=1)
print(model)                                    # Print network structure, showing layer information

# Test network: input a sample, view output
input_tensor = torch.tensor([[1.0, 2.0]])       # Create a 1×2 input tensor (1 sample, 2 features)
output = model(input_tensor)                    # Pass input through network, perform forward pass
print(f"Network output: {output}")                    # Output network prediction (random due to randomly initialized weights)
```

## Training a Simple Linear Regression Model

### Complete Training Code

```python
import torch                                    # Import PyTorch library
import torch.nn as nn                           # Import neural network module
import torch.optim as optim                     # Import optimizer module (SGD, Adam, etc.)
import matplotlib.pyplot as plt                 # Import plotting library for visualizing results
import numpy as np                              # Import NumPy for generating simulated data

# ========== 1. Generate Simulated Data ==========
np.random.seed(42)                              # Set random seed to ensure consistent results
x = np.random.rand(100, 1) * 10                # Generate 100 random numbers between [0, 10) as feature x
y = 2 * x + 1 + np.random.randn(100, 1) * 0.5  # Generate labels y = 2x + 1 + noise, simulating real data

# Convert NumPy arrays to PyTorch tensors (PyTorch models can only handle tensors)
x_tensor = torch.from_numpy(x).float()          # Convert x to float32 tensor
y_tensor = torch.from_numpy(y).float()          # Convert y to float32 tensor

# ========== 2. Define Model ==========
class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        # Define a linear layer: input dimension 1 (x), output dimension 1 (y)
        # Equivalent to y = wx + b, PyTorch automatically initializes w and b
        self.linear = nn.Linear(1, 1)
    
    def forward(self, x):
        return self.linear(x)                   # Forward pass: calculate y = wx + b

model = LinearRegression()                      # Instantiate linear regression model
print(model)                                    # Print model structure, can see initial values of weights and biases

# ========== 3. Define Loss Function and Optimizer ==========
# MSE loss function: mean squared error, calculates average squared difference between predictions and true values
# Formula: Loss = (1/n) × Σ(ŷᵢ - yᵢ)²
criterion = nn.MSELoss()

# Stochastic Gradient Descent optimizer: used to update model parameters (weights and biases)
# model.parameters(): get all trainable parameters in the model
# lr=0.01: learning rate, controls step size of each parameter update
optimizer = optim.SGD(model.parameters(), lr=0.01)

# ========== 4. Train Model ==========
epochs = 1000                                   # Training epochs: entire dataset will be reused 1000 times
losses = []                                     # Used to record loss value each epoch, for later analysis

for epoch in range(epochs):                     # Iterate through each training epoch
    # --- Forward Pass ---
    outputs = model(x_tensor)                   # Pass all data through model, get predictions
    loss = criterion(outputs, y_tensor)         # Calculate MSE loss between predictions and true values
    
    # --- Backward Pass and Parameter Update ---
    optimizer.zero_grad()                       # Clear previous gradients (PyTorch accumulates gradients by default)
    loss.backward()                             # Backward pass: automatically calculate gradients of loss with respect to each parameter
    optimizer.step()                            # Update parameters based on gradients: w = w - lr × gradient
    
    # --- Record and Print ---
    losses.append(loss.item())                  # loss.item() converts single-element tensor to Python scalar
    if (epoch + 1) % 100 == 0:                  # Print training progress every 100 epochs
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

# ========== 5. Evaluate Model ==========
with torch.no_grad():                           # Disable gradient tracking (not needed during evaluation)
    predicted = model(x_tensor).numpy()         # Make predictions with trained model, convert to NumPy array

# Print model learned parameters (ideally should be close to w=2, b=1)
print(f'Model parameters:')
for name, param in model.named_parameters():    # Iterate through all named parameters of the model
    print(f'{name}: {param.data.item()}')       # Print parameter name and value

# ========== 6. Visualize Results ==========
plt.figure(figsize=(10, 6))                     # Create 10×6 inch figure
plt.scatter(x, y, label='Original data')              # Draw scatter plot showing original data points
plt.plot(x, predicted, color='red', label='Predicted line')  # Draw fitted line
plt.xlabel('X')                                 # Set x-axis label
plt.ylabel('Y')                                 # Set y-axis label
plt.title('Linear Regression')                            # Set chart title
plt.legend()                                    # Show legend
plt.show()                                      # Display chart

# ========== 7. Save Model ==========
# Save only model parameters (weights and biases), not model structure
# .pth is standard extension for PyTorch model files
torch.save(model.state_dict(), 'linear_regression_model.pth')
print('Model saved')

# ========== 8. Load Model ==========
loaded_model = LinearRegression()               # First create a model instance with same structure
loaded_model.load_state_dict(torch.load('linear_regression_model.pth'))  # Load saved parameters
print('Model loaded')

# Test loaded model: input x=5.0, prediction y should be close to 2×5+1 = 11
with torch.no_grad():                           # No gradients needed during evaluation
    test_input = torch.tensor([[5.0]])           # Create test input
    test_output = loaded_model(test_input)       # Make prediction with loaded model
    print(f'Input 5.0, predicted output: {test_output.item()}')  # Print prediction result
    print(f'True value should be close to: {2*5 + 1}')          # Print theoretical value: 11
```

## Training a Simple Classification Model

### Complete Training Code

```python
import torch                                    # Import PyTorch library
import torch.nn as nn                           # Import neural network module
import torch.optim as optim                     # Import optimizer module
from sklearn.datasets import make_classification  # Import sklearn's classification data generator
from sklearn.model_selection import train_test_split  # Import dataset splitting tool
from sklearn.preprocessing import StandardScaler     # Import data standardization tool

# ========== 1. Generate Simulated Classification Data ==========
# Generate 1000 samples, each with 20 features, divided into 2 classes
# n_informative=10: 10 features are discriminative, remaining 10 are noise features
X, y = make_classification(
    n_samples=1000, n_features=20, n_classes=2,
    n_informative=10, random_state=42
)

# Data standardization: scale each feature to have mean 0 and standard deviation 1
# This is very important for neural network training, can accelerate convergence
scaler = StandardScaler()
X = scaler.fit_transform(X)                     # Calculate mean and standard deviation, apply standardization

# Split into training set (80%) and test set (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert NumPy arrays to PyTorch tensors
X_train_tensor = torch.from_numpy(X_train).float()  # Training set features, converted to float32
Y_train_tensor = torch.from_numpy(y_train).long()   # Training set labels, converted to long (required by CrossEntropyLoss)
X_test_tensor = torch.from_numpy(X_test).float()    # Test set features
Y_test_tensor = torch.from_numpy(y_test).long()     # Test set labels

# ========== 2. Define Model ==========
class SimpleClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleClassifier, self).__init__()
        # First layer: fully connected layer, maps 20-dimensional input to 32-dimensional hidden layer
        self.fc1 = nn.Linear(input_size, hidden_size)
        # ReLU activation function: introduces non-linearity, helps network learn complex patterns
        self.relu = nn.ReLU()
        # Second layer: fully connected layer, maps 32-dimensional hidden layer to 2-dimensional output (scores for 2 classes)
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        out = self.fc1(x)                       # Linear transformation: 20D → 32D
        out = self.relu(out)                    # ReLU activation: turns negative values to 0
        out = self.fc2(out)                     # Linear transformation: 32D → 2D (output logits)
        return out                              # Return raw scores (logits) for each class

# Create model instance: input 20D, hidden layer 32D, output 2D (2 classes)
model = SimpleClassifier(input_size=20, hidden_size=32, output_size=2)
print(model)                                    # Print model structure

# ========== 3. Define Loss Function and Optimizer ==========
# Cross entropy loss function: suitable for multi-class classification tasks
# Internally automatically applies softmax + log operations, so model output doesn't need softmax
criterion = nn.CrossEntropyLoss()

# Adam optimizer: adaptive learning rate optimizer, converges faster than SGD
# lr=0.001: initial learning rate
optimizer = optim.Adam(model.parameters(), lr=0.001)

# ========== 4. Train Model ==========
epochs = 100                                   # Train for 100 epochs
train_losses = []                               # Record training loss each epoch
test_losses = []                                # Record test loss each epoch

for epoch in range(epochs):                     # Iterate through each training epoch
    # --- Training Phase ---
    model.train()                               # Set to training mode (enables dropout and batch norm, etc.)
    
    outputs = model(X_train_tensor)             # Forward pass: calculate training set predictions
    loss = criterion(outputs, Y_train_tensor)   # Calculate training loss
    
    optimizer.zero_grad()                       # Clear gradients
    loss.backward()                             # Backward pass: calculate gradients
    optimizer.step()                            # Update parameters
    
    train_losses.append(loss.item())            # Record training loss
    
    # --- Validation Phase ---
    model.eval()                                # Set to evaluation mode (disables dropout and batch norm, etc.)
    with torch.no_grad():                       # Disable gradient tracking, save memory
        test_outputs = model(X_test_tensor)     # Calculate test set predictions
        test_loss = criterion(test_outputs, Y_test_tensor)  # Calculate test loss
        test_losses.append(test_loss.item())    # Record test loss
    
    if (epoch + 1) % 10 == 0:                  # Print every 10 epochs
        print(f'Epoch [{epoch+1}/{epochs}], Train Loss: {loss.item():.4f}, Test Loss: {test_loss.item():.4f}')

# ========== 5. Evaluate Model ==========
model.eval()                                    # Set to evaluation mode
with torch.no_grad():                           # Disable gradient tracking
    # Calculate training set accuracy
    train_outputs = model(X_train_tensor)       # Training set predictions
    _, train_preds = torch.max(train_outputs, 1)  # Take index of maximum value in each row as predicted class
    train_accuracy = (train_preds == Y_train_tensor).sum().item() / len(Y_train_tensor)
    
    # Calculate test set accuracy
    test_outputs = model(X_test_tensor)         # Test set predictions
    _, test_preds = torch.max(test_outputs, 1)   # Take index of maximum value in each row as predicted class
    test_accuracy = (test_preds == Y_test_tensor).sum().item() / len(Y_test_tensor)

print(f'Training set accuracy: {train_accuracy:.4f}')     # Print training set accuracy
print(f'Test set accuracy: {test_accuracy:.4f}')      # Print test set accuracy

# ========== 6. Save Model ==========
torch.save(model.state_dict(), 'simple_classifier.pth')  # Save model parameters
print('Model saved')
```

## PyTorch Common Techniques

### 1. Data Loading

```python
from torch.utils.data import Dataset, DataLoader  # Import dataset and data loader

# Custom dataset class, inheriting from Dataset (base class for PyTorch datasets)
class CustomDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.from_numpy(X).float()    # Convert features to float32 tensor
        self.y = torch.from_numpy(y).long()     # Convert labels to long tensor (required for classification tasks)
    
    def __len__(self):
        return len(self.X)                      # Return total number of samples in dataset (must implement)
    
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]         # Return a sample and corresponding label by index (must implement)

# Create dataset instance
train_dataset = CustomDataset(X_train, y_train)

# Create data loader: automatically batches data, shuffles order
# batch_size=32: 32 samples per batch
# shuffle=True: shuffle data order at start of each epoch to prevent model from memorizing data order
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# Use data loader for training
for batch_idx, (data, targets) in enumerate(train_loader):
    # data: current batch of feature data, shape [32, 20]
    # targets: current batch of labels, shape [32]
    # Write training code here...
    pass
```

### 2. Model Evaluation

```python
def evaluate_model(model, data_loader, criterion):
    """Evaluate model accuracy and average loss on given dataset"""
    model.eval()                                # Set to evaluation mode
    total_loss = 0                              # Cumulative loss
    correct = 0                                 # Number of correct predictions
    total = 0                                   # Total number of samples
    
    with torch.no_grad():                       # Disable gradient tracking
        for data, targets in data_loader:       # Iterate through each batch
            outputs = model(data)               # Forward pass, get predictions
            loss = criterion(outputs, targets)  # Calculate loss
            total_loss += loss.item()           # Accumulate loss value
            
            # torch.max(outputs, 1): returns maximum value and its index for each row
            # _: maximum value (not needed), predicted: index of maximum value (i.e., predicted class)
            _, predicted = torch.max(outputs, 1)
            total += targets.size(0)            # Accumulate number of samples in current batch
            correct += (predicted == targets).sum().item()  # Accumulate number of correct predictions
    
    accuracy = correct / total                  # Calculate accuracy
    avg_loss = total_loss / len(data_loader)    # Calculate average loss (averaged by number of batches)
    
    return accuracy, avg_loss                   # Return accuracy and average loss
```

### 3. Using GPU Acceleration

```python
# Check if GPU is available, use GPU if available, otherwise use CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Using device: {device}')                    # Output current device being used

# Move all model parameters to GPU
model.to(device)                                # Model's forward and backward passes will now execute on GPU

# Move data to GPU (need to move to same device before inputting data each time)
X_train_tensor = X_train_tensor.to(device)      # Move training set features to GPU
Y_train_tensor = Y_train_tensor.to(device)      # Move training set labels to GPU
```

## Common Issues and Solutions

### 1. CUDA Out of Memory

```python
# Method 1: Reduce batch size, decrease number of samples GPU needs to process at once
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)  # Reduce from 32 to 16

# Method 2: Use gradient accumulation, simulate larger batch_size
# Principle: Split a large batch into multiple small batches, calculate gradients separately and accumulate, then update parameters once
accumulation_steps = 4                         # Update parameters every 4 small batches
for batch_idx, (data, targets) in enumerate(train_loader):
    outputs = model(data)                       # Forward pass
    loss = criterion(outputs, targets)          # Calculate loss
    loss = loss / accumulation_steps            # Divide loss by accumulation steps to keep gradient mean unchanged
    loss.backward()                             # Backward pass, gradients will accumulate (because zero_grad not called)
    
    if (batch_idx + 1) % accumulation_steps == 0:  # Update parameters after every 4 accumulated steps
        optimizer.step()                        # Update parameters using accumulated gradients
        optimizer.zero_grad()                   # Clear gradients, prepare for next accumulation round
```

### 2. Overfitting

```python
# Method 1: Add Dropout layer, randomly drop some neurons during training
# Effect: Prevents neurons from over-relying on specific features, improves model generalization ability
class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)  # First fully connected layer
        self.relu = nn.ReLU()                   # ReLU activation function
        self.dropout = nn.Dropout(p=0.5)        # Dropout layer: randomly drop 50% of neurons during training
        self.fc2 = nn.Linear(hidden_size, output_size)  # Second fully connected layer
    
    def forward(self, x):
        out = self.fc1(x)                       # Linear transformation
        out = self.relu(out)                    # ReLU activation
        out = self.dropout(out)                  # Dropout (only effective when model.train())
        out = self.fc2(out)                     # Linear transformation
        return out

# Method 2: Use L2 regularization (weight decay)
# Effect: Add L2 norm penalty of parameters to loss function, prevent parameters from becoming too large
# weight_decay=1e-4: weight decay coefficient, larger value means stronger regularization
optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-4)
```

## Further Learning Resources

- [PyTorch Official Documentation](https://pytorch.org/docs/stable/index.html)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Deep Learning with PyTorch: A 60 Minute Blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
- [PyTorch Official Examples](https://github.com/pytorch/examples)
- [Deep Learning Introduction with PyTorch](https://github.com/L1aoXingyu/code-of-learn-deep-learning-with-pytorch)

---

*Through this tutorial, you should have mastered the basic usage of PyTorch and techniques for training simple machine learning models. Continue learning to build more complex deep learning models!* 🎉
