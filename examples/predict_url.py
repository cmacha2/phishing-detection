from phishing_detection_py.detector import PhishingDetector

detector = PhishingDetector("url")
url = "http://example.com"
result = detector.predict_proba(url)
print(result)
