from phishing_detection.detector import PhishingDetector

detector = PhishingDetector("email")
email = "Urgent: Your account is locked. Click here to unlock it."
result = detector.predict_proba(email)
print(result)
