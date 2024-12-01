from phishing_detection.detector import PhishingDetector

detector = PhishingDetector("url")
url = "http://example.com"
result = detector.predict_proba(url)
print(result)
