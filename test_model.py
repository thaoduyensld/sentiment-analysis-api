
from transformers import pipeline

# 1. Tải mô hình AI từ Hugging Face
classifier = pipeline(
    "text-classification",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

# 2. Chuẩn bị văn bản đầu vào
text = "I love learning Python!"

# 3. Cho AI phân tích cảm xúc
result = classifier(text)

# 4. Hiển thị kết quả
print("Input:", text)
print("Result:", result)
