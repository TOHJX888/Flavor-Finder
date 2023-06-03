import random
import nltk


def get_user_preferences():
    print("Welcome to Flavor Finder!")
    allergies = input("Do you have any allergies? (separated by commas, or 'none' if none): ")
    likes = input("What are your likes? (separated by commas): ")
    dislikes = input("What are your dislikes? (separated by commas): ")
    return allergies, likes, dislikes


def suggest_dish(allergies, likes, dislikes):
    # Tokenize user input using NLP techniques
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    allergies_tokens = tokenizer.tokenize(allergies.lower())
    likes_tokens = tokenizer.tokenize(likes.lower())
    dislikes_tokens = tokenizer.tokenize(dislikes.lower())

    # Filter dishes based on user preferences
    filtered_dishes = []
    for dish in dishes:
        recipe_ingredients = [ingredient.lower() for ingredient in dish["ingredients"]]
        if not any(allergy in recipe_ingredients for allergy in allergies_tokens):
           # if any(like in recipe_ingredients for like in likes_tokens):
                if all(dislike not in recipe_ingredients for dislike in dislikes_tokens):
                    filtered_dishes.append(dish)
                  
    priority_dishes = []
    for dish in filtered_dishes:
        recipe_ingredients = [ingredient.lower() for ingredient in dish["ingredients"]]
        if any(like in recipe_ingredients for like in likes_tokens):
            priority_dishes.append(dish)
        else:
            priority_dishes.append(dish)
    
    if priority_dishes:
        suggested_dish = random.choice(priority_dishes)
        print(f"We suggest trying {suggested_dish['name']}.")
        print("Here are the ingredients you'll need:")
        for ingredient in suggested_dish["ingredients"]:
            print("-", ingredient)
        print("Here are the instructions:")
        print(suggested_dish["instructions"])
    else:
        print("Sorry, we couldn't find a suitable dish based on your preferences.")


