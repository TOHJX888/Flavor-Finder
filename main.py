import random
import nltk

def get_user_preferences():
    print("Welcome to Flavor Finder!")
    print("This app will recommend food for you based on your preferences!")
    print("-------------------------------------")
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
                if all(dislike not in recipe_ingredients for dislike in dislikes_tokens):
                    filtered_dishes.append(dish)
                  
    priority_dishes = []
    for dish in filtered_dishes:
        recipe_ingredients = [ingredient.lower() for ingredient in dish["ingredients"]]
        if any(like in recipe_ingredients for like in likes_tokens):
            priority_dishes.append(dish)
     #   else:
     #       priority_dishes.append(dish)
    
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
    "name": "Stir-fried Vegetables",
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
    "name": "Vegetable Lasagna",
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
     {
  "name": "Mediterranean Quinoa Salad",
  "ingredients": [
    "1 cup quinoa",
    "2 cups vegetable broth",
    "1 cucumber, diced",
    "1 red bell pepper, diced",
    "1/2 red onion, finely chopped",
    "1/2 cup Kalamata olives, pitted and halved",
    "1/2 cup cherry tomatoes, halved",
    "1/4 cup fresh parsley, chopped",
    "1/4 cup fresh mint, chopped",
    "Juice of 1 lemon",
    "2 tablespoons extra virgin olive oil",
    "Salt and pepper to taste"
  ],
  "instructions": "1. Rinse the quinoa under cold water to remove any bitter coating.\n2. In a medium saucepan, bring the vegetable broth to a boil. Add the rinsed quinoa and reduce the heat to low. Cover and simmer for about 15-20 minutes, or until the quinoa is cooked and the liquid is absorbed. Fluff with a fork and let it cool.\n3. In a large bowl, combine the cooked quinoa, diced cucumber, diced red bell pepper, finely chopped red onion, Kalamata olives, cherry tomatoes, chopped parsley, and chopped mint.\n4. In a small bowl, whisk together the lemon juice, extra virgin olive oil, salt, and pepper.\n5. Pour the dressing over the quinoa salad and toss well to combine.\n6. Adjust the seasoning if needed.\n7. Serve the Mediterranean quinoa salad chilled or at room temperature. Enjoy!"
},
  {
  "name": "Kung Pao Chicken",
  "ingredients": [
    "1 lb boneless, skinless chicken breasts, cut into bite-sized cubes",
    "1/2 cup unsalted peanuts",
    "1 red bell pepper, diced",
    "1 green bell pepper, diced",
    "1/2 cup diced celery",
    "1/2 cup diced carrots",
    "3 cloves garlic, minced",
    "2 tablespoons vegetable oil",
    "2 tablespoons soy sauce",
    "2 tablespoons rice vinegar",
    "1 tablespoon hoisin sauce",
    "1 tablespoon cornstarch",
    "1 tablespoon Szechuan peppercorns (optional)",
    "1 teaspoon sugar",
    "1/2 teaspoon red pepper flakes (adjust to taste)",
    "Salt to taste",
    "Cooked rice, for serving"
  ],
  "instructions": "1. In a small bowl, whisk together soy sauce, rice vinegar, hoisin sauce, cornstarch, sugar, and a pinch of salt. Set aside.\n2. Heat vegetable oil in a wok or large skillet over medium-high heat.\n3. Add the minced garlic and Szechuan peppercorns (if using) to the hot oil. Stir-fry for about 30 seconds until fragrant.\n4. Add the chicken cubes to the wok and stir-fry until they are cooked through and slightly browned.\n5. Add the diced bell peppers, celery, and carrots to the wok. Stir-fry for another 2-3 minutes until the vegetables are crisp-tender.\n6. Pour the prepared sauce over the chicken and vegetables in the wok. Stir well to coat everything evenly.\n7. Add the peanuts and red pepper flakes to the wok and stir-fry for an additional minute.\n8. Taste and adjust the seasoning with salt and red pepper flakes if desired.\n9. Remove from heat and serve the Kung Pao Chicken over cooked rice. You will definitely like it!"
},
  {
  "name": "Mapo Tofu",
  "ingredients": [
    "1 block (14 oz) firm tofu, cut into small cubes",
    "1/2 lb ground pork (optional)",
    "2 tablespoons vegetable oil",
    "2 cloves garlic, minced",
    "1 tablespoon ginger, minced",
    "2 tablespoons doubanjiang (spicy bean paste)",
    "1 tablespoon fermented black beans, rinsed and chopped",
    "1 cup chicken or vegetable broth",
    "2 tablespoons soy sauce",
    "1 teaspoon sugar",
    "1/2 teaspoon Szechuan peppercorns, crushed",
    "2 green onions, chopped",
    "1 tablespoon cornstarch mixed with 2 tablespoons water",
    "Cooked rice, for serving"
  ],
  "instructions": "1. Heat vegetable oil in a large wok or skillet over medium heat.\n2. Add minced garlic and ginger to the hot oil and stir-fry for about 1 minute until fragrant.\n3. If using ground pork, add it to the wok and cook until browned and cooked through.\n4. Add doubanjiang (spicy bean paste) and fermented black beans to the wok. Stir-fry for another minute.\n5. Add tofu cubes to the wok and gently stir to coat them with the sauce.\n6. Pour in chicken or vegetable broth and bring to a simmer. Let it cook for about 5 minutes to allow the flavors to meld.\n7. Stir in soy sauce, sugar, and crushed Szechuan peppercorns.\n8. Add the chopped green onions and let them cook for another minute.\n9. Stir in the cornstarch-water mixture to thicken the sauce. Cook for an additional minute until the sauce has thickened.\n10. Remove from heat and serve the Mapo Tofu over steamed rice. Have a nice meal!"
},
  {
  "name": "Sweet and Sour Pork",
  "ingredients": [
    "1 lb pork tenderloin, cut into bite-sized pieces",
    "1/2 cup pineapple chunks",
    "1/2 cup bell peppers, cut into chunks",
    "1/2 cup onion, cut into chunks",
    "2 tablespoons vegetable oil",
    "3 tablespoons ketchup",
    "2 tablespoons vinegar",
    "2 tablespoons soy sauce",
    "2 tablespoons sugar",
    "1 tablespoon cornstarch mixed with 2 tablespoons water",
    "Salt and pepper to taste",
    "Cooked rice, for serving"
  ],
  "instructions": "1. Heat vegetable oil in a large skillet or wok over medium-high heat.\n2. Season the pork pieces with salt and pepper, then add them to the hot skillet. Cook until browned and cooked through.\n3. Remove the cooked pork from the skillet and set aside.\n4. In the same skillet, add the onion and bell peppers. Stir-fry for a few minutes until they start to soften.\n5. In a small bowl, whisk together ketchup, vinegar, soy sauce, sugar, and cornstarch mixture.\n6. Pour the sauce mixture into the skillet with the vegetables. Stir well to combine.\n7. Add the cooked pork and pineapple chunks to the skillet. Stir gently to coat everything with the sauce.\n8. Simmer for a few minutes until the sauce thickens and coats the pork and vegetables.\n9. Remove from heat and serve hot with cooked rice."
}, 
  {
  "name": "Chicken Tikka Masala",
  "ingredients": [
    "1 lb boneless, skinless chicken breasts, cut into bite-sized pieces",
    "1 cup plain yogurt",
    "2 tablespoons lemon juice",
    "2 tablespoons vegetable oil",
    "1 large onion, finely chopped",
    "2 cloves garlic, minced",
    "1 tablespoon ginger, grated",
    "2 teaspoons ground cumin",
    "2 teaspoons ground coriander",
    "1 teaspoon ground paprika",
    "1 teaspoon ground turmeric",
    "1 teaspoon garam masala",
    "1/2 teaspoon chili powder",
    "1 cup tomato puree",
    "1 cup heavy cream",
    "Salt to taste",
    "Fresh cilantro leaves, for garnish",
    "Cooked basmati rice, for serving"
  ],
  "instructions": "1. In a bowl, combine the yogurt and lemon juice. Add the chicken pieces and marinate for at least 1 hour, or overnight for best results.\n2. Heat the vegetable oil in a large skillet over medium heat. Add the chopped onion and cook until softened and lightly browned.\n3. Add the minced garlic and grated ginger to the skillet. Cook for an additional minute.\n4. In a small bowl, mix together the ground cumin, coriander, paprika, turmeric, garam masala, and chili powder. Add this spice mixture to the skillet and cook for 1-2 minutes, stirring constantly.\n5. Add the marinated chicken pieces to the skillet and cook until they are browned on all sides.\n6. Stir in the tomato puree and cook for a few minutes until the sauce thickens slightly.\n7. Reduce the heat to low and pour in the heavy cream. Simmer for 10-15 minutes, stirring occasionally, until the chicken is cooked through and the sauce has thickened.\n8. Season with salt to taste.\n9. Garnish with fresh cilantro leaves and serve hot with cooked basmati rice."
},
  {
  "name": "Nasi Lemak",
  "ingredients": [
    "2 cups jasmine rice",
    "1 cup coconut milk",
    "1 cup water",
    "2 pandan leaves, tied in a knot",
    "1 teaspoon salt",
    "4 tablespoons vegetable oil",
    "4 shallots, thinly sliced",
    "2 cloves garlic, minced",
    "1 tablespoon dried anchovies",
    "2 tablespoons roasted peanuts",
    "2 hard-boiled eggs, halved",
    "Cucumber slices, for garnish",
    "Sambal sauce, for serving"
  ],
  "instructions": "1. Rinse the jasmine rice until the water runs clear, then drain well.\n2. In a saucepan, combine the rinsed rice, coconut milk, water, pandan leaves, and salt. Bring to a boil over medium heat.\n3. Reduce the heat to low, cover the saucepan, and let the rice simmer for about 15-20 minutes, or until the liquid is absorbed and the rice is cooked.\n4. While the rice is cooking, heat the vegetable oil in a frying pan over medium heat. Add the shallots and garlic, and sauté until golden brown and crispy. Remove and set aside for garnish.\n5. In the same pan, fry the dried anchovies until crispy. Remove and set aside for garnish.\n6. In the same pan, toast the roasted peanuts until fragrant. Remove and set aside for garnish.\n7. Once the rice is cooked, fluff it with a fork and remove the pandan leaves.\n8. Serve the nasi lemak by placing a scoop of rice on a plate. Garnish with the fried shallots, garlic, dried anchovies, roasted peanuts, hard-boiled eggs, and cucumber slices.\n9. Serve with sambal sauce on the side.\n10. Enjoy your delicious Nasi Lemak!"
},
  {
  "name": "Rendang",
  "ingredients": [
    "500g beef, cut into cubes",
    "4 tablespoons rendang paste",
    "1 can coconut milk",
    "2 stalks lemongrass, bruised",
    "4 kaffir lime leaves",
    "2 tablespoons tamarind paste",
    "2 tablespoons palm sugar",
    "Salt, to taste",
    "Water, as needed",
    "Cooking oil"
  ],
  "instructions": "1. Heat some cooking oil in a large pot over medium heat.\n2. Add the rendang paste and stir-fry for a few minutes until fragrant.\n3. Add the beef cubes and stir-fry until they are browned on all sides.\n4. Pour in the coconut milk and add the lemongrass, kaffir lime leaves, tamarind paste, palm sugar, and a pinch of salt.\n5. Stir well to combine all the ingredients.\n6. Reduce the heat to low, cover the pot, and let the rendang simmer for about 2-3 hours, or until the beef is tender and the sauce has thickened. Stir occasionally and add water if needed to prevent the sauce from drying out.\n7. Once the beef is tender and the sauce has thickened to your desired consistency, taste and adjust the seasoning with salt if needed.\n8. Serve the rendang hot with steamed rice.\n9. Enjoy your delicious Rendang!"
},
  {
  "name": "Mee Goreng",
  "ingredients": [
    "200g yellow noodles",
    "2 tablespoons cooking oil",
    "2 cloves garlic, minced",
    "1 small onion, sliced",
    "100g chicken breast, sliced",
    "100g shrimp, peeled and deveined",
    "1 cup bean sprouts",
    "1/2 cup cabbage, shredded",
    "1/4 cup carrots, julienned",
    "2 tablespoons tomato ketchup",
    "1 tablespoon chili sauce",
    "1 tablespoon soy sauce",
    "1 tablespoon oyster sauce",
    "1/2 teaspoon curry powder",
    "Salt and pepper to taste",
    "Fried shallots for garnish",
    "Lime wedges for serving"
  ],
  "instructions": "1. Cook the yellow noodles according to the package instructions, then drain and set aside.\n2. Heat the cooking oil in a large pan or wok over medium heat.\n3. Add the minced garlic and sliced onion, and sauté until fragrant and golden brown.\n4. Add the chicken breast and shrimp, and cook until they are cooked through.\n5. Add the bean sprouts, shredded cabbage, and julienned carrots, and stir-fry for a few minutes until the vegetables are slightly wilted.\n6. In a small bowl, mix together the tomato ketchup, chili sauce, soy sauce, oyster sauce, curry powder, salt, and pepper.\n7. Pour the sauce mixture over the cooked ingredients in the pan and stir well to coat everything.\n8. Add the cooked yellow noodles to the pan and toss them with the sauce and ingredients until well combined.\n9. Continue stir-frying for a few more minutes until the noodles are heated through.\n10. Remove from heat and garnish with fried shallots.\n11. Serve hot with lime wedges on the side."
},
  {
  "name": "Beef Stroganoff",
  "ingredients": [
    "500g beef sirloin, thinly sliced",
    "2 tablespoons butter",
    "1 onion, thinly sliced",
    "2 cloves garlic, minced",
    "250g mushrooms, sliced",
    "1 cup beef broth",
    "2 tablespoons all-purpose flour",
    "1 cup sour cream",
    "1 tablespoon Dijon mustard",
    "Salt and pepper to taste",
    "Fresh parsley for garnish",
    "Egg noodles or rice for serving"
  ],
  "instructions": "1. In a large skillet, melt the butter over medium-high heat.\n2. Add the sliced beef sirloin to the skillet and cook until browned. Remove the beef from the skillet and set aside.\n3. In the same skillet, add the sliced onion and minced garlic. Sauté until the onion is translucent.\n4. Add the sliced mushrooms to the skillet and cook until they release their moisture and become tender.\n5. In a small bowl, whisk together the beef broth and all-purpose flour until smooth.\n6. Pour the broth mixture into the skillet with the onions and mushrooms. Stir well and bring to a simmer.\n7. Return the cooked beef to the skillet and stir to combine with the sauce.\n8. Reduce the heat to low and stir in the sour cream and Dijon mustard. Heat gently until the sauce is warmed through, but do not boil.\n9. Season with salt and pepper to taste.\n10. Serve the Beef Stroganoff over egg noodles or rice.\n11. Garnish with fresh parsley before serving."
},
{
"name": "Broccoli and Corn Stir-Fry",
"ingredients": [
"2 cups broccoli florets", "1 cup corn kernels", "1 red bell pepper, thinly sliced", "1 small onion, thinly sliced", "2 cloves garlic, minced", "2 tablespoons soy sauce", "1 tablespoon oyster sauce", "1 tablespoon sesame oil", "1 tablespoon vegetable oil", "Salt and pepper to taste"
],
"instructions": "1. Heat the vegetable oil in a large skillet or wok over medium-high heat.\n2. Add the minced garlic and sauté for a minute until fragrant.\n3. Add the sliced onion and red bell pepper to the skillet. Stir-fry for 2-3 minutes until the vegetables start to soften.\n4. Add the broccoli florets and corn kernels to the skillet. Stir-fry for another 3-4 minutes until the broccoli is tender-crisp.\n5. In a small bowl, whisk together the soy sauce, oyster sauce, and sesame oil.\n6. Pour the sauce mixture over the vegetables in the skillet. Stir well to coat the vegetables evenly.\n7. Season with salt and pepper to taste.\n8. Continue stir-frying for another 1-2 minutes until the sauce is heated through.\n9. Remove from heat and transfer the stir-fried vegetables to a serving dish.\n10. Serve hot as a side dish or over steamed rice.\n11. Enjoy your delicious Broccoli and Corn Stir-Fry!"
}, 
  {
  "name": "Corn Fritters",
  "ingredients": [
    "1 cup all-purpose flour",
    "1 teaspoon baking powder",
    "1/2 teaspoon salt",
    "1/4 teaspoon black pepper",
    "1/4 teaspoon paprika",
    "1/4 teaspoon garlic powder",
    "1/2 cup milk",
    "1 large egg",
    "2 cups corn kernels",
    "1/4 cup chopped green onions",
    "2 tablespoons chopped fresh parsley",
    "Vegetable oil for frying"
  ],
  "instructions": "1. In a large bowl, whisk together the flour, baking powder, salt, black pepper, paprika, and garlic powder.\n2. In a separate bowl, whisk together the milk and egg.\n3. Pour the milk mixture into the flour mixture and stir until well combined.\n4. Add the corn kernels, chopped green onions, and chopped parsley to the batter. Stir until evenly distributed.\n5. In a large skillet, heat enough vegetable oil to cover the bottom of the pan over medium-high heat.\n6. Once the oil is hot, drop spoonfuls of the corn batter into the skillet, spacing them apart.\n7. Flatten the spoonfuls slightly with the back of a spoon to form fritters.\n8. Cook the fritters for 2-3 minutes per side, or until golden brown and crispy.\n9. Remove the cooked fritters from the skillet and place them on a paper towel-lined plate to drain excess oil.\n10. Repeat steps 6-9 until all the batter is used.\n11. Serve the corn fritters warm as an appetizer or side dish.\n12. Enjoy your delicious homemade Corn Fritters!"
}, 
  {
  "name": "Garlic Roasted Broccoli",
  "ingredients": [
    "2 heads of broccoli, cut into florets",
    "3 tablespoons olive oil",
    "4 cloves garlic, minced",
    "1/2 teaspoon salt",
    "1/4 teaspoon black pepper",
    "1/4 teaspoon red pepper flakes (optional)",
    "1 tablespoon lemon juice",
    "Grated Parmesan cheese for garnish"
  ],
  "instructions": "1. Preheat the oven to 425°F (220°C).\n2. Place the broccoli florets on a baking sheet.\n3. In a small bowl, combine the olive oil, minced garlic, salt, black pepper, and red pepper flakes (if using).\n4. Drizzle the olive oil mixture over the broccoli and toss until the florets are evenly coated.\n5. Spread the broccoli out in a single layer on the baking sheet.\n6. Roast in the preheated oven for 20-25 minutes, or until the edges of the broccoli start to brown and crisp.\n7. Remove the roasted broccoli from the oven and drizzle with lemon juice.\n8. Sprinkle grated Parmesan cheese over the top for added flavor (optional).\n9. Transfer the garlic roasted broccoli to a serving dish.\n10. Serve hot as a side dish or as a healthy snack.\n11. Enjoy your delicious Garlic Roasted Broccoli!"
},

  {
  "name": "Broccoli Cheddar Soup",
  "ingredients": [
    "2 heads of broccoli, cut into florets",
    "1 onion, diced",
    "2 carrots, diced",
    "2 cloves of garlic, minced",
    "4 cups vegetable or chicken broth",
    "1 cup milk",
    "2 cups shredded cheddar cheese",
    "2 tablespoons butter",
    "2 tablespoons all-purpose flour",
    "1/2 teaspoon dried thyme",
    "Salt and pepper to taste"
  ],
  "instructions": "1. In a large pot, melt the butter over medium heat.\n2. Add the diced onion, carrots, and minced garlic to the pot. Sauté for 5-7 minutes, or until the vegetables start to soften.\n3. Sprinkle the flour over the vegetables and stir to coat.\n4. Slowly pour in the vegetable or chicken broth, stirring continuously to avoid lumps.\n5. Add the broccoli florets and dried thyme to the pot. Bring the mixture to a boil, then reduce the heat and simmer for 15-20 minutes, or until the broccoli is tender.\n6. Using an immersion blender or regular blender, puree the soup until smooth. Alternatively, you can leave it slightly chunky if desired.\n7. Return the soup to the pot and stir in the milk.\n8. Gradually add the shredded cheddar cheese, stirring until melted and well combined.\n9. Season with salt and pepper to taste.\n10. Simmer the soup for an additional 5 minutes to allow the flavors to meld together.\n11. Serve hot and garnish with additional shredded cheddar cheese if desired.\n12. Enjoy your comforting and creamy Broccoli Cheddar Soup!"
},
  {
  "name": "Cheesy Baked Ziti",
  "ingredients": [
    "1 pound ziti pasta",
    "2 cups marinara sauce",
    "2 cups shredded mozzarella cheese",
    "1 cup ricotta cheese",
    "1/2 cup grated Parmesan cheese",
    "2 cloves garlic, minced",
    "1 teaspoon dried oregano",
    "1/2 teaspoon dried basil",
    "1/4 teaspoon red pepper flakes (optional)",
    "Salt and pepper to taste",
    "Fresh basil leaves for garnish"
  ],
  "instructions": "1. Preheat the oven to 375°F (190°C). Grease a 9x13-inch baking dish.\n2. Cook the ziti pasta according to package instructions until al dente. Drain and set aside.\n3. In a large mixing bowl, combine the marinara sauce, minced garlic, dried oregano, dried basil, red pepper flakes (if using), salt, and pepper. Stir well.\n4. Add the cooked ziti pasta to the bowl with the sauce and toss to coat the pasta evenly.\n5. Transfer half of the sauced pasta to the prepared baking dish and spread it out evenly.\n6. Dollop spoonfuls of ricotta cheese over the pasta and spread it out slightly with the back of a spoon.\n7. Sprinkle half of the shredded mozzarella cheese and grated Parmesan cheese over the ricotta.\n8. Repeat the layers with the remaining sauced pasta, ricotta cheese, and shredded cheeses.\n9. Cover the baking dish with foil and bake for 20 minutes.\n10. Remove the foil and bake for an additional 10-15 minutes, or until the cheese is melted and bubbly.\n11. Remove from the oven and let it cool for a few minutes.\n12. Garnish with fresh basil leaves before serving.\n13. Serve hot and enjoy the cheesy goodness of Baked Ziti!"
},
  {
  "name": "Macaroni and Cheese",
  "ingredients": [
    "8 ounces elbow macaroni",
    "2 cups shredded cheddar cheese",
    "2 cups milk",
    "2 tablespoons butter",
    "2 tablespoons all-purpose flour",
    "1/2 teaspoon salt",
    "1/4 teaspoon black pepper",
    "1/4 teaspoon paprika (optional)",
    "1/4 cup breadcrumbs (optional)"
  ],
  "instructions": "1. Cook the macaroni according to package instructions until al dente. Drain and set aside.\n2. In a saucepan, melt the butter over medium heat. Add the flour and whisk constantly for about 1 minute to create a roux.\n3. Slowly pour in the milk while whisking continuously to combine with the roux. Continue cooking and whisking until the mixture thickens, about 5 minutes.\n4. Add the salt, black pepper, and paprika (if using), and stir to combine.\n5. Reduce the heat to low and gradually add the shredded cheddar cheese, stirring until it melts and the sauce becomes smooth and creamy.\n6. Add the cooked macaroni to the cheese sauce and stir until well coated.\n7. If desired, transfer the macaroni and cheese mixture to a greased baking dish and sprinkle breadcrumbs on top for a crispy topping.\n8. Preheat the oven to 350°F (175°C) and bake the macaroni and cheese for about 20-25 minutes, or until golden and bubbling.\n9. Remove from the oven and let it cool for a few minutes.\n10. Serve hot as a comforting and cheesy main dish or side.\n11. Enjoy the classic and delicious Macaroni and Cheese!"
},
  {
  "name": "Laksa",
  "ingredients": [
    "200g rice noodles",
    "200g chicken, sliced",
    "200g shrimp, peeled and deveined",
    "2 tablespoons laksa paste",
    "400ml coconut milk",
    "500ml chicken broth",
    "2 tablespoons fish sauce",
    "1 tablespoon sugar",
    "1 tablespoon vegetable oil",
    "Bean sprouts, for garnish",
    "Hard-boiled eggs, halved",
    "Fresh cilantro leaves, for garnish",
    "Lime wedges, for serving"
  ],
  "instructions": "1. Prepare the rice noodles according to the package instructions. Drain and set aside.\n2. Heat the vegetable oil in a large pot or wok over medium heat.\n3. Add the laksa paste and cook for a minute until fragrant.\n4. Add the chicken slices and cook until they are no longer pink.\n5. Add the shrimp and cook until they turn pink and are cooked through.\n6. Pour in the coconut milk and chicken broth, and bring the mixture to a gentle simmer.\n7. Stir in the fish sauce and sugar, and let the soup simmer for about 10 minutes to allow the flavors to meld together.\n8. Divide the cooked rice noodles among serving bowls.\n9. Ladle the hot laksa soup over the noodles, ensuring each bowl has a generous amount of chicken, shrimp, and broth.\n10. Garnish with bean sprouts, hard-boiled eggs, and fresh cilantro leaves.\n11. Serve hot with lime wedges on the side.\n12. Enjoy the aromatic and spicy flavors of Laksa!"
},
  {
  "name": "Chicken Rice",
  "ingredients": [
    "1 whole chicken",
    "2 cups jasmine rice",
    "4 cups chicken broth",
    "4 cloves garlic, minced",
    "1 thumb-sized ginger, sliced",
    "2 tablespoons vegetable oil",
    "1 tablespoon sesame oil",
    "2 tablespoons soy sauce",
    "1 cucumber, sliced",
    "Fresh cilantro leaves, for garnish",
    "Sliced chili, for garnish",
    "Lime wedges, for serving"
  ],
  "instructions": "1. In a large pot, bring water to a boil. Add the whole chicken and cook for about 30-40 minutes until fully cooked. Remove the chicken from the pot and set it aside to cool. Reserve the chicken broth for cooking the rice.\n2. Rinse the jasmine rice under cold water until the water runs clear.\n3. In a separate pot, heat vegetable oil and sesame oil over medium heat. Add minced garlic and sliced ginger. Sauté until fragrant.\n4. Add the rinsed jasmine rice to the pot and stir well to coat the grains with oil. Cook for a couple of minutes.\n5. Pour 4 cups of chicken broth into the pot with rice. Bring to a boil, then reduce the heat to low, cover, and let it simmer for about 15-20 minutes or until the rice is cooked and fluffy.\n6. While the rice is cooking, carve the chicken into serving pieces.\n7. In a small bowl, mix soy sauce and a tablespoon of chicken broth.\n8. Serve the chicken rice by placing a scoop of rice on a plate, top it with a few chicken pieces, and drizzle with the soy sauce mixture.\n9. Garnish with cucumber slices, fresh cilantro leaves, and sliced chili.\n10. Serve hot with lime wedges on the side.\n11. Enjoy the fragrant and flavorful Chicken Rice!"
},
  {
  "name": "Hokkien Mee",
  "ingredients": [
    "200g yellow noodles",
    "200g thick rice noodles (bee hoon)",
    "200g prawns, peeled and deveined",
    "200g pork belly, sliced",
    "100g squid, sliced",
    "4 cloves garlic, minced",
    "2 eggs, beaten",
    "4 cups chicken broth",
    "1 cup bean sprouts",
    "2 tablespoons soy sauce",
    "1 tablespoon oyster sauce",
    "1 tablespoon dark soy sauce",
    "1 tablespoon cooking oil",
    "Salt and pepper to taste",
    "Lime wedges, for serving"
  ],
  "instructions": "1. Heat cooking oil in a large wok or frying pan over medium heat.\n2. Add minced garlic and sauté until fragrant.\n3. Add pork belly slices to the pan and cook until browned and slightly crispy.\n4. Add prawns and squid to the pan and stir-fry until cooked through.\n5. Push the ingredients to one side of the pan and pour the beaten eggs into the empty space. Scramble the eggs until cooked.\n6. Add yellow noodles and rice noodles to the pan. Stir-fry everything together for a few minutes.\n7. Add soy sauce, oyster sauce, and dark soy sauce to the noodles. Stir well to coat the noodles evenly.\n8. Pour in the chicken broth and bring it to a simmer. Cook for a few minutes until the noodles absorb the flavors.\n9. Add bean sprouts to the pan and stir-fry for another minute.\n10. Season with salt and pepper to taste.\n11. Serve the Hokkien Mee hot, garnished with lime wedges.\n12. Squeeze lime juice over the noodles before eating.\n13. Enjoy the rich and savory Hokkien Mee!"
},
  {
  "name": "Fish Ball Noodles",
  "ingredients": [
    "200g fish balls",
    "200g noodles of your choice",
    "4 cups chicken or vegetable broth",
    "2 cloves garlic, minced",
    "2 tablespoons soy sauce",
    "1 tablespoon oyster sauce",
    "1 tablespoon sesame oil",
    "1 tablespoon cooking oil",
    "Bok choy or other leafy greens, for serving",
    "Green onions, chopped, for garnish",
    "Fried shallots, for garnish",
    "Chili sauce or sambal, for serving (optional)"
  ],
  "instructions": "1. Bring a pot of water to a boil and cook the noodles according to package instructions. Drain and set aside.\n2. Heat cooking oil in a large pot or saucepan over medium heat.\n3. Add minced garlic to the pot and sauté until fragrant.\n4. Pour in the chicken or vegetable broth and bring it to a simmer.\n5. Add soy sauce, oyster sauce, and sesame oil to the broth. Stir well to combine.\n6. Add fish balls to the broth and cook for a few minutes until heated through.\n7. Meanwhile, blanch bok choy or other leafy greens in boiling water for a minute or two until wilted. Drain and set aside.\n8. To serve, divide the cooked noodles into bowls.\n9. Ladle the fish ball broth over the noodles, making sure to include fish balls in each bowl.\n10. Add blanched bok choy on top of the noodles.\n11. Garnish with chopped green onions and fried shallots.\n12. Serve the Fish Ball Noodles hot, with chili sauce or sambal on the side for extra heat, if desired.\n13. Enjoy the comforting and tasty Fish Ball Noodles!"
},
  {
  "name": "Spicy Szechuan Chicken",
  "ingredients": [
    "500g boneless chicken, cut into bite-sized pieces",
    "2 tablespoons vegetable oil",
    "3 cloves garlic, minced",
    "1 tablespoon ginger, minced",
    "2 tablespoons Szechuan peppercorns, crushed",
    "2 tablespoons chili bean paste",
    "1 tablespoon soy sauce",
    "1 tablespoon rice vinegar",
    "1 tablespoon sugar",
    "1/2 cup chicken broth",
    "1/2 cup water",
    "1 tablespoon cornstarch, mixed with 2 tablespoons water",
    "2 green onions, sliced",
    "1 tablespoon sesame oil",
    "Steamed rice, for serving"
  ],
  "instructions": "1. Heat the vegetable oil in a wok or large skillet over high heat.\n2. Add the minced garlic, ginger, and crushed Szechuan peppercorns. Stir-fry for about 30 seconds until fragrant.\n3. Add the chicken to the wok and stir-fry until it is browned and cooked through.\n4. Push the chicken to the sides of the wok and add the chili bean paste to the center. Stir-fry the paste for a minute to release its flavors.\n5. Add the soy sauce, rice vinegar, sugar, chicken broth, and water to the wok. Stir well to combine all the ingredients.\n6. Bring the sauce to a simmer and let it cook for a few minutes until it thickens slightly.\n7. Stir in the cornstarch-water mixture to further thicken the sauce.\n8. Add the sliced green onions and sesame oil to the wok. Stir well to incorporate them into the dish.\n9. Remove from heat and transfer the Spicy Szechuan Chicken to a serving dish.\n10. Serve hot with steamed rice.\n11. Enjoy the flavorful and spicy Spicy Szechuan Chicken!"
},
  {
  "name": "Tom Yum Soup",
  "ingredients": [
    "4 cups vegetable or chicken broth",
    "2 stalks lemongrass, bruised and cut into 2-inch pieces",
    "3 kaffir lime leaves, torn into pieces",
    "3-4 slices galangal or ginger",
    "2 cloves garlic, minced",
    "2 Thai bird's eye chilies, sliced (adjust to taste)",
    "1 cup mushrooms, sliced",
    "1 tomato, cut into wedges",
    "1 small onion, sliced",
    "1/2 cup cooked shrimp or chicken (optional)",
    "2 tablespoons fish sauce",
    "1 tablespoon lime juice",
    "1 teaspoon sugar",
    "Fresh cilantro leaves for garnish"
  ],
  "instructions": "1. In a large pot, bring the vegetable or chicken broth to a boil.\n2. Add the lemongrass, kaffir lime leaves, galangal or ginger, minced garlic, and sliced Thai bird's eye chilies to the pot. Simmer for about 5 minutes to infuse the flavors into the broth.\n3. Add the mushrooms, tomato wedges, and sliced onion to the pot. Continue simmering for another 5 minutes until the vegetables are tender.\n4. If using, add the cooked shrimp or chicken to the soup and cook for an additional 2 minutes to heat through.\n5. Stir in the fish sauce, lime juice, and sugar. Taste and adjust the seasoning according to your preference.\n6. Remove the lemongrass stalks, kaffir lime leaves, and galangal or ginger slices from the soup.\n7. Ladle the Tom Yum Soup into bowls and garnish with fresh cilantro leaves.\n8. Serve hot and enjoy the aromatic and spicy flavors of this traditional Thai soup."
},
  {
  "name": "Green Curry Soup",
  "ingredients": [
    "2 tablespoons green curry paste",
    "1 can (14 oz) coconut milk",
    "2 cups vegetable or chicken broth",
    "1 tablespoon vegetable oil",
    "1 onion, thinly sliced",
    "2 cloves garlic, minced",
    "1 tablespoon grated fresh ginger",
    "1 bell pepper, thinly sliced",
    "1 cup sliced mushrooms",
    "1 cup diced tofu or cooked chicken",
    "1 cup broccoli florets",
    "1 tablespoon soy sauce",
    "1 tablespoon fish sauce (optional)",
    "1 tablespoon lime juice",
    "1 tablespoon brown sugar",
    "Fresh cilantro leaves for garnish"
  ],
  "instructions": "1. Heat the vegetable oil in a large pot over medium heat.\n2. Add the green curry paste and cook for a minute until fragrant.\n3. Stir in the minced garlic, grated ginger, and sliced onion. Cook for another 2 minutes until the onion softens.\n4. Pour in the coconut milk and vegetable or chicken broth. Bring to a simmer.\n5. Add the bell pepper, mushrooms, tofu or cooked chicken, and broccoli florets to the pot. Simmer for about 10 minutes until the vegetables are tender.\n6. Stir in the soy sauce, fish sauce (if using), lime juice, and brown sugar. Adjust the seasoning according to your taste.\n7. Remove the pot from heat and ladle the Green Curry Soup into bowls.\n8. Garnish with fresh cilantro leaves.\n9. Serve hot and enjoy the aromatic and spicy flavors of this Thai-inspired soup."
},
  {
  "name": "Tomato Basil Pasta",
  "ingredients": [
    "8 ounces spaghetti or your preferred pasta",
    "2 tablespoons olive oil",
    "3 cloves garlic, minced",
    "1 can (14 oz) diced tomatoes",
    "1/4 teaspoon red pepper flakes (optional)",
    "1/2 teaspoon dried oregano",
    "1/2 teaspoon dried basil",
    "Salt and pepper to taste",
    "1/4 cup fresh basil leaves, torn",
    "Grated Parmesan cheese for garnish"
  ],
  "instructions": "1. Cook the pasta according to the package instructions until al dente. Drain and set aside.\n2. In a large skillet, heat the olive oil over medium heat.\n3. Add the minced garlic and sauté for about 1 minute until fragrant.\n4. Add the diced tomatoes, red pepper flakes (if using), dried oregano, and dried basil to the skillet. Stir well to combine.\n5. Season with salt and pepper to taste. Simmer the tomato mixture for about 10 minutes, stirring occasionally.\n6. Add the cooked pasta to the skillet and toss to coat it evenly with the tomato sauce.\n7. Stir in the torn fresh basil leaves.\n8. Remove from heat and transfer the Tomato Basil Pasta to serving plates.\n9. Garnish with grated Parmesan cheese.\n10. Serve hot and enjoy the flavorful combination of tomatoes, basil, and pasta."
},
  {
  "name": "Rogan Josh",
  "ingredients": [
    "500g mutton, cut into pieces",
    "2 onions, finely chopped",
    "4 cloves garlic, minced",
    "1-inch ginger, grated",
    "2 tomatoes, pureed",
    "2 tablespoons vegetable oil",
    "1 tablespoon ghee",
    "2 teaspoons red chili powder",
    "1 teaspoon turmeric powder",
    "1 teaspoon ground cumin",
    "1 teaspoon ground coriander",
    "1 teaspoon garam masala",
    "1 cup plain yogurt",
    "Salt to taste",
    "Fresh cilantro for garnish"
  ],
  "instructions": "1. Heat the vegetable oil and ghee in a large pot or pressure cooker over medium heat.\n2. Add the chopped onions and sauté until golden brown.\n3. Add the minced garlic and grated ginger. Sauté for another minute.\n4. Add the mutton pieces to the pot and cook until browned on all sides.\n5. Stir in the tomato puree and cook for a few minutes until the raw smell disappears.\n6. Add the red chili powder, turmeric powder, ground cumin, ground coriander, and garam masala. Mix well to coat the mutton.\n7. Reduce the heat to low and add the plain yogurt. Stir well to combine.\n8. Cover the pot and simmer for about 1-2 hours, or until the mutton is tender and cooked through. If using a pressure cooker, cook for about 20-25 minutes.\n9. Season with salt to taste.\n10. Garnish with fresh cilantro before serving.\n11. Serve hot with rice or naan bread.\n12. Enjoy the rich and flavorful Rogan Josh!"
},
  {
  "name": "Pork Adobo",
  "ingredients": [
    "1 kg pork belly or shoulder, cut into cubes",
    "1/2 cup soy sauce",
    "1/2 cup vinegar (preferably white cane vinegar)",
    "4 cloves garlic, minced",
    "1 onion, chopped",
    "1 bay leaf",
    "1 teaspoon whole peppercorns",
    "1/2 cup water",
    "2 tablespoons cooking oil",
    "Salt and pepper to taste",
    "Chopped green onions for garnish"
  ],
  "instructions": "1. In a large bowl, combine the pork cubes, soy sauce, vinegar, minced garlic, chopped onion, bay leaf, and whole peppercorns. Mix well to coat the pork in the marinade. Let it marinate for at least 30 minutes or up to overnight in the refrigerator.\n2. Heat the cooking oil in a large skillet or pot over medium heat.\n3. Remove the pork from the marinade, reserving the marinade for later use. Add the pork to the hot skillet and cook until browned on all sides.\n4. Pour in the reserved marinade and add the water. Bring to a boil, then reduce the heat to low.\n5. Cover the skillet and let the pork simmer for about 1 to 1 1/2 hours, or until the pork is tender and the flavors have melded together. Stir occasionally to prevent sticking.\n6. Once the pork is tender, remove the lid and continue cooking uncovered for about 10-15 minutes to reduce the sauce and thicken it slightly.\n7. Season with salt and pepper to taste.\n8. Transfer the Pork Adobo to a serving dish and garnish with chopped green onions.\n9. Serve hot with steamed rice.\n10. Enjoy the delicious and tangy Pork Adobo!"
},




























  



    # Add more dishes here
    # ...
    # Up to a total of 50 dishes
]
# Main program
allergies, likes, dislikes = get_user_preferences()
suggest_dish(allergies, likes, dislikes)
