from pinecone import Pinecone

def connect_to_vector_db():
  pc = Pinecone(api_key="5e6a8457-bac4-4e49-88a0-c7fad19a9f13")
  index_name = "cafe-reviews"
  index = pc.Index(index_name)
  return index

def insert_to_vector_db(vector_data):
  index = connect_to_vector_db()
  index.upsert(vectors=vector_data)
  