# Define the dishes with their ingredients and instructions
dishes = [
    {
        "name": "Pasta Carbonara",
        "ingredients": ["spaghetti", "eggs", "bacon", "Parmesan cheese", "black pepper"],
        "instructions": "1. Cook spaghetti according to package instructions. Drain and set aside.\n2. In a separate bowl, whisk together eggs, grated Parmesan cheese, and black pepper.\n3. In a skillet, cook bacon until crispy. Remove from heat and crumble.\n4. In the same skillet, add cooked spaghetti and bacon. Pour the egg mixture over the pasta and toss until well coated.\n5. The heat from the pasta will cook the eggs, creating a creamy sauce.\n6. Serve hot with additional grated Parmesan cheese and black pepper."
    },
    {
        "name": "Chicken Stir-Fry",
        "ingredients": ["chicken breast", "broccoli", "carrots", "soy sauce", "garlic"],
        "instructions": "1. Cut chicken breast into small pieces.\n2. In a pan, heat oil over medium heat. Add minced garlic and cook for 1 minute.\n3. Add chicken pieces to the pan and cook until they are no longer pink.\n4. Add chopped broccoli and carrots. Stir-fry for a few minutes until the vegetables are tender-crisp.\n5. Pour soy sauce over the chicken and vegetables. Stir well to coat.\n6. Cook for an additional 2-3 minutes, then remove from heat.\n7. Serve hot with steamed rice."
    },
            {
            "name": "Veg Pizza",
            "ingredients": ["pizza dough", "tomato sauce", "mozzarella cheese", "bell peppers", "mushrooms", "red onions", "olives", "oregano"],
            "instructions": "1. Preheat the oven to the recommended temperature for the pizza dough.\n2. Roll out the pizza dough into your desired shape and thickness.\n3. Spread a generous amount of tomato sauce evenly over the dough.\n4. Sprinkle mozzarella cheese over the sauce, covering the entire pizza.\n5. Slice the bell peppers, mushrooms, and red onions into thin slices.\n6. Arrange the sliced vegetables on top of the cheese.\n7. Add sliced olives for additional flavor, if desired.\n8. Sprinkle some dried oregano over the pizza.\n9. Place the pizza in the preheated oven and bake according to the dough instructions or until the cheese is melted and bubbly.\n10. Once cooked, remove from the oven and let it cool slightly before slicing and serving."
        },
        {
            "name": "Vegetable Fried Rice",
            "ingredients": ["cooked rice", "mixed vegetables (carrots, peas, corn, bell peppers)", "onion", "garlic", "soy sauce", "vegetable oil", "eggs", "salt", "pepper"],
            "instructions": "1. Heat vegetable oil in a large pan or wok over medium heat.\n2. Add finely chopped onion and minced garlic to the pan. Sauté until the onion turns translucent.\n3. Push the onion and garlic to one side of the pan and crack eggs into the other side. Scramble the eggs until they are cooked through.\n4. Add the mixed vegetables to the pan and stir-fry for a few minutes until they are slightly tender.\n5. Add cooked rice to the pan and mix it well with the vegetables.\n6. Pour soy sauce over the rice and vegetables. Stir-fry for a few more minutes until everything is well combined.\n7. Season with salt and pepper to taste.\n8. Remove from heat and serve hot."
        },
        {
    "name": "Vegetarian Hakka Noodles",
    "ingredients": ["hakka noodles", "mixed vegetables (carrots, cabbage, bell peppers, onions)", "garlic", "soy sauce", "vegetable oil", "salt", "pepper"],
    "instructions": "1. Boil the Hakka noodles according to the package instructions until they are al dente. Drain and rinse with cold water to prevent sticking.\n2. Heat vegetable oil in a large pan or wok over medium heat.\n3. Add minced garlic to the pan and sauté for a minute until fragrant.\n4. Add thinly sliced onions and stir-fry until they turn translucent.\n5. Add the mixed vegetables (carrots, cabbage, bell peppers) and stir-fry for a few minutes until they are slightly tender.\n6. Add the boiled Hakka noodles to the pan and toss them with the vegetables.\n7. Drizzle soy sauce over the noodles and vegetables. Stir-fry for a few more minutes until everything is well combined.\n8. Season with salt and pepper to taste.\n9. Remove from heat and serve hot."
      },
      {
    "name": "Corn Cheese Balls",
    "ingredients": ["corn kernels", "grated cheese", "bread crumbs", "all-purpose flour", "corn flour", "green chili (optional)", "onion", "garlic powder", "salt", "pepper", "oil (for frying)"],
    "instructions": "1. In a mixing bowl, add corn kernels, grated cheese, finely chopped onion, finely chopped green chili (optional), garlic powder, salt, and pepper. Mix well to combine.\n2. Add bread crumbs to the mixture gradually and mix until you get a firm mixture that can be easily shaped into balls.\n3. Take small portions of the mixture and shape them into round balls.\n4. In a separate bowl, prepare a batter by mixing all-purpose flour, corn flour, salt, and water until smooth and lump-free.\n5. Dip each corn cheese ball into the batter, making sure it is coated evenly.\n6. Roll the coated ball in bread crumbs to give it a crispy outer coating.\n7. Repeat the dipping and rolling process for all the corn cheese balls.\n8. Heat oil in a deep pan or kadai for frying. Once the oil is hot, carefully drop the corn cheese balls into the oil in small batches.\n9. Fry the balls until they turn golden brown and crispy. Remove them from the oil using a slotted spoon and drain excess oil on a paper towel.\n10. Serve the corn cheese balls hot with ketchup or any dipping sauce of your choice."
      },
      {
    "name": "Vegetable Curry",
    "ingredients": ["mixed vegetables (carrots, potatoes, peas, cauliflower, bell peppers)", "onion", "garlic", "ginger", "tomatoes", "coconut milk", "curry powder", "turmeric powder", "cumin powder", "coriander powder", "red chili powder", "garam masala", "salt", "vegetable oil", "fresh cilantro (for garnish)"],
    "instructions": "1. Heat vegetable oil in a large pan or pot over medium heat.\n2. Add finely chopped onion, minced garlic, and grated ginger to the pan. Sauté until the onions become translucent.\n3. Add diced tomatoes to the pan and cook until they soften.\n4. Add curry powder, turmeric powder, cumin powder, coriander powder, red chili powder, and salt to the pan. Stir well to combine the spices with the onion and tomato mixture.\n5. Add the mixed vegetables (carrots, potatoes, peas, cauliflower, bell peppers) to the pan and mix them with the spice mixture.\n6. Pour in coconut milk and stir everything together. Cover the pan and let the curry simmer on low heat until the vegetables are cooked through and tender.\n7. Once the vegetables are cooked, sprinkle garam masala over the curry and give it a final stir.\n8. Remove from heat and garnish with fresh cilantro.\n9. Serve the vegetable curry hot with steamed rice or naan bread."
      },
      {
    "name": "Lentil Soup",
    "ingredients": ["lentils", "onion", "carrots", "celery", "garlic", "vegetable broth", "tomatoes", "cumin", "coriander", "paprika", "bay leaf", "salt", "black pepper", "olive oil", "fresh parsley (for garnish)"],
    "instructions": "1. Rinse the lentils under cold water and set them aside.\n2. Heat olive oil in a large pot over medium heat.\n3. Add finely chopped onion, diced carrots, diced celery, and minced garlic to the pot. Sauté until the vegetables soften.\n4. Add cumin, coriander, and paprika to the pot. Stir well to coat the vegetables with the spices.\n5. Add the lentils to the pot and pour in the vegetable broth.\n6. Add diced tomatoes and bay leaf to the pot. Season with salt and black pepper.\n7. Bring the soup to a boil, then reduce the heat to low and let it simmer for about 30-40 minutes, or until the lentils are tender.\n8. Remove the bay leaf from the soup and adjust the seasoning if needed.\n9. Serve the lentil soup hot, garnished with fresh parsley.\n10. You can also drizzle some olive oil on top before serving for added flavor."
      },
      {
    "name": "Chickpea Salad",
    "ingredients": ["canned chickpeas", "cucumber", "tomatoes", "red onion", "bell pepper", "parsley", "lemon juice", "olive oil", "garlic", "salt", "black pepper"],
    "instructions": "1. Rinse the canned chickpeas under cold water and drain them well.\n2. Chop the cucumber, tomatoes, red onion, and bell pepper into small pieces.\n3. In a large mixing bowl, combine the chickpeas, chopped vegetables, and finely chopped parsley.\n4. In a separate small bowl, whisk together lemon juice, olive oil, minced garlic, salt, and black pepper to make the dressing.\n5. Pour the dressing over the chickpea and vegetable mixture. Toss everything together until well combined.\n6. Let the salad marinate in the refrigerator for at least 30 minutes to allow the flavors to meld together.\n7. Before serving, give the salad a final toss and adjust the seasoning if needed.\n8. Serve the chickpea salad chilled as a refreshing and healthy side dish or light meal."
    },
    {
    "name": "Caprese Salad",
    "ingredients": ["ripe tomatoes", "fresh mozzarella cheese", "fresh basil leaves", "extra virgin olive oil", "balsamic vinegar", "salt", "black pepper"],
    "instructions": "1. Slice the tomatoes and fresh mozzarella cheese into equal-sized rounds.\n2. Arrange the tomato slices on a serving platter or plate.\n3. Place a slice of fresh mozzarella cheese on top of each tomato slice.\n4. Take fresh basil leaves and place them on top of the cheese and tomato slices.\n5. Drizzle extra virgin olive oil over the salad, ensuring each slice is coated.\n6. Drizzle balsamic vinegar over the salad for added flavor.\n7. Season with salt and black pepper to taste.\n8. Let the salad sit for a few minutes to allow the flavors to meld together.\n9. Serve the Caprese salad as a light and refreshing appetizer or side dish."
    },
    {
    "name": "Classic Burger",
    "ingredients": ["ground beef", "hamburger buns", "lettuce leaves", "tomato slices", "onion slices", "pickles", "cheddar cheese slices", "ketchup", "mayonnaise", "mustard", "salt", "black pepper"],
    "instructions": "1. Divide the ground beef into equal-sized portions and shape them into patties.\n2. Season the patties with salt and black pepper on both sides.\n3. Preheat a grill or a skillet over medium-high heat.\n4. Cook the burger patties for about 4-5 minutes on each side or until they reach the desired level of doneness.\n5. While the patties are cooking, prepare the hamburger buns by lightly toasting them.\n6. Once the patties are cooked, remove them from the heat and let them rest for a few minutes.\n7. Assemble the burgers by placing a patty on the bottom half of each toasted bun.\n8. Top the patties with lettuce leaves, tomato slices, onion slices, pickles, and cheddar cheese slices.\n9. Spread ketchup, mayonnaise, and mustard on the top half of the buns.\n10. Place the top bun on the assembled ingredients to complete the burger.\n11. Serve the classic burger with your choice of side dishes and enjoy!"
      },
      {
    "name": "Quesadilla",
    "ingredients": ["flour tortillas", "shredded cheese (such as cheddar or Monterey Jack)", "cooked chicken or vegetables (optional)", "sliced bell peppers", "sliced onions", "sliced jalapenos (optional)", "sour cream (for serving)", "salsa (for serving)", "guacamole (for serving)", "salt", "vegetable oil"],
    "instructions": "1. Heat a skillet or griddle over medium heat.\n2. Place a flour tortilla on the skillet and sprinkle a layer of shredded cheese on half of the tortilla.\n3. If desired, add cooked chicken or vegetables on top of the cheese.\n4. Add sliced bell peppers, onions, and jalapenos (if using) on top.\n5. Sprinkle a bit more cheese on top of the vegetables.\n6. Fold the tortilla in half, covering the filling.\n7. Cook the quesadilla for about 2-3 minutes on each side, or until the cheese is melted and the tortilla is crispy and golden brown.\n8. Remove the quesadilla from the skillet and let it cool slightly.\n9. Repeat the process with the remaining tortillas and filling ingredients.\n10. Slice the quesadillas into wedges and serve them hot.\n11. Serve with sour cream, salsa, and guacamole on the side for dipping.\n12. Enjoy your delicious quesadillas!"
      },
      {
    "name": "Ratatouille",
    "ingredients": ["eggplant", "zucchini", "yellow squash", "bell peppers", "onion", "garlic", "tomatoes", "olive oil", "fresh basil leaves", "dried thyme", "salt", "black pepper"],
    "instructions": "1. Preheat the oven to 375°F (190°C).\n2. Slice the eggplant, zucchini, yellow squash, and bell peppers into thin rounds or chunks.\n3. Thinly slice the onion and mince the garlic.\n4. In a baking dish, arrange the sliced vegetables in alternating patterns, overlapping them slightly.\n5. Drizzle olive oil over the vegetables and season with salt, black pepper, and dried thyme.\n6. Sprinkle minced garlic evenly over the vegetables.\n7. Pour diced tomatoes (with their juice) over the vegetables.\n8. Cover the baking dish with foil and bake in the preheated oven for about 45 minutes.\n9. Remove the foil and continue baking for an additional 15-20 minutes, or until the vegetables are tender and lightly browned.\n10. Remove the ratatouille from the oven and let it cool slightly.\n11. Garnish with fresh basil leaves before serving.\n12. Ratatouille can be served as a side dish or as a main course with crusty bread or rice."
      },
      {
    "name": "Stuffed Bell Peppers",
    "ingredients": ["bell peppers", "ground beef (or ground turkey)", "onion", "garlic", "cooked rice", "tomato sauce", "shredded cheese", "olive oil", "Italian seasoning", "salt", "black pepper"],
    "instructions": "1. Preheat the oven to 375°F (190°C).\n2. Cut the tops off the bell peppers and remove the seeds and membranes from the inside.\n3. Place the bell peppers in a baking dish and set aside.\n4. In a large skillet, heat olive oil over medium heat.\n5. Add diced onion and minced garlic to the skillet and cook until the onion becomes translucent.\n6. Add ground beef (or ground turkey) to the skillet and cook until browned and cooked through.\n7. Drain any excess fat from the skillet.\n8. Stir in cooked rice, tomato sauce, Italian seasoning, salt, and black pepper. Mix well to combine all the ingredients.\n9. Spoon the filling mixture into each bell pepper, packing it tightly.\n10. Top each stuffed bell pepper with shredded cheese.\n11. Cover the baking dish with foil and bake in the preheated oven for about 30-35 minutes.\n12. Remove the foil and continue baking for an additional 10-15 minutes, or until the bell peppers are tender and the cheese is melted and bubbly.\n13. Remove the stuffed bell peppers from the oven and let them cool slightly before serving.\n14. Stuffed bell peppers can be served as a delicious and satisfying main dish."
      },
      {
    "name": "Veggie Stir Fry",
    "ingredients": ["assorted vegetables (such as bell peppers, broccoli, carrots, snap peas, mushrooms)", "tofu (optional)", "garlic", "ginger", "soy sauce", "sesame oil", "vegetable oil", "salt", "black pepper"],
    "instructions": "1. Prepare the vegetables by washing them and cutting them into bite-sized pieces.\n2. If using tofu, drain and press it to remove excess moisture, then cut it into cubes.\n3. In a wok or large skillet, heat vegetable oil over medium-high heat.\n4. Add minced garlic and grated ginger to the hot oil and stir-fry for about 1 minute, until fragrant.\n5. Add the tofu cubes (if using) to the skillet and cook until they are lightly browned.\n6. Add the assorted vegetables to the skillet and stir-fry for about 4-5 minutes, until they are crisp-tender.\n7. Drizzle soy sauce and sesame oil over the vegetables and tofu. Toss everything together to coat evenly.\n8. Season with salt and black pepper to taste.\n9. Continue stir-frying for another minute or two to let the flavors meld together.\n10. Remove from heat and serve the veggie stir fry hot as a delicious and healthy main dish or as a side dish with rice or noodles."
      },
      {
    "name": "Margherita Pizza",
    "ingredients": ["pizza dough", "tomato sauce", "fresh mozzarella cheese", "fresh basil leaves", "olive oil", "salt", "black pepper"],
    "instructions": "1. Preheat the oven to the highest temperature setting (typically around 475°F or 245°C).\n2. Roll out the pizza dough into a round shape on a floured surface.\n3. Place the rolled-out dough onto a baking sheet or pizza stone.\n4. Spread a thin layer of tomato sauce evenly over the dough, leaving a small border around the edges.\n5. Tear or slice the fresh mozzarella cheese into small pieces and distribute them over the tomato sauce.\n6. Arrange fresh basil leaves on top of the cheese.\n7. Drizzle a small amount of olive oil over the pizza.\n8. Sprinkle salt and black pepper to taste.\n9. Place the pizza in the preheated oven and bake for about 10-12 minutes, or until the crust is golden and the cheese is melted and bubbly.\n10. Remove the pizza from the oven and let it cool for a few minutes.\n11. Slice the Margherita pizza into wedges and serve it hot.\n12. Enjoy the classic and flavorful Margherita pizza!"
      },
      {
    "name": "Vegetable Biryani",
    "ingredients": ["basmati rice", "assorted vegetables (such as carrots, peas, potatoes, cauliflower)", "onion", "garlic", "ginger", "yogurt", "tomatoes", "green chili peppers", "biryani masala powder", "turmeric powder", "garam masala powder", "saffron strands", "milk", "cashews", "raisins", "ghee (clarified butter)", "salt"],
    "instructions": "1. Rinse the basmati rice in cold water until the water runs clear. Soak the rice in water for 30 minutes, then drain.\n2. In a large pot, bring water to a boil. Add salt and the soaked rice. Cook the rice until it is about 70% cooked. Drain the rice and set it aside.\n3. In a separate pan, heat ghee over medium heat. Add sliced onion and cook until it turns golden brown.\n4. Add minced garlic and grated ginger to the pan and sauté for about 1 minute.\n5. Add diced vegetables, such as carrots, peas, potatoes, and cauliflower, to the pan. Sauté them for a few minutes until they are slightly cooked.\n6. Add chopped tomatoes, sliced green chili peppers, biryani masala powder, turmeric powder, and garam masala powder. Mix well and cook for a few more minutes.\n7. In a small bowl, soak saffron strands in warm milk and set aside.\n8. In a separate pan, heat ghee and fry cashews and raisins until they turn golden brown. Set them aside.\n9. In the pot used to cook the rice, layer the partially cooked rice and the vegetable mixture. Repeat the layers until all the rice and vegetables are used.\n10. Drizzle the saffron-infused milk over the layers of rice.\n11. Sprinkle the fried cashews and raisins over the top.\n12. Cover the pot with a tight-fitting lid and cook on low heat for about 20-25 minutes, or until the rice is fully cooked and the flavors have melded together.\n13. Remove the lid and gently fluff the biryani with a fork.\n14. Serve the vegetable biryani hot with raita or cucumber salad.\n15. Enjoy the aromatic and flavorful vegetable biryani!"
      },
      {
    "name": "Veggie Lasagna",
    "ingredients": ["lasagna noodles", "assorted vegetables (such as spinach, zucchini, bell peppers, mushrooms)", "onion", "garlic", "tomato sauce", "ricotta cheese", "mozzarella cheese", "Parmesan cheese", "fresh basil leaves", "dried oregano", "salt", "black pepper", "olive oil"],
    "instructions": "1. Preheat the oven to 375°F (190°C).\n2. Cook the lasagna noodles according to the package instructions until al dente. Drain and set aside.\n3. In a large skillet, heat olive oil over medium heat. Add diced onion and minced garlic. Sauté until the onion becomes translucent.\n4. Add the assorted vegetables, such as spinach, zucchini, bell peppers, and mushrooms, to the skillet. Cook until the vegetables are tender.\n5. Pour tomato sauce into the skillet and stir to combine with the vegetables. Season with dried oregano, salt, and black pepper to taste. Simmer for a few minutes.\n6. In a separate bowl, mix ricotta cheese with grated Parmesan cheese. Season with salt and pepper.\n7. In a baking dish, spread a thin layer of the vegetable sauce at the bottom.\n8. Arrange a layer of cooked lasagna noodles on top of the sauce.\n9. Spread a layer of the ricotta cheese mixture over the noodles.\n10. Sprinkle shredded mozzarella cheese and torn basil leaves over the ricotta layer.\n11. Repeat the layers of sauce, noodles, ricotta mixture, mozzarella cheese, and basil leaves until all the ingredients are used, ending with a layer of sauce and a generous amount of mozzarella cheese on top.\n12. Cover the baking dish with foil and bake in the preheated oven for about 25 minutes.\n13. Remove the foil and continue baking for an additional 10-15 minutes, or until the cheese is melted and bubbly and the lasagna is heated through.\n14. Remove the veggie lasagna from the oven and let it cool for a few minutes.\n15. Slice and serve the lasagna hot, garnished with fresh basil leaves.\n16. Enjoy the delicious and hearty veggie lasagna!"
      },
      {
    "name": "Greek Salad",
    "ingredients": ["cucumbers", "tomatoes", "red onion", "Kalamata olives", "feta cheese", "fresh parsley", "extra virgin olive oil", "lemon juice", "dried oregano", "salt", "black pepper"],
    "instructions": "1. Wash and chop cucumbers and tomatoes into bite-sized pieces.\n2. Slice red onion thinly.\n3. In a large bowl, combine the chopped cucumbers, tomatoes, red onion, and Kalamata olives.\n4. Crumble feta cheese over the vegetables.\n5. Chop fresh parsley and add it to the bowl.\n6. In a separate small bowl, whisk together extra virgin olive oil, lemon juice, dried oregano, salt, and black pepper to make the dressing.\n7. Pour the dressing over the salad ingredients.\n8. Toss everything together gently to coat the vegetables and feta cheese with the dressing.\n9. Taste and adjust the seasonings if needed.\n10. Transfer the Greek salad to a serving dish or individual plates.\n11. Serve the Greek salad immediately and enjoy the fresh and vibrant flavors."
      },
      {
    "name": "Roasted Vegetable Medley",
    "ingredients": ["assorted vegetables (such as bell peppers, zucchini, carrots, red onion, cherry tomatoes)", "olive oil", "garlic", "dried herbs (such as thyme, rosemary, oregano)", "salt", "black pepper"],
    "instructions": "1. Preheat the oven to 425°F (220°C).\n2. Wash and chop the assorted vegetables into bite-sized pieces.\n3. In a large bowl, toss the chopped vegetables with olive oil to coat them evenly.\n4. Mince garlic cloves and add them to the bowl.\n5. Sprinkle dried herbs, salt, and black pepper over the vegetables. Toss well to distribute the seasonings.\n6. Spread the seasoned vegetables in a single layer on a baking sheet.\n7. Place the baking sheet in the preheated oven and roast the vegetables for about 25-30 minutes, or until they are tender and slightly caramelized, stirring once or twice during cooking.\n8. Remove the roasted vegetable medley from the oven and let it cool slightly.\n9. Transfer the vegetables to a serving dish and garnish with fresh herbs, if desired.\n10. Serve the roasted vegetable medley as a delicious side dish or add it to salads, pasta, or grain bowls.\n11. Enjoy the flavorful and nutritious roasted vegetable medley!"
      },
    # Add more dishes here
    # ...
    # Up to a total of 50 dishes
]
# Main program
allergies, likes, dislikes = get_user_preferences()
suggest_dish(allergies, likes, dislikes)
