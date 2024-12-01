# Phishing Detection Framework

![GitHub release](https://img.shields.io/github/v/release/cmacha2/phishing-detection-py)
![GitHub stars](https://img.shields.io/github/stars/cmacha2/phishing-detection-py?style=social)
![License](https://img.shields.io/github/license/cmacha2/phishing-detection-py)

## Overview
The Phishing Detection Framework provides an easy-to-use Python library for detecting phishing attempts in URLs and email messages. It leverages state-of-the-art machine learning models from Hugging Face to ensure high accuracy and reliability.

### Key Features
- **Dual Detection Modes**: Supports both URL and email phishing detection.
- **Pre-trained Models**: Uses advanced models for performance:
  - [`bert-finetuned-phishing`](https://huggingface.co/ealvaradob/bert-finetuned-phishing)
  - [`phishing-email-detection-distilbert_v2.4.1`](https://huggingface.co/cybersectony/phishing-email-detection-distilbert_v2.4.1)
- **Batch Processing**: Handle multiple inputs efficiently.
- **Developer Friendly**: Flexible API for seamless integration and customization.
- **Open-Source**: Built for developers by developers.

---

## 🚀 Get Started

### Installation
Install the library using pip:

```bash
pip install phishing-detection-py
```

For detailed installation steps and dependency management, visit the [Installation Guide](https://cmacha2.github.io/phishing-detection-docs/docs/installation).

### Quick Start Example

```python
from phishing_detection_py import PhishingDetector

detector = PhishingDetector(model_type="url")
result = detector.predict("http://example-phishing-site.com")
print(result)
# Output: [{'input': 'http://example-phishing-site.com', 'label': 'phishing', 'confidence': 0.98}]
```

---

## 📖 Documentation

Comprehensive documentation for setup, API usage, and customization is available:

👉 [Phishing Detection Framework Documentation](https://cmacha2.github.io/phishing-detection-docs/)

Highlights include:
- [API Reference](https://cmacha2.github.io/phishing-detection-docs/docs/api-reference)
- [Installation Guide](https://cmacha2.github.io/phishing-detection-docs/docs/installation)
- [Usage Examples](https://cmacha2.github.io/phishing-detection-docs/docs/usage)

---

## 🤝 Contributing
We welcome contributions to improve the Phishing Detection Framework! Get started by reviewing our [Contributing Guide](https://cmacha2.github.io/phishing-detection-docs/docs/contributing).

### How to Contribute
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## 🛡️ License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.

---

## 🙏 Acknowledgments
- Hugging Face for providing pre-trained models and tools.
- Inspiration from the `cybersectony` and `ealvaradob` models.

---

Let's build a safer internet together! 🌐✨
