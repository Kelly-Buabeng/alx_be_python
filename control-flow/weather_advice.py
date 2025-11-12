input_answer = str(input("What's the weather like today? (sunny/rainy/cold): ")).lower()
if input_answer == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif input_answer == "rainy":
    print("Don't forget your umbrella and raincoat.")
elif input_answer == "cold":
    print("Make sure to wear a warm coat and scarf.")
else:
    print("Sorry, I don't have advice for this weather.")
