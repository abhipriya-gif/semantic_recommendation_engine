from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

embedder = SentenceTransformer('all-MiniLM-L6-v2')
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = AutoModelForSequenceClassification.from_pretrained(model_name)

def create_embedding(text):
    embeddings = embedder.encode(text, convert_to_tensor=True)
    return embeddings

def create_vector(all_reviews, review_to_restaurant):
  corpus_embeddings =create_embedding(all_reviews)
  corpus_embeddings_list = corpus_embeddings.tolist()

  vector_data = []
  for i, embedding in enumerate(corpus_embeddings_list):
    # Calculate sentiment score beforehand
    sentiment = get_sentiment_score(str(all_reviews[i]))

    vector_data.append({
        'id': str(i),  # Unique ID for each vector
        'values': embedding,
        'metadata': {'review': str(all_reviews[i]), 'restaurant': review_to_restaurant[all_reviews[i]], 'sentiment': sentiment}  # Optional metadata
    })
    return vector_data

def get_sentiment_score(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = classifier(**inputs)
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    return probabilities[0][1].item()
