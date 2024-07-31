from pinecone import Pinecone
import os
api_key = os.getenv('pinecone_api_key')

def connect_to_vector_db():
  pc = Pinecone(api_key=api_key)
  index_name = "cafe-reviews"
  index = pc.Index(index_name)
  return index

def insert_to_vector_db(vector_data):
  index = connect_to_vector_db()
  index.upsert(vectors=vector_data)
  