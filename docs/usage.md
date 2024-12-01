
# Usage Guide

## Predicting Phishing URLs

### Example:
```python
from phishing_detection import PhishingDetector

detector = PhishingDetector(model_type="url")
result = detector.predict("http://example-phishing-site.com")
print(result)
```

---

## Predicting Phishing Emails

### Example:
```python
from phishing_detection import PhishingDetector

detector = PhishingDetector(model_type="email")
result = detector.predict("Urgent: Your account is locked. Click here to unlock it.")
print(result)
```

---

## Batch Processing

### Example:
```python
from phishing_detection.batch_processor import BatchProcessor

inputs = ["http://phishing-url.com", "https://safe-url.org"]
batch_processor = BatchProcessor(model_type="url")
results = batch_processor.process(inputs)
print(results)
```

---

## Advanced Usage
### Custom Configurations
```python
from phishing_detection.utils import load_config

config = load_config("path/to/config.yaml")
print(config)
```
