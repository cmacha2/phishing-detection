
# API Reference

## `PhishingDetector` Class

### Methods:

#### `__init__(model_type: str = 'url')`
- Initializes the phishing detector with the specified model type.
- **Parameters**:
  - `model_type` (str): The type of model to load (`'url'` or `'email'`).
  
#### `predict(input_data: str) -> List[Dict]`
- Predicts whether the given input data is phishing or not.
- **Parameters**:
  - `input_data` (str): The input URL or email text to classify.
- **Returns**: List of prediction results with labels and scores.

#### `predict_proba(input_data: str) -> Dict`
- Predicts the probabilities of the input data belonging to each class.
- **Parameters**:
  - `input_data` (str): The input URL or email text to classify.
- **Returns**: A dictionary with input, prediction, and probabilities.

---

## `ModelRegistry` Class

### Methods:

#### `get_pipeline(model_type: str) -> Pipeline`
- Returns the pipeline for the specified model type.
- **Parameters**:
  - `model_type` (str): The type of model to use (`'url'` or `'email'`).
- **Returns**: A Hugging Face pipeline object.

---

## `utils` Module

### Functions:

#### `load_config(config_path: str) -> Dict`
- Loads configuration from the specified YAML file.
- **Parameters**:
  - `config_path` (str): Path to the YAML configuration file.
- **Returns**: Dictionary containing configuration data.

#### `log_message(message: str, level: str = 'info')`
- Logs messages with the specified level.
- **Parameters**:
  - `message` (str): The message to log.
  - `level` (str): The log level (`'info'`, `'warning'`, `'error'`).
  