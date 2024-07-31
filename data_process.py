
def process_input_data(input_data):
  
  data = {input_data["cafe_name"]:input_data["review"]}
  all_reviews = []
  review_to_restaurant = {}
  for restaurant, reviews in data.items():
      for review in reviews:
          all_reviews.append(review)
          review_to_restaurant[review] = restaurant
  return all_reviews, review_to_restaurant