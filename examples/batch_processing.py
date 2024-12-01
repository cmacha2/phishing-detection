from phishing_detection.batch_processor import BatchProcessor

batch_processor = BatchProcessor("url")
urls = [
    "http://example-phishing.com",
    "https://safe-site.org",
    "http://another-phishing-site.xyz"
]
results = batch_processor.process_batch(urls)
print("Batch Processing Results:")
for result in results:
    print(result)
