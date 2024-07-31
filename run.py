from flask import Flask, request
from vectorize import create_vector, create_embedding
from data_process import process_input_data
from vector_db import insert_to_vector_db, connect_to_vector_db


app = Flask(__name__)
@app.route("/health", methods=["GET"])
#health check
def health_check():
    return "I am alive!"

@app.route("/corpus_encoding", methods=["POST"])
def corpus_encoding():
  input_data = request.get_json()
  all_reviews, review_to_restaurant = process_input_data(input_data)
  vector = create_vector(all_reviews, review_to_restaurant)
  try:
    insert_to_vector_db(vector)
    return "Success!"
  except Exception as e:
     print(e)
     return str(e)
     
     
@app.route("/top_5", methods=["POST", "GET"])
def get_recommendation():
  input_data = request.get_json()
  prompt = input_data["prompt"]
  user_embedding = create_embedding(prompt).tolist()
  index = connect_to_vector_db()
  query_result = index.query(vector=user_embedding,top_k=5,include_metadata=True,filter={'sentiment': {'$gt': 0.5}})
  recommendations = []

  for match in query_result['matches']:
      recommendations.append(match['metadata']['restaurant'])

  return recommendations
  

if __name__ == '__main__':
    app.run()


