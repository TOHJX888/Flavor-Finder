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
        if all(like in recipe_ingredients for like in likes_tokens):
            priority_dishes.append(dish)
        else:
            if any(like in recipe_ingredients for like in likes_tokens):
                priority_dishes.append(dish)
            else:
                if not any(like in recipe_ingredients for like in likes_tokens):
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
  {
  "name": "Corn Chowder",
  "ingredients": [
    "4 cups corn kernels (fresh or frozen)",
    "4 slices bacon, chopped",
    "1 onion, diced",
    "2 cloves garlic, minced",
    "2 potatoes, peeled and diced",
    "4 cups chicken or vegetable broth",
    "1 cup milk or cream",
    "2 tablespoons all-purpose flour",
    "1/2 teaspoon dried thyme",
    "Salt and pepper to taste",
    "Chopped fresh parsley for garnish"
  ],
  "instructions": "1. In a large pot or Dutch oven, cook the chopped bacon over medium heat until crispy. Remove the bacon with a slotted spoon and set aside for later use. Leave about 1 tablespoon of bacon drippings in the pot.\n2. In the same pot, add the diced onion and minced garlic. Sauté until the onion is translucent and fragrant.\n3. Add the diced potatoes and corn kernels to the pot. Stir well to combine with the onion and garlic.\n4. In a small bowl, whisk together the flour and a little bit of milk to create a slurry. This will help thicken the chowder.\n5. Pour the slurry into the pot with the corn and potatoes. Stir to coat the vegetables evenly.\n6. Gradually pour in the chicken or vegetable broth, stirring continuously. Bring the mixture to a boil.\n7. Reduce the heat to low and let the chowder simmer for about 15-20 minutes, or until the potatoes are tender.\n8. Stir in the remaining milk or cream and dried thyme. Season with salt and pepper to taste.\n9. Continue to cook the chowder for another 5 minutes, allowing the flavors to blend together.\n10. Remove the pot from heat and ladle the Corn Chowder into bowls.\n11. Garnish with crispy bacon and chopped fresh parsley.\n12. Serve hot and enjoy the creamy and comforting Corn Chowder!"
},
  {
  "name": "Mexican Street Corn (Elote)",
  "ingredients": [
    "4 ears of corn",
    "1/4 cup mayonnaise",
    "1/4 cup sour cream",
    "1/2 cup crumbled cotija cheese",
    "1/2 teaspoon chili powder",
    "1/4 teaspoon paprika",
    "1/4 cup chopped fresh cilantro",
    "1 lime, cut into wedges",
    "Salt and pepper to taste"
  ],
  "instructions": "1. Preheat a grill or grill pan over medium-high heat.\n2. Remove the husks and silk from the corn ears, and brush them with a little bit of olive oil.\n3. Grill the corn for about 8-10 minutes, rotating occasionally, until it is lightly charred and cooked through.\n4. In a small bowl, mix together the mayonnaise, sour cream, chili powder, paprika, and a pinch of salt and pepper.\n5. Once the corn is done, remove it from the grill and let it cool slightly.\n6. Brush the mayonnaise mixture onto each ear of corn, making sure to coat it evenly.\n7. Sprinkle the crumbled cotija cheese over the corn, pressing it gently so it sticks to the mayonnaise mixture.\n8. Garnish the corn with chopped fresh cilantro.\n9. Serve the Mexican Street Corn hot, with lime wedges on the side for squeezing over the corn.\n10. Enjoy the delicious and tangy flavors of Mexican Street Corn (Elote)!"
},
  {
  "name": "Cheesy Corn Casserole",
  "ingredients": [
    "2 cups corn kernels (fresh or frozen)",
    "1 cup shredded cheddar cheese",
    "1/2 cup shredded mozzarella cheese",
    "1/2 cup sour cream",
    "1/4 cup mayonnaise",
    "1/4 cup diced green chilies (optional)",
    "1/4 cup chopped green onions",
    "1/4 cup breadcrumbs",
    "2 tablespoons melted butter",
    "1/2 teaspoon garlic powder",
    "Salt and pepper to taste"
  ],
  "instructions": "1. Preheat your oven to 375°F (190°C) and lightly grease a baking dish.\n2. In a large bowl, combine the corn kernels, cheddar cheese, mozzarella cheese, sour cream, mayonnaise, diced green chilies (if using), and green onions. Mix well.\n3. Season the mixture with garlic powder, salt, and pepper to taste. Stir until all the ingredients are evenly combined.\n4. Transfer the corn mixture to the greased baking dish and spread it out in an even layer.\n5. In a separate bowl, combine the breadcrumbs and melted butter. Mix well until the breadcrumbs are coated with butter.\n6. Sprinkle the breadcrumb mixture over the top of the corn mixture in the baking dish.\n7. Bake the casserole in the preheated oven for about 25-30 minutes, or until the top is golden brown and the casserole is bubbly.\n8. Remove the casserole from the oven and let it cool for a few minutes.\n9. Serve the Cheesy Corn Casserole warm as a side dish or a main course.\n10. Enjoy the creamy and cheesy goodness of this delicious corn casserole!"
      },
  {
  "name": "Banana Chocolate Smoothie",
  "ingredients": [
    "2 ripe bananas",
    "1 cup milk (dairy or plant-based)",
    "2 tablespoons cocoa powder",
    "2 tablespoons honey or maple syrup",
    "1/2 teaspoon vanilla extract",
    "1 cup ice cubes"
  ],
  "instructions": "1. Peel the ripe bananas and break them into chunks.\n2. In a blender, combine the banana chunks, milk, cocoa powder, honey or maple syrup, and vanilla extract.\n3. Add the ice cubes to the blender.\n4. Blend all the ingredients together on high speed until smooth and creamy.\n5. Pause the blender and scrape down the sides if necessary, then continue blending until well combined.\n6. Taste the smoothie and adjust the sweetness or chocolate flavor to your liking by adding more honey, cocoa powder, or vanilla extract if desired.\n7. Once the desired consistency and taste are achieved, pour the smoothie into glasses.\n8. Optionally, garnish the smoothie with a sprinkle of cocoa powder or a banana slice.\n9. Serve immediately and enjoy the refreshing and chocolaty goodness of the Banana Chocolate Smoothie!"
},
  {
  "name": "Peanut Butter Banana Toast",
  "ingredients": [
    "2 slices of bread (your choice of bread)",
    "2 tablespoons peanut butter",
    "1 ripe banana, sliced",
    "Honey or maple syrup, for drizzling (optional)"
  ],
  "instructions": "1. Toast the slices of bread until golden and crisp.\n2. Spread one tablespoon of peanut butter onto each slice of toast.\n3. Arrange the sliced banana on top of one slice of the peanut butter-covered toast.\n4. Drizzle honey or maple syrup over the banana slices for added sweetness, if desired.\n5. Place the other slice of toast, peanut butter side down, on top of the banana slices to create a sandwich.\n6. Gently press the sandwich together.\n7. Slice the sandwich diagonally or into halves.\n8. Serve the Peanut Butter Banana Toast as a delicious and satisfying breakfast or snack.\n9. Enjoy the combination of creamy peanut butter, sweet bananas, and toasty bread!"
},
  {
  "name": "Greek Salad",
  "ingredients": [
    "2 large tomatoes, diced",
    "1 cucumber, diced",
    "1/2 red onion, thinly sliced",
    "1/2 cup Kalamata olives, pitted",
    "1/2 cup crumbled feta cheese",
    "1/4 cup extra virgin olive oil",
    "2 tablespoons red wine vinegar",
    "1 teaspoon dried oregano",
    "Salt and pepper to taste"
  ],
  "instructions": "1. In a large bowl, combine the diced tomatoes, diced cucumber, thinly sliced red onion, Kalamata olives, and crumbled feta cheese.\n2. In a separate small bowl, whisk together the extra virgin olive oil, red wine vinegar, dried oregano, salt, and pepper to make the dressing.\n3. Pour the dressing over the salad ingredients in the large bowl.\n4. Toss the salad gently to ensure all the ingredients are coated with the dressing.\n5. Taste and adjust the seasoning with more salt and pepper if needed.\n6. Let the Greek Salad sit for a few minutes to allow the flavors to meld together.\n7. Serve the salad as a refreshing and healthy side dish or as a light lunch.\n8. Enjoy the combination of fresh vegetables, tangy feta cheese, and Mediterranean flavors in this classic Greek Salad!" 
},
  {
  "name": "Chicken Parmesan",
  "ingredients": [
    "2 boneless, skinless chicken breasts",
    "1/2 cup breadcrumbs",
    "1/4 cup grated Parmesan cheese",
    "1 teaspoon dried basil",
    "1 teaspoon dried oregano",
    "1/2 teaspoon garlic powder",
    "1/2 teaspoon salt",
    "1/4 teaspoon black pepper",
    "1/4 cup all-purpose flour",
    "1 large egg, beaten",
    "2 tablespoons olive oil",
    "1 cup marinara sauce",
    "1/2 cup shredded mozzarella cheese",
    "Fresh basil leaves, for garnish"
  ],
  "instructions": "1. Preheat the oven to 400°F (200°C).\n2. In a shallow dish, combine the breadcrumbs, grated Parmesan cheese, dried basil, dried oregano, garlic powder, salt, and black pepper.\n3. Place the flour in a separate shallow dish and the beaten egg in another dish.\n4. Pound the chicken breasts to an even thickness, about 1/2 inch thick.\n5. Dredge each chicken breast in the flour, shaking off any excess.\n6. Dip the floured chicken breasts into the beaten egg, allowing any excess to drip off.\n7. Press the chicken breasts into the breadcrumb mixture, coating both sides evenly.\n8. In a large oven-safe skillet, heat the olive oil over medium heat.\n9. Add the breaded chicken breasts to the skillet and cook for 3-4 minutes on each side until golden brown.\n10. Remove the skillet from the heat and spoon marinara sauce over each chicken breast.\n11. Sprinkle shredded mozzarella cheese on top of each chicken breast.\n12. Transfer the skillet to the preheated oven and bake for 15-20 minutes until the chicken is cooked through and the cheese is melted and bubbly.\n13. Remove from the oven and let the chicken rest for a few minutes.\n14. Garnish with fresh basil leaves before serving.\n15. Serve the Chicken Parmesan with pasta or a side of your choice.\n16. Enjoy the crispy, cheesy goodness of Chicken Parmesan!" 
},
  {
  "name": "Avocado Toast",
  "ingredients": [
    "2 slices of bread (your choice of bread)",
    "1 ripe avocado",
    "Juice of 1/2 lemon",
    "Salt and pepper to taste",
    "Optional toppings: sliced tomatoes, red pepper flakes, feta cheese, microgreens, etc."
  ],
  "instructions": "1. Toast the slices of bread until golden and crisp.\n2. Cut the ripe avocado in half, remove the pit, and scoop out the flesh into a bowl.\n3. Mash the avocado with a fork until it reaches your desired consistency.\n4. Squeeze the lemon juice over the mashed avocado and mix well to combine.\n5. Season with salt and pepper to taste.\n6. Spread the avocado mixture evenly onto each slice of toast.\n7. Add your desired toppings such as sliced tomatoes, red pepper flakes, feta cheese, or microgreens.\n8. Serve the Avocado Toast as a delicious and nutritious breakfast or snack.\n9. Enjoy the creamy avocado and crunchy toast combination!" 
},
  {
  "name": "Blueberry Pancakes",
  "ingredients": [
    "1 cup all-purpose flour",
    "2 tablespoons sugar",
    "2 teaspoons baking powder",
    "1/2 teaspoon salt",
    "1 cup milk",
    "1 large egg",
    "2 tablespoons melted butter",
    "1 teaspoon vanilla extract",
    "1 cup fresh blueberries"
  ],
  "instructions": "1. In a large bowl, whisk together the flour, sugar, baking powder, and salt.\n2. In a separate bowl, whisk together the milk, egg, melted butter, and vanilla extract.\n3. Pour the wet ingredients into the dry ingredients and stir until just combined.\n4. Gently fold in the fresh blueberries.\n5. Heat a non-stick skillet or griddle over medium heat and lightly grease with butter or cooking spray.\n6. Spoon 1/4 cup of the pancake batter onto the skillet for each pancake.\n7. Cook until bubbles form on the surface of the pancake, then flip and cook for another 1-2 minutes until golden brown.\n8. Repeat with the remaining batter, adding more butter or cooking spray as needed.\n9. Serve the Blueberry Pancakes warm with maple syrup or your favorite toppings.\n10. Enjoy the fluffy pancakes bursting with juicy blueberries!" 
},
  {
  "name": "Classic Chocolate Chip Cookies",
  "ingredients": [
    "1 cup unsalted butter, softened",
    "1 cup granulated sugar",
    "1 cup packed brown sugar",
    "2 large eggs",
    "1 teaspoon vanilla extract",
    "3 cups all-purpose flour",
    "1 teaspoon baking soda",
    "1/2 teaspoon salt",
    "2 cups chocolate chips"
  ],
  "instructions": "1. Preheat the oven to 375°F (190°C) and line baking sheets with parchment paper.\n2. In a large bowl, cream together the softened butter, granulated sugar, and brown sugar until light and fluffy.\n3. Beat in the eggs one at a time, then stir in the vanilla extract.\n4. In a separate bowl, whisk together the flour, baking soda, and salt.\n5. Gradually add the dry ingredients to the butter mixture, mixing until just combined.\n6. Fold in the chocolate chips until evenly distributed throughout the dough.\n7. Drop rounded tablespoons of dough onto the prepared baking sheets, spacing them about 2 inches apart.\n8. Bake for 9-11 minutes, or until the edges are golden brown.\n9. Remove from the oven and let the cookies cool on the baking sheets for a few minutes, then transfer them to wire racks to cool completely.\n10. Enjoy the classic and irresistible taste of homemade chocolate chip cookies!" 
},
  {
  "name": "Chicken Noodle Soup",
  "ingredients": [
    "1 tablespoon olive oil",
    "1 onion, diced",
    "2 carrots, diced",
    "2 celery stalks, diced",
    "3 cloves garlic, minced",
    "8 cups chicken broth",
    "2 cups cooked chicken, shredded",
    "2 cups egg noodles",
    "1 teaspoon dried thyme",
    "1 bay leaf",
    "Salt and pepper to taste",
    "Fresh parsley, chopped (for garnish)"
  ],
  "instructions": "1. Heat the olive oil in a large pot over medium heat.\n2. Add the diced onion, carrots, celery, and minced garlic to the pot. Cook for 5-6 minutes, until the vegetables are softened.\n3. Pour in the chicken broth and add the shredded chicken, dried thyme, and bay leaf. Season with salt and pepper to taste.\n4. Bring the soup to a boil, then reduce the heat to low and let it simmer for 15-20 minutes to allow the flavors to meld together.\n5. Add the egg noodles to the pot and cook for an additional 8-10 minutes, or until the noodles are tender.\n6. Remove the bay leaf from the soup and discard.\n7. Taste the soup and adjust the seasoning if needed.\n8. Ladle the chicken noodle soup into bowls and garnish with freshly chopped parsley.\n9. Serve hot and enjoy the comforting and nourishing flavors of homemade chicken noodle soup!" 
},
 {
  "name": "Spinach and Feta Stuffed Chicken Breast",
  "ingredients": [
    "2 boneless, skinless chicken breasts",
    "1 cup fresh spinach leaves",
    "1/2 cup crumbled feta cheese",
    "2 tablespoons olive oil",
    "2 cloves garlic, minced",
    "1/2 teaspoon dried oregano",
    "Salt and pepper to taste"
  ],
  "instructions": "1. Preheat the oven to 400°F (200°C).\n2. Butterfly the chicken breasts by cutting them horizontally along one side, without cutting all the way through, and then opening them up like a book.\n3. Season the inside of the chicken breasts with salt, pepper, and dried oregano.\n4. Layer the fresh spinach leaves and crumbled feta cheese on one side of each chicken breast.\n5. Fold the other side of the chicken breast over the spinach and feta filling, pressing down gently to seal.\n6. In a small bowl, mix together the olive oil and minced garlic.\n7. Brush the olive oil and garlic mixture over the stuffed chicken breasts, coating them evenly.\n8. Place the stuffed chicken breasts in a baking dish and bake in the preheated oven for 25-30 minutes, or until the chicken is cooked through and no longer pink in the center.\n9. Remove from the oven and let the stuffed chicken breasts rest for a few minutes.\n10. Slice the stuffed chicken breasts crosswise into medallions.\n11. Serve the Spinach and Feta Stuffed Chicken Breast with a side of your choice, such as roasted vegetables or a salad.\n12. Enjoy the flavorful and tender chicken with the delicious spinach and feta filling!" 
},
  {
  "name": "Banana Bread",
  "ingredients": [
    "2 cups all-purpose flour",
    "1 teaspoon baking soda",
    "1/4 teaspoon salt",
    "1/2 cup unsalted butter, softened",
    "1 cup granulated sugar",
    "2 large eggs",
    "4 ripe bananas, mashed",
    "1/4 cup milk",
    "1 teaspoon vanilla extract"
  ],
  "instructions": "1. Preheat the oven to 350°F (175°C) and grease a 9x5-inch loaf pan.\n2. In a medium bowl, whisk together the flour, baking soda, and salt.\n3. In a large bowl, cream together the softened butter and sugar until light and fluffy.\n4. Beat in the eggs one at a time, then stir in the mashed bananas.\n5. Mix in the milk and vanilla extract until well combined.\n6. Gradually add the dry ingredients to the banana mixture, stirring until just combined.\n7. Pour the batter into the prepared loaf pan and smooth the top with a spatula.\n8. Bake for 60-70 minutes, or until a toothpick inserted into the center comes out clean.\n9. Remove from the oven and let the banana bread cool in the pan for 10 minutes.\n10. Transfer the banana bread to a wire rack to cool completely before slicing and serving.\n11. Enjoy the moist and flavorful homemade banana bread as a delicious snack or breakfast treat!" 
},
  {
  "name": "Garlic Shrimp Pasta",
  "ingredients": [
    "8 ounces linguine or spaghetti",
    "1 pound shrimp, peeled and deveined",
    "4 tablespoons butter, divided",
    "4 cloves garlic, minced",
    "1/4 teaspoon red pepper flakes (optional)",
    "1/4 cup chicken broth",
    "1/4 cup white wine (optional)",
    "1/4 cup heavy cream",
    "1/4 cup grated Parmesan cheese",
    "Salt and pepper to taste",
    "Chopped fresh parsley for garnish"
  ],
  "instructions": "1. Cook the linguine or spaghetti according to package instructions until al dente. Drain and set aside.\n2. In a large skillet, melt 2 tablespoons of butter over medium-high heat.\n3. Add the shrimp to the skillet and cook for 2-3 minutes per side until pink and cooked through. Remove the shrimp from the skillet and set aside.\n4. In the same skillet, melt the remaining 2 tablespoons of butter.\n5. Add the minced garlic and red pepper flakes (if using) to the skillet. Sauté for about 1 minute until fragrant.\n6. Pour in the chicken broth and white wine (if using), and let it simmer for 2-3 minutes to reduce slightly.\n7. Stir in the heavy cream and grated Parmesan cheese. Cook for another 2-3 minutes until the sauce thickens.\n8. Season with salt and pepper to taste.\n9. Add the cooked shrimp back to the skillet and toss to coat with the sauce.\n10. Add the cooked linguine or spaghetti to the skillet and toss to combine with the shrimp and sauce.\n11. Garnish with chopped fresh parsley.\n12. Serve the garlic shrimp pasta hot and enjoy!" 
},
  {
  "name": "Beef and Broccoli Stir-Fry",
  "ingredients": [
    "1 pound flank steak, thinly sliced",
    "2 cups broccoli florets",
    "1 red bell pepper, sliced",
    "1 onion, sliced",
    "3 cloves garlic, minced",
    "1/4 cup soy sauce",
    "2 tablespoons oyster sauce",
    "1 tablespoon cornstarch",
    "1 tablespoon vegetable oil",
    "1/2 teaspoon sesame oil",
    "Salt and pepper to taste",
    "Cooked rice or noodles for serving"
  ],
  "instructions": "1. In a small bowl, whisk together soy sauce, oyster sauce, cornstarch, and a pinch of salt and pepper.\n2. In a large skillet or wok, heat vegetable oil over high heat.\n3. Add minced garlic and cook for 30 seconds until fragrant.\n4. Add thinly sliced flank steak to the skillet and stir-fry for 2-3 minutes until browned and cooked through. Remove the beef from the skillet and set aside.\n5. In the same skillet, add broccoli florets, sliced bell pepper, and onion. Stir-fry for 3-4 minutes until the vegetables are tender-crisp.\n6. Return the cooked beef to the skillet and pour the sauce mixture over the ingredients.\n7. Stir well to coat the beef and vegetables in the sauce. Cook for an additional 1-2 minutes until the sauce thickens.\n8. Drizzle sesame oil over the stir-fry and give it a final toss.\n9. Remove from heat and serve the Beef and Broccoli Stir-Fry over cooked rice or noodles.\n10. Enjoy this flavorful and satisfying dish!"
},
  {
  "name": "Broccoli Corn Stir-Fry",
  "ingredients": [
    "2 cups broccoli florets",
    "1 cup corn kernels (fresh or frozen)",
    "1 red bell pepper, thinly sliced",
    "1 small onion, thinly sliced",
    "2 cloves garlic, minced",
    "2 tablespoons soy sauce",
    "1 tablespoon oyster sauce",
    "1 teaspoon sesame oil",
    "1 tablespoon vegetable oil",
    "Salt and pepper to taste",
    "Sesame seeds for garnish (optional)"
  ],
  "instructions": "1. Heat vegetable oil in a large skillet or wok over medium-high heat.\n2. Add the minced garlic and sauté for 1-2 minutes until fragrant.\n3. Add the sliced onion and red bell pepper to the skillet. Stir-fry for about 2-3 minutes until the vegetables start to soften.\n4. Add the broccoli florets and corn kernels to the skillet. Stir-fry for an additional 3-4 minutes until the broccoli is tender-crisp.\n5. In a small bowl, whisk together the soy sauce, oyster sauce, and sesame oil.\n6. Pour the sauce mixture over the vegetables in the skillet. Stir-fry for another minute to coat the vegetables evenly.\n7. Season with salt and pepper to taste.\n8. Remove the skillet from heat and transfer the stir-fried broccoli corn to a serving dish.\n9. Garnish with sesame seeds if desired.\n10. Serve the delicious and vibrant Broccoli Corn Stir-Fry as a side dish or with steamed rice for a complete meal.\n11. Enjoy the flavorful combination of broccoli, corn, and Asian-inspired sauces!" 
},
  {
  "name": "Broccoli Corn Soup",
  "ingredients": [
    "2 cups broccoli florets",
    "1 cup corn kernels (fresh or frozen)",
    "1 small onion, chopped",
    "2 cloves garlic, minced",
    "4 cups vegetable or chicken broth",
    "1/2 cup heavy cream",
    "2 tablespoons butter",
    "1 tablespoon all-purpose flour",
    "Salt and pepper to taste",
    "Chopped fresh parsley for garnish (optional)"
  ],
  "instructions": "1. In a large pot, melt the butter over medium heat. Add the chopped onion and minced garlic, and sauté until the onion becomes translucent.\n2. Add the broccoli florets and corn kernels to the pot, and cook for a few minutes until they start to soften.\n3. Sprinkle the flour over the vegetables and stir well to coat them evenly. Cook for another minute to cook off the raw flour taste.\n4. Gradually pour in the vegetable or chicken broth, stirring constantly to avoid lumps. Bring the mixture to a boil.\n5. Reduce the heat to low and simmer for about 15-20 minutes, or until the vegetables are tender.\n6. Use an immersion blender or transfer the soup to a blender, and blend until smooth and creamy.\n7. Return the soup to the pot (if using a blender), and stir in the heavy cream. Season with salt and pepper to taste.\n8. Heat the soup over low heat until warmed through, but do not boil.\n9. Ladle the broccoli corn soup into bowls and garnish with chopped fresh parsley if desired.\n10. Serve the comforting and creamy Broccoli Corn Soup as a satisfying meal on its own or with a side of crusty bread.\n11. Enjoy the delicious and nourishing flavors of this homemade soup!" 
},
  {
  "name": "Strawberry Lemonade",
  "ingredients": [
    "1 cup fresh strawberries, hulled and sliced",
    "1/2 cup freshly squeezed lemon juice",
    "1/2 cup granulated sugar",
    "4 cups cold water",
    "Ice cubes",
    "Fresh mint leaves for garnish (optional)"
  ],
  "instructions": "1. In a blender, combine the sliced strawberries, lemon juice, and granulated sugar. Blend until smooth and well combined.\n2. Pour the strawberry mixture into a pitcher.\n3. Add cold water to the pitcher and stir well to combine.\n4. Taste the lemonade and adjust the sweetness by adding more sugar if desired.\n5. Fill glasses with ice cubes and pour the strawberry lemonade over the ice.\n6. Garnish with fresh mint leaves if desired.\n7. Serve the refreshing and tangy Strawberry Lemonade chilled and enjoy it on a hot day!\nNote: You can also strain the strawberry mixture before adding water if you prefer a smoother consistency." 
},
  {
  "name": "Broccoli and Chicken Stir-Fry",
  "ingredients": [
    "2 cups broccoli florets",
    "2 boneless, skinless chicken breasts, thinly sliced",
    "2 cloves garlic, minced",
    "1 tablespoon soy sauce",
    "1 tablespoon oyster sauce",
    "1 tablespoon sesame oil",
    "1 tablespoon vegetable oil",
    "Salt and pepper to taste"
  ],
  "instructions": "1. Heat vegetable oil in a large skillet or wok over medium-high heat.\n2. Add minced garlic to the skillet and sauté for about 30 seconds until fragrant.\n3. Add the sliced chicken to the skillet and stir-fry until it is cooked through and lightly browned.\n4. Add the broccoli florets to the skillet and stir-fry for 3-4 minutes until they are bright green and tender-crisp.\n5. In a small bowl, whisk together soy sauce, oyster sauce, and sesame oil.\n6. Pour the sauce mixture over the chicken and broccoli in the skillet. Stir well to coat the ingredients evenly.\n7. Season with salt and pepper to taste.\n8. Continue stir-frying for another 1-2 minutes until the sauce is heated through.\n9. Remove from heat and transfer the stir-fried broccoli and chicken to a serving dish.\n10. Serve hot as a main course with steamed rice.\n11. Enjoy your delicious Broccoli and Chicken Stir-Fry!"
},
  {
  "name": "Mango Lassi",
  "ingredients": [
    "1 ripe mango, peeled and diced",
    "1 cup plain yogurt",
    "1/2 cup milk",
    "2 tablespoons sugar, or to taste",
    "1/2 teaspoon ground cardamom (optional)",
    "Ice cubes"
  ],
  "instructions": "1. In a blender, combine the diced mango, plain yogurt, milk, sugar, and ground cardamom (if using).\n2. Blend until smooth and creamy.\n3. Taste the mango lassi and adjust the sweetness by adding more sugar if desired.\n4. Add a few ice cubes to the blender and blend again until the lassi is chilled and frothy.\n5. Pour the mango lassi into glasses.\n6. Garnish with a sprinkle of ground cardamom or a mango slice if desired.\n7. Serve the delicious and refreshing Mango Lassi chilled as a perfect beverage or snack!\nNote: You can also add a splash of rose water or a squeeze of lime juice for additional flavor variations." 
},
  {
  "name": "Pad Thai",
  "ingredients": [
    "8 oz rice noodles",
    "2 tablespoons vegetable oil",
    "2 cloves garlic, minced",
    "4 oz shrimp, peeled and deveined",
    "1 egg, lightly beaten",
    "1 cup bean sprouts",
    "2 green onions, sliced",
    "1/4 cup crushed peanuts",
    "2 tablespoons fish sauce",
    "2 tablespoons tamarind paste",
    "1 tablespoon sugar",
    "1/2 teaspoon chili powder",
    "Lime wedges for serving",
    "Cilantro for garnish"
  ],
  "instructions": "1. Cook the rice noodles according to the package instructions, then drain and set aside.\n2. In a large skillet or wok, heat the vegetable oil over medium-high heat.\n3. Add the minced garlic and sauté for about 30 seconds until fragrant.\n4. Add the shrimp to the skillet and cook until pink and cooked through, about 2-3 minutes.\n5. Push the shrimp to one side of the skillet and pour the beaten egg into the other side. Scramble the egg until cooked, then mix it with the shrimp.\n6. Add the cooked rice noodles to the skillet and toss to combine with the shrimp and egg.\n7. Stir in the bean sprouts, sliced green onions, and crushed peanuts.\n8. In a small bowl, whisk together the fish sauce, tamarind paste, sugar, and chili powder. Pour the sauce over the noodles and stir well to coat.\n9. Cook for another 1-2 minutes until everything is heated through.\n10. Remove from heat and transfer the Pad Thai to serving plates.\n11. Serve hot with lime wedges on the side and garnish with cilantro.\n12. Enjoy your delicious Pad Thai!"
},
  {
  "name": "Chocolate Mousse",
  "ingredients": [
    "8 ounces (225g) bittersweet chocolate, chopped",
    "1 cup heavy cream",
    "3 tablespoons granulated sugar",
    "4 large egg whites",
    "1/4 teaspoon cream of tartar",
    "1/2 teaspoon vanilla extract",
    "Whipped cream and chocolate shavings for garnish (optional)"
  ],
  "instructions": "1. Place the chopped chocolate in a heatproof bowl and set it aside.\n2. In a separate bowl, whip the heavy cream and 1 tablespoon of sugar until soft peaks form. Refrigerate until needed.\n3. In a clean bowl, beat the egg whites until frothy. Add the cream of tartar and continue beating until soft peaks form.\n4. Gradually add the remaining 2 tablespoons of sugar while continuing to beat until stiff peaks form.\n5. In a small saucepan, bring about an inch of water to a simmer. Place the bowl with the chocolate over the saucepan, making sure the bottom of the bowl doesn't touch the water.\n6. Stir the chocolate occasionally until it is melted and smooth. Remove the bowl from heat and let it cool slightly.\n7. Fold the whipped cream into the melted chocolate until well combined.\n8. Gently fold in the beaten egg whites, followed by the vanilla extract. Mix until the mousse is smooth and fluffy.\n9. Divide the chocolate mousse into serving glasses or bowls.\n10. Refrigerate for at least 2 hours or until set.\n11. Before serving, garnish with whipped cream and chocolate shavings if desired.\n12. Enjoy the decadent and creamy Chocolate Mousse as a delightful dessert!" 
},
  {
  "name": "Apple Crisp",
  "ingredients": [
    "4 cups sliced apples (about 4 medium-sized apples)",
    "1/2 cup all-purpose flour",
    "1/2 cup rolled oats",
    "1/2 cup packed brown sugar",
    "1/2 teaspoon ground cinnamon",
    "1/4 teaspoon ground nutmeg",
    "1/4 teaspoon salt",
    "1/2 cup cold unsalted butter, diced",
    "Vanilla ice cream or whipped cream for serving (optional)"
  ],
  "instructions": "1. Preheat the oven to 375°F (190°C) and lightly grease a 9-inch square baking dish.\n2. In a large bowl, combine the sliced apples, flour, rolled oats, brown sugar, cinnamon, nutmeg, and salt. Toss until the apples are evenly coated.\n3. Transfer the apple mixture to the prepared baking dish and spread it out evenly.\n4. In the same bowl (no need to wash it), add the cold diced butter. Using your fingertips or a pastry cutter, cut the butter into the flour mixture until it resembles coarse crumbs.\n5. Sprinkle the crumb mixture evenly over the apples in the baking dish.\n6. Bake for about 30-35 minutes or until the topping is golden brown and the apples are tender.\n7. Remove the apple crisp from the oven and let it cool slightly.\n8. Serve warm, optionally with a scoop of vanilla ice cream or a dollop of whipped cream.\n9. Enjoy the warm and comforting Apple Crisp as a delicious dessert!" 
},
  {
  "name": "Green Papaya Salad",
  "ingredients": [
    "1 small green papaya, shredded",
    "2 cloves garlic",
    "2 Thai chilies, chopped",
    "2 tablespoons fish sauce",
    "1 tablespoon palm sugar",
    "2 tablespoons lime juice",
    "1 cup cherry tomatoes, halved",
    "1/4 cup roasted peanuts, crushed",
    "2 tablespoons dried shrimp (optional)",
    "2 tablespoons green beans, cut into 1-inch pieces",
    "2 tablespoons carrots, julienned",
    "Fresh cilantro for garnish"
  ],
  "instructions": "1. In a mortar and pestle, pound the garlic and Thai chilies into a paste.\n2. Add the fish sauce, palm sugar, and lime juice to the mortar and mix well until the sugar is dissolved.\n3. In a large mixing bowl, combine the shredded green papaya, cherry tomatoes, roasted peanuts, dried shrimp (if using), green beans, and carrots.\n4. Pour the dressing over the ingredients in the bowl and toss well to coat.\n5. Taste and adjust the seasoning by adding more fish sauce, sugar, or lime juice if desired.\n6. Transfer the green papaya salad to a serving plate.\n7. Garnish with fresh cilantro.\n8. Serve immediately and enjoy your refreshing Green Papaya Salad!"
},
  {
  "name": "Parmesan Garlic Roasted Chickpeas",
  "ingredients": [
    "2 cans chickpeas (15 ounces each), drained and rinsed",
    "2 tablespoons olive oil",
    "2 tablespoons grated Parmesan cheese",
    "1 teaspoon garlic powder",
    "1/2 teaspoon salt",
    "1/4 teaspoon black pepper",
    "1/4 teaspoon paprika",
    "1/4 teaspoon dried parsley"
  ],
  "instructions": "1. Preheat the oven to 400°F (200°C) and line a baking sheet with parchment paper.\n2. In a bowl, combine the drained and rinsed chickpeas, olive oil, grated Parmesan cheese, garlic powder, salt, black pepper, paprika, and dried parsley. Toss well to coat the chickpeas evenly.\n3. Spread the seasoned chickpeas in a single layer on the prepared baking sheet.\n4. Bake for 25-30 minutes, stirring once or twice during baking, until the chickpeas are golden brown and crispy.\n5. Remove the baking sheet from the oven and let the roasted chickpeas cool for a few minutes.\n6. Serve the Parmesan Garlic Roasted Chickpeas as a tasty and nutritious snack. Enjoy them on their own or as a crunchy addition to salads or soups!\nNote: The roasted chickpeas are best enjoyed on the day they are made, as they can lose their crispiness over time." 
},
  {
  "name": "Green Papaya Salad",
  "ingredients": [
    "1 small green papaya, shredded",
    "2 cloves garlic",
    "2 Thai chilies, chopped",
    "2 tablespoons fish sauce",
    "1 tablespoon palm sugar",
    "2 tablespoons lime juice",
    "1 cup cherry tomatoes, halved",
    "1/4 cup roasted peanuts, crushed",
    "2 tablespoons dried shrimp (optional)",
    "2 tablespoons green beans, cut into 1-inch pieces",
    "2 tablespoons carrots, julienned",
    "Fresh cilantro for garnish"
  ],
  "instructions": "1. In a mortar and pestle, pound the garlic and Thai chilies into a paste.\n2. Add the fish sauce, palm sugar, and lime juice to the mortar and mix well until the sugar is dissolved.\n3. In a large mixing bowl, combine the shredded green papaya, cherry tomatoes, roasted peanuts, dried shrimp (if using), green beans, and carrots.\n4. Pour the dressing over the ingredients in the bowl and toss well to coat.\n5. Taste and adjust the seasoning by adding more fish sauce, sugar, or lime juice if desired.\n6. Transfer the green papaya salad to a serving plate.\n7. Garnish with fresh cilantro.\n8. Serve immediately and enjoy your refreshing Green Papaya Salad!"
},
  {
  "name": "Caprese Skewers",
  "ingredients": [
    "Cherry tomatoes",
    "Fresh basil leaves",
    "Fresh mozzarella balls",
    "Balsamic glaze",
    "Extra virgin olive oil",
    "Salt and pepper"
  ],
  "instructions": "1. Prepare the ingredients by rinsing the cherry tomatoes and basil leaves. Drain and pat dry the mozzarella balls.\n2. Take a toothpick or small skewer and thread on a cherry tomato, followed by a basil leaf, and then a mozzarella ball.\n3. Repeat the process until you have made enough skewers.\n4. Arrange the Caprese skewers on a serving platter or plate.\n5. Drizzle balsamic glaze and extra virgin olive oil over the skewers.\n6. Sprinkle with a pinch of salt and pepper to taste.\n7. Serve the Caprese Skewers as a delightful and colorful appetizer. They are perfect for parties, gatherings, or as a light snack!\nNote: You can also add a small folded piece of prosciutto or salami between the tomato and basil leaf for additional flavor." 
},
  {
  "name": "Guacamole",
  "ingredients": [
    "2 ripe avocados",
    "1 small onion, finely diced",
    "1 ripe tomato, diced",
    "1 jalapeño pepper, seeded and minced",
    "2 tablespoons fresh lime juice",
    "1/4 cup chopped fresh cilantro",
    "1/2 teaspoon salt",
    "1/4 teaspoon ground cumin",
    "1/4 teaspoon garlic powder",
    "Tortilla chips, for serving"
  ],
  "instructions": "1. Cut the avocados in half lengthwise and remove the pit. Scoop the avocado flesh into a bowl.\n2. Mash the avocados with a fork until you achieve your desired consistency (smooth or chunky).\n3. Add the finely diced onion, diced tomato, minced jalapeño pepper, lime juice, chopped cilantro, salt, cumin, and garlic powder to the bowl with the mashed avocados.\n4. Mix all the ingredients together until well combined.\n5. Taste the guacamole and adjust the seasoning if needed, adding more salt or lime juice to taste.\n6. Transfer the guacamole to a serving bowl.\n7. Serve the delicious and creamy guacamole with tortilla chips as a classic and crowd-pleasing snack or appetizer!\nNote: You can also customize your guacamole by adding additional ingredients like diced garlic, chopped jalapeños, or diced bell peppers for extra flavor and heat." 
},
  {
  "name": "Panang Curry",
  "ingredients": [
    "1 pound chicken (or beef, pork, or tofu), thinly sliced",
    "2 tablespoons panang curry paste",
    "1 can (13.5 ounces) coconut milk",
    "1 cup chicken broth",
    "1 red bell pepper, thinly sliced",
    "1 small onion, thinly sliced",
    "1 tablespoon fish sauce",
    "1 tablespoon palm sugar or brown sugar",
    "1 tablespoon lime juice",
    "1/4 cup fresh Thai basil leaves",
    "Cooked rice for serving"
  ],
  "instructions": "1. In a wok or large skillet, heat some oil over medium heat. Add the panang curry paste and stir-fry for about 1 minute until fragrant.\n2. Add the sliced chicken to the wok and cook until browned and cooked through.\n3. Pour in the coconut milk and chicken broth, and stir well to combine. Bring the mixture to a gentle simmer.\n4. Add the sliced red bell pepper and onion to the curry, and cook for about 5 minutes until the vegetables are tender-crisp.\n5. Stir in the fish sauce, palm sugar, and lime juice. Taste and adjust the seasoning as needed.\n6. Remove the panang curry from the heat and stir in the fresh Thai basil leaves.\n7. Serve the Panang Curry over cooked rice.\n8. Enjoy your flavorful and aromatic Panang Curry!"
},
  {
  "name": "Hummus with Pita Chips",
  "ingredients": [
    "1 can chickpeas (15 ounces), drained and rinsed",
    "3 tablespoons tahini",
    "2 tablespoons lemon juice",
    "2 tablespoons olive oil",
    "2 cloves garlic, minced",
    "1/2 teaspoon cumin",
    "Salt to taste",
    "Water (if needed for consistency)",
    "Pita bread, cut into triangles",
    "Olive oil for brushing"
  ],
  "instructions": "1. In a food processor, combine the drained and rinsed chickpeas, tahini, lemon juice, olive oil, minced garlic, cumin, and a pinch of salt.\n2. Process the mixture until smooth and creamy. If needed, add water gradually to achieve your desired consistency.\n3. Taste the hummus and adjust the seasoning by adding more salt or lemon juice if desired.\n4. Transfer the hummus to a serving bowl.\n5. Preheat the oven to 350°F (175°C).\n6. Brush the pita bread triangles with olive oil on both sides.\n7. Place the pita triangles on a baking sheet and bake for about 10-12 minutes, or until crispy and golden brown.\n8. Remove the pita chips from the oven and let them cool.\n9. Serve the homemade hummus with the freshly baked pita chips.\n10. Enjoy the creamy and flavorful Hummus with Pita Chips as a delicious and healthy snack or appetizer!" 
},
  {
  "name": "Mango Sticky Rice",
  "ingredients": [
    "1 cup sticky rice",
    "2 ripe mangoes",
    "1 cup coconut milk",
    "1/2 cup sugar",
    "1/4 teaspoon salt",
    "Toasted sesame seeds (for garnish)"
  ],
  "instructions": "1. Soak the sticky rice in water for at least 4 hours or overnight.\n2. Rinse the soaked rice and drain well. Place the rice in a steamer basket lined with cheesecloth or a muslin cloth.\n3. Steam the rice over medium-high heat for about 20-25 minutes until cooked and tender.\n4. While the rice is steaming, prepare the coconut sauce. In a saucepan, heat the coconut milk, sugar, and salt over medium heat. Stir until the sugar dissolves and the mixture is heated through. Remove from heat.\n5. Once the rice is cooked, transfer it to a bowl and pour half of the coconut sauce over the rice. Mix well to coat the rice with the sauce.\n6. Let the rice sit for a few minutes to absorb the sauce.\n7. Peel and slice the ripe mangoes.\n8. Serve the mango slices with the sticky rice, drizzle with the remaining coconut sauce, and sprinkle with toasted sesame seeds.\n9. Enjoy your sweet and creamy Mango Sticky Rice!"
},
  {
  "name": "Massaman Curry",
  "ingredients": [
    "1 pound beef (or chicken, pork, or tofu), cut into bite-sized pieces",
    "2 tablespoons massaman curry paste",
    "1 can (13.5 ounces) coconut milk",
    "1 cup beef or chicken broth",
    "1 large potato, peeled and cut into chunks",
    "1 small onion, sliced",
    "1/2 cup roasted peanuts",
    "2 tablespoons fish sauce",
    "1 tablespoon tamarind paste",
    "1 tablespoon palm sugar or brown sugar",
    "1 cinnamon stick",
    "2 cardamom pods",
    "2 star anise",
    "Cooked rice for serving"
  ],
  "instructions": "1. In a large pot or Dutch oven, heat some oil over medium heat. Add the massaman curry paste and stir-fry for about 1 minute until fragrant.\n2. Add the beef to the pot and cook until browned on all sides.\n3. Pour in the coconut milk and beef or chicken broth, and stir well to combine. Bring the mixture to a gentle simmer.\n4. Add the potato chunks, sliced onion, roasted peanuts, fish sauce, tamarind paste, and sugar to the curry. Stir to combine.\n5. Tie the cinnamon stick, cardamom pods, and star anise in a piece of cheesecloth or place them in a spice bag. Add the spice bundle to the pot.\n6. Cover the pot and let the curry simmer for about 1 hour, or until the beef and potatoes are tender.\n7. Remove the spice bundle from the curry.\n8. Serve the Massaman Curry over cooked rice.\n9. Enjoy the rich and flavorful Massaman Curry!"
},
  {
  "name": "General Tso's Chicken",
  "ingredients": [
    "1 pound boneless, skinless chicken thighs, cut into bite-sized pieces",
    "1/2 cup cornstarch",
    "2 tablespoons vegetable oil",
    "3 cloves garlic, minced",
    "1 tablespoon ginger, minced",
    "1/4 cup soy sauce",
    "1/4 cup hoisin sauce",
    "2 tablespoons rice vinegar",
    "2 tablespoons honey",
    "1 tablespoon cornstarch, dissolved in 2 tablespoons water",
    "1/2 teaspoon red pepper flakes (adjust to taste)",
    "1/4 cup green onions, chopped (for garnish)",
    "Sesame seeds (for garnish)"
  ],
  "instructions": "1. In a shallow bowl, coat the chicken pieces with cornstarch.\n2. Heat the vegetable oil in a large skillet or wok over medium-high heat.\n3. Add the coated chicken pieces to the skillet and cook until golden brown and crispy. Remove from the skillet and set aside.\n4. In the same skillet, add the minced garlic and ginger. Sauté for a minute until fragrant.\n5. In a small bowl, whisk together the soy sauce, hoisin sauce, rice vinegar, honey, and cornstarch-water mixture.\n6. Pour the sauce mixture into the skillet and bring to a simmer. Cook until the sauce thickens.\n7. Add the cooked chicken pieces back into the skillet and toss to coat them with the sauce.\n8. Sprinkle with red pepper flakes and toss to combine.\n9. Remove from heat and garnish with chopped green onions and sesame seeds.\n10. Serve hot with steamed rice.\n11. Enjoy your delicious General Tso's Chicken!"
},
  {
  "name": "Tomato and Egg Stir-Fry",
  "ingredients": [
    "3 tomatoes, diced",
    "4 eggs, beaten",
    "2 green onions, chopped",
    "2 cloves garlic, minced",
    "1 tablespoon soy sauce",
    "1/2 teaspoon sugar",
    "1/2 teaspoon salt",
    "1/4 teaspoon black pepper",
    "2 tablespoons vegetable oil"
  ],
  "instructions": "1. Heat vegetable oil in a large skillet or wok over medium heat.\n2. Add minced garlic and chopped green onions to the skillet. Sauté for 1-2 minutes until fragrant.\n3. Add diced tomatoes to the skillet. Cook for 3-4 minutes until the tomatoes start to soften.\n4. In a small bowl, whisk together beaten eggs, soy sauce, sugar, salt, and black pepper.\n5. Push the tomatoes to one side of the skillet and pour the beaten egg mixture into the empty space.\n6. Allow the eggs to cook undisturbed for a few seconds until they start to set around the edges.\n7. Gently scramble the eggs with a spatula, incorporating them with the tomatoes.\n8. Continue cooking for another 2-3 minutes until the eggs are fully cooked.\n9. Season with additional salt and pepper to taste.\n10. Remove from heat and transfer the Tomato and Egg Stir-Fry to a serving dish.\n11. Serve hot as a side dish or over steamed rice.\n12. Enjoy your delicious Tomato and Egg Stir-Fry!"
},
  {
  "name": "Tomato Bruschetta",
  "ingredients": [
    "4 ripe tomatoes, diced",
    "2 cloves garlic, minced",
    "1/4 cup fresh basil leaves, chopped",
    "2 tablespoons extra virgin olive oil",
    "1 tablespoon balsamic vinegar",
    "Salt and pepper to taste",
    "Baguette or bread slices"
  ],
  "instructions": "1. In a bowl, combine the diced tomatoes, minced garlic, chopped basil leaves, olive oil, and balsamic vinegar.\n2. Season the mixture with salt and pepper to taste and stir well.\n3. Allow the tomato mixture to marinate for about 15-20 minutes to let the flavors meld together.\n4. Preheat the oven to broil.\n5. Slice the baguette or bread into thin slices and arrange them on a baking sheet.\n6. Toast the bread slices under the broiler for a few minutes until they turn golden and crispy.\n7. Remove the toasted bread slices from the oven and let them cool slightly.\n8. Spoon the tomato mixture onto each toasted bread slice, distributing it evenly.\n9. Garnish with additional basil leaves, if desired.\n10. Serve the Tomato Bruschetta as an appetizer or light snack.\n11. Enjoy the vibrant flavors of the Tomato Bruschetta!"
},
  {
  "name": "Spicy Black Bean Burger",
  "ingredients": [
    "1 can black beans, drained and rinsed",
    "1/2 cup bread crumbs",
    "1/4 cup red bell pepper, finely chopped",
    "1/4 cup onion, finely chopped",
    "2 cloves garlic, minced",
    "1 teaspoon cumin",
    "1 teaspoon chili powder",
    "1/2 teaspoon paprika",
    "1/4 teaspoon cayenne pepper (optional)",
    "1/4 cup cilantro, chopped",
    "1 tablespoon lime juice",
    "Salt and pepper to taste",
    "Burger buns",
    "Toppings of your choice (lettuce, tomato, onion, avocado, etc.)"
  ],
  "instructions": "1. In a bowl, mash the black beans with a fork or potato masher until mostly smooth.\n2. Add the bread crumbs, red bell pepper, onion, garlic, cumin, chili powder, paprika, cayenne pepper (if using), cilantro, lime juice, salt, and pepper to the mashed black beans.\n3. Mix well until all the ingredients are combined.\n4. Divide the mixture into equal-sized patties, shaping them with your hands.\n5. Heat a grill pan or skillet over medium heat and lightly grease it with oil.\n6. Cook the black bean patties for about 4-5 minutes per side, or until they are heated through and develop a golden crust.\n7. Toast the burger buns, if desired.\n8. Place each black bean patty on a burger bun and add your preferred toppings.\n9. Serve the Spicy Black Bean Burgers hot and enjoy!\n10. These burgers are also delicious served with a side of fries or a salad."
},
  {
  "name": "Teriyaki Chicken Burger",
  "ingredients": [
    "1 pound ground chicken",
    "1/4 cup teriyaki sauce",
    "2 tablespoons breadcrumbs",
    "1 tablespoon grated ginger",
    "1 clove garlic, minced",
    "1/2 teaspoon sesame oil",
    "1/4 teaspoon black pepper",
    "4 burger buns",
    "Lettuce leaves",
    "Sliced tomatoes",
    "Sliced onions",
    "Mayonnaise (optional)"
  ],
  "instructions": "1. In a bowl, combine the ground chicken, teriyaki sauce, breadcrumbs, grated ginger, minced garlic, sesame oil, and black pepper.\n2. Mix well until all the ingredients are evenly incorporated.\n3. Divide the chicken mixture into 4 equal-sized patties.\n4. Preheat a grill or skillet over medium heat and lightly grease it with oil.\n5. Cook the chicken patties for about 5-6 minutes per side, or until they are cooked through and reach an internal temperature of 165°F (74°C).\n6. While the patties are cooking, toast the burger buns if desired.\n7. Assemble the Teriyaki Chicken Burgers by placing a lettuce leaf, a chicken patty, sliced tomatoes, and sliced onions on each bun.\n8. Spread mayonnaise on the bun if desired.\n9. Serve the Teriyaki Chicken Burgers hot and enjoy!\n10. These burgers pair well with a side of sweet potato fries or a fresh salad."
},
  {
  "name": "Portobello Mushroom Burger",
  "ingredients": [
    "4 large Portobello mushroom caps",
    "4 burger buns",
    "4 slices of Swiss cheese",
    "1 red onion, sliced",
    "4 lettuce leaves",
    "4 tomato slices",
    "4 tablespoons mayonnaise",
    "2 tablespoons balsamic vinegar",
    "2 tablespoons olive oil",
    "2 cloves garlic, minced",
    "1 teaspoon dried thyme",
    "Salt and pepper to taste"
  ],
  "instructions": "1. Preheat the grill or grill pan over medium-high heat.\n2. In a small bowl, whisk together the balsamic vinegar, olive oil, minced garlic, dried thyme, salt, and pepper.\n3. Brush both sides of the Portobello mushroom caps with the marinade.\n4. Place the mushrooms on the grill and cook for 4-5 minutes per side, or until tender.\n5. While the mushrooms are grilling, toast the burger buns on the grill until lightly browned.\n6. Remove the mushrooms from the grill and let them rest for a few minutes.\n7. Assemble the burgers by spreading mayonnaise on the bottom bun, followed by a lettuce leaf, a tomato slice, a grilled Portobello mushroom cap, a slice of Swiss cheese, and some sliced red onion.\n8. Place the top bun on the burger and serve.\n9. Enjoy your delicious Portobello Mushroom Burger!"
},
  {
  "name": "Loaded Cheese Fries",
  "ingredients": [
    "4 large potatoes, washed and cut into fries",
    "1 cup shredded cheddar cheese",
    "4 slices bacon, cooked and crumbled",
    "2 green onions, thinly sliced",
    "1/4 cup sour cream",
    "1/4 cup mayonnaise",
    "1 teaspoon garlic powder",
    "1/2 teaspoon paprika",
    "Salt and pepper to taste"
  ],
  "instructions": "1. Preheat the oven to 425°F (220°C) and line a baking sheet with parchment paper.\n2. In a large bowl, toss the cut potatoes with olive oil, salt, pepper, and paprika until evenly coated.\n3. Arrange the seasoned potato fries in a single layer on the prepared baking sheet.\n4. Bake in the preheated oven for 25-30 minutes, or until the fries are crispy and golden brown.\n5. In a small bowl, combine the sour cream, mayonnaise, garlic powder, and salt. Stir well to combine.\n6. Once the fries are cooked, remove them from the oven and sprinkle the shredded cheddar cheese over the hot fries.\n7. Return the baking sheet to the oven for 2-3 minutes, or until the cheese is melted and bubbly.\n8. Remove the loaded fries from the oven and let them cool slightly.\n9. Sprinkle the crumbled bacon and sliced green onions over the cheese-topped fries.\n10. Serve the loaded cheese fries with the sour cream and mayonnaise dipping sauce on the side.\n11. Enjoy your delicious Loaded Cheese Fries!"
},
  {
  "name": "Sweet Potato Fries",
  "ingredients": [
    "2 large sweet potatoes",
    "2 tablespoons olive oil",
    "1 teaspoon paprika",
    "1/2 teaspoon garlic powder",
    "1/2 teaspoon salt",
    "1/4 teaspoon black pepper",
    "1/4 teaspoon cayenne pepper (optional)"
  ],
  "instructions": "1. Preheat the oven to 425°F (220°C) and line a baking sheet with parchment paper.\n2. Wash and peel the sweet potatoes. Cut them into even-sized fries.\n3. In a large bowl, toss the sweet potato fries with olive oil, paprika, garlic powder, salt, black pepper, and cayenne pepper (if using), until well coated.\n4. Arrange the seasoned sweet potato fries in a single layer on the prepared baking sheet.\n5. Bake in the preheated oven for 20-25 minutes, flipping halfway through, until the fries are crispy and golden brown.\n6. Remove the sweet potato fries from the oven and let them cool for a few minutes.\n7. Serve the sweet potato fries as a delicious and healthier alternative to regular fries.\n8. Enjoy your tasty Sweet Potato Fries!"
},
  {
  "name": "Spicy Seasoned Fries",
  "ingredients": [
    "4 large russet potatoes",
    "2 tablespoons olive oil",
    "1 teaspoon paprika",
    "1/2 teaspoon cayenne pepper",
    "1/2 teaspoon garlic powder",
    "1/2 teaspoon onion powder",
    "1/2 teaspoon salt",
    "1/4 teaspoon black pepper",
    "1/4 teaspoon chili powder",
    "1/4 teaspoon dried oregano"
  ],
  "instructions": "1. Preheat the oven to 425°F (220°C). Line a baking sheet with parchment paper.\n2. Wash and scrub the potatoes. Cut them into thin fries or wedges.\n3. In a large bowl, toss the potato slices with olive oil, paprika, cayenne pepper, garlic powder, onion powder, salt, black pepper, chili powder, and dried oregano. Make sure the potatoes are evenly coated with the spice mixture.\n4. Spread the seasoned potato slices in a single layer on the prepared baking sheet.\n5. Bake in the preheated oven for about 25-30 minutes, flipping halfway through, until the fries are crispy and golden brown.\n6. Remove from the oven and let them cool for a few minutes before serving.\n7. Enjoy the delicious and spicy seasoned fries as a snack or as a side dish with your favorite dipping sauce!"
},
  {
  "name": "Hakka-style Chili Chicken",
  "ingredients": [
    "500g boneless chicken, cut into bite-sized pieces",
    "2 tablespoons soy sauce",
    "1 tablespoon oyster sauce",
    "1 tablespoon tomato ketchup",
    "1 tablespoon chili sauce",
    "1 tablespoon cornstarch",
    "1 teaspoon sugar",
    "1/2 teaspoon black pepper",
    "1/2 teaspoon salt",
    "2 tablespoons vegetable oil",
    "3 cloves garlic, minced",
    "1 onion, thinly sliced",
    "1 bell pepper, thinly sliced",
    "2 green chilies, sliced",
    "1 teaspoon sesame oil",
    "2 spring onions, chopped (for garnish)"
  ],
  "instructions": "1. In a bowl, marinate the chicken with soy sauce, oyster sauce, tomato ketchup, chili sauce, cornstarch, sugar, black pepper, and salt. Mix well and let it sit for 20 minutes.\n2. Heat vegetable oil in a wok or skillet over high heat. Add minced garlic and sauté until fragrant.\n3. Add marinated chicken to the wok and stir-fry until it turns golden brown and cooked through.\n4. Push the chicken to one side of the wok and add sliced onion, bell pepper, and green chilies. Stir-fry for a few minutes until the vegetables are slightly tender.\n5. Mix everything together in the wok and drizzle with sesame oil. Stir-fry for another minute.\n6. Remove from heat and garnish with chopped spring onions.\n7. Serve hot with steamed rice or noodles.\n8. Enjoy the delicious Hakka-style Chili Chicken!"
},
  {
  "name": "Hakka-style Tofu and Vegetable Stir-Fry",
  "ingredients": [
    "1 block firm tofu, cut into cubes",
    "2 tablespoons vegetable oil",
    "2 cloves garlic, minced",
    "1-inch ginger, grated",
    "1 onion, sliced",
    "1 bell pepper, sliced",
    "1 carrot, julienned",
    "1 cup snap peas",
    "1 cup mushrooms, sliced",
    "2 tablespoons soy sauce",
    "1 tablespoon oyster sauce",
    "1 tablespoon hoisin sauce",
    "1 teaspoon sugar",
    "1/2 teaspoon salt",
    "1/4 teaspoon black pepper",
    "1/4 teaspoon red pepper flakes (optional)",
    "2 green onions, chopped (for garnish)"
  ],
  "instructions": "1. Heat vegetable oil in a large skillet or wok over medium heat.\n2. Add minced garlic and grated ginger to the skillet. Stir-fry for a minute until fragrant.\n3. Add sliced onion, bell pepper, carrot, snap peas, and mushrooms to the skillet. Stir-fry for 3-4 minutes until the vegetables are slightly tender.\n4. Push the vegetables to one side of the skillet and add tofu cubes to the empty space. Cook for a few minutes until the tofu is lightly browned.\n5. In a small bowl, mix together soy sauce, oyster sauce, hoisin sauce, sugar, salt, black pepper, and red pepper flakes (if using). Pour the sauce mixture over the tofu and vegetables in the skillet.\n6. Stir everything together to coat the tofu and vegetables with the sauce. Cook for another 2-3 minutes until heated through.\n7. Remove from heat and garnish with chopped green onions.\n8. Serve hot with steamed rice or noodles.\n9. Enjoy the delicious Hakka-style Tofu and Vegetable Stir-Fry!"
},
  {
  "name": "Hakka-style Chicken Manchurian",
  "ingredients": [
    "1 pound boneless chicken, cut into bite-sized pieces",
    "2 tablespoons cornstarch",
    "2 tablespoons all-purpose flour",
    "1 egg, beaten",
    "1 teaspoon ginger-garlic paste",
    "1/2 teaspoon salt",
    "1/4 teaspoon black pepper",
    "2 tablespoons vegetable oil",
    "1 onion, sliced",
    "1 bell pepper, sliced",
    "3 cloves garlic, minced",
    "1-inch ginger, grated",
    "2 tablespoons soy sauce",
    "1 tablespoon tomato ketchup",
    "1 tablespoon chili sauce",
    "1 tablespoon vinegar",
    "1 tablespoon cornstarch, dissolved in 2 tablespoons water",
    "1 cup chicken broth",
    "2 green onions, chopped (for garnish)"
  ],
  "instructions": "1. In a bowl, combine cornstarch, all-purpose flour, beaten egg, ginger-garlic paste, salt, and black pepper. Mix well to make a thick batter.\n2. Heat vegetable oil in a large skillet or wok over medium-high heat.\n3. Dip the chicken pieces in the batter, ensuring they are well coated, and add them to the hot oil. Fry until the chicken is golden brown and crispy. Remove from the skillet and set aside.\n4. In the same skillet, add sliced onion, bell pepper, minced garlic, and grated ginger. Stir-fry for 2-3 minutes until the vegetables are slightly tender.\n5. In a small bowl, mix together soy sauce, tomato ketchup, chili sauce, vinegar, and the dissolved cornstarch. Pour the sauce mixture over the vegetables in the skillet.\n6. Add chicken broth to the skillet and bring the mixture to a boil. Cook for a few minutes until the sauce thickens.\n7. Return the fried chicken pieces to the skillet and toss everything together to coat the chicken with the sauce.\n8. Cook for another 2-3 minutes until the chicken is heated through.\n9. Remove from heat and garnish with chopped green onions.\n10. Serve hot with steamed rice or noodles.\n11. Enjoy the delicious Hakka-style Chicken Manchurian!"
},
  {
  "name": "Cantonese Roast Pork",
  "ingredients": [
    "1 pound pork belly",
    "2 tablespoons soy sauce",
    "1 tablespoon hoisin sauce",
    "1 tablespoon oyster sauce",
    "1 tablespoon honey",
    "1 tablespoon Shaoxing wine",
    "1 teaspoon five-spice powder",
    "1/2 teaspoon salt",
    "1/4 teaspoon white pepper",
    "1/4 teaspoon garlic powder"
  ],
  "instructions": "1. Preheat the oven to 425°F (220°C).\n2. Score the skin of the pork belly with a sharp knife, making crosshatch cuts about 1/2 inch apart.\n3. In a bowl, mix together soy sauce, hoisin sauce, oyster sauce, honey, Shaoxing wine, five-spice powder, salt, white pepper, and garlic powder to make the marinade.\n4. Place the pork belly in a large ziplock bag and pour the marinade over it. Seal the bag and massage the marinade into the meat, making sure it is evenly coated. Let it marinate in the refrigerator for at least 2 hours, or overnight for best results.\n5. Place the marinated pork belly on a baking rack set over a baking sheet, with the skin side up. Make sure the skin is dry before roasting.\n6. Roast in the preheated oven for about 45-50 minutes, or until the skin is crispy and browned, and the internal temperature reaches 145°F (63°C).\n7. Remove from the oven and let it rest for a few minutes before slicing.\n8. Slice the Cantonese roast pork into thin pieces and serve it as a main dish or as a filling for buns, noodles, or rice.\n9. Enjoy your delicious Cantonese Roast Pork!"
},
  {
  "name": "Steamed Sea Bass with Ginger and Soy Sauce",
  "ingredients": [
    "1 whole sea bass (about 2 pounds), cleaned and scaled",
    "1 thumb-sized piece of ginger, julienned",
    "3 green onions, sliced into thin strips",
    "2 tablespoons soy sauce",
    "1 tablespoon oyster sauce",
    "1 tablespoon Shaoxing wine",
    "1 tablespoon sesame oil",
    "1/2 teaspoon sugar",
    "1/4 teaspoon white pepper"
  ],
  "instructions": "1. Rinse the sea bass inside and out with cold water. Pat dry with paper towels.\n2. Make a few diagonal cuts on each side of the fish, about 1 inch apart.\n3. Place the fish on a heatproof plate or steaming dish that fits inside a steamer.\n4. Sprinkle the ginger and green onions over the fish, ensuring they go into the cuts as well.\n5. In a small bowl, mix together soy sauce, oyster sauce, Shaoxing wine, sesame oil, sugar, and white pepper to make the sauce.\n6. Pour the sauce evenly over the fish.\n7. Prepare a steamer and bring the water to a boil. Carefully place the plate with the fish into the steamer.\n8. Steam the fish over high heat for about 12-15 minutes, or until the flesh is opaque and flakes easily with a fork.\n9. Carefully remove the plate from the steamer and garnish with additional green onions if desired.\n10. Serve the Steamed Sea Bass with Ginger and Soy Sauce hot with steamed rice.\n11. Enjoy your delicious Cantonese-style steamed fish!"
},
  {
  "name": "Crispy Roast Pork Belly",
  "ingredients": [
    "2 pounds pork belly, skin-on",
    "2 tablespoons salt",
    "1 tablespoon five-spice powder",
    "1 tablespoon white vinegar",
    "1 tablespoon honey",
    "1 tablespoon soy sauce",
    "1 teaspoon sesame oil"
  ],
  "instructions": "1. Preheat the oven to 375°F (190°C).\n2. Score the pork belly skin with a sharp knife, making shallow cuts about 1 inch apart.\n3. Rub the pork belly with salt and five-spice powder, making sure to coat the meat and skin evenly.\n4. Place the pork belly on a wire rack set inside a baking tray, with the skin side up.\n5. Roast the pork belly in the preheated oven for about 1 hour, or until the skin is crispy and golden brown.\n6. In a small bowl, mix together white vinegar, honey, soy sauce, and sesame oil to make the glaze.\n7. Remove the pork belly from the oven and brush the glaze over the skin.\n8. Increase the oven temperature to 425°F (220°C) and return the pork belly to the oven for another 10-15 minutes to further crisp up the skin.\n9. Remove the pork belly from the oven and let it rest for a few minutes before slicing.\n10. Slice the Crispy Roast Pork Belly into thin pieces and serve it hot.\n11. Enjoy the delicious and flavorful Cantonese-style Crispy Roast Pork Belly!"
},
  {
  "name": "Steamed Fish with Ginger and Scallions",
  "ingredients": [
    "1 whole fish (such as sea bass or snapper), cleaned and scaled",
    "2 tablespoons soy sauce",
    "2 tablespoons oyster sauce",
    "2 tablespoons Shaoxing wine or dry sherry",
    "1 tablespoon ginger, julienned",
    "2 stalks scallions, sliced",
    "1 tablespoon vegetable oil",
    "1 teaspoon sesame oil",
    "Salt to taste"
  ],
  "instructions": "1. Rinse the fish under cold water and pat it dry with paper towels.\n2. Season the fish with salt, both inside and outside.\n3. Place the fish on a heatproof dish or a steamer basket.\n4. In a small bowl, mix together soy sauce, oyster sauce, Shaoxing wine, ginger, scallions, vegetable oil, and sesame oil.\n5. Pour the sauce mixture over the fish, making sure to coat it evenly.\n6. Prepare a steamer by filling a wok or a large pot with water and bringing it to a boil.\n7. Place the dish with the fish in the steamer and cover it with a lid.\n8. Steam the fish over high heat for about 10-15 minutes, or until the flesh is opaque and easily flakes with a fork.\n9. Carefully remove the dish from the steamer and garnish with additional sliced scallions, if desired.\n10. Serve the Steamed Fish with Ginger and Scallions hot, along with steamed rice.\n11. Enjoy this delicious and healthy Cantonese-style dish!"
},
  {
  "name": "Tomato Rice",
  "ingredients": [
    "2 cups basmati rice",
    "4 cups water",
    "2 tablespoons vegetable oil",
    "1 onion, finely chopped",
    "2 cloves garlic, minced",
    "1 thumb-sized ginger, grated",
    "2 tomatoes, chopped",
    "1 teaspoon turmeric powder",
    "1 teaspoon cumin powder",
    "1 teaspoon coriander powder",
    "1/2 teaspoon chili powder",
    "Salt to taste",
    "Fresh cilantro leaves for garnish"
  ],
  "instructions": "1. Rinse the basmati rice under cold water until the water runs clear. Drain and set aside.\n2. In a large pot, heat the vegetable oil over medium heat.\n3. Add the chopped onion and sauté until translucent.\n4. Add the minced garlic and grated ginger. Sauté for an additional minute.\n5. Add the chopped tomatoes and cook until they soften and release their juices.\n6. Stir in the turmeric powder, cumin powder, coriander powder, and chili powder. Mix well to coat the ingredients.\n7. Add the drained basmati rice to the pot and stir to combine with the tomato mixture.\n8. Pour in the water and season with salt to taste. Stir once more.\n9. Bring the mixture to a boil, then reduce the heat to low and cover the pot with a tight-fitting lid.\n10. Cook for about 15-20 minutes, or until the rice is tender and the liquid is absorbed.\n11. Remove from heat and let the rice rest for 5 minutes.\n12. Fluff the rice with a fork and garnish with fresh cilantro leaves before serving."
},
  {
  "name": "Ayam Percik",
  "ingredients": [
    "1 whole chicken, cut into pieces",
    "1 cup coconut milk",
    "3 tablespoons tamarind juice",
    "2 tablespoons palm sugar",
    "1 tablespoon chili paste",
    "2 cloves garlic, minced",
    "1 thumb-sized ginger, grated",
    "1 teaspoon turmeric powder",
    "1 teaspoon coriander powder",
    "1 teaspoon cumin powder",
    "Salt to taste",
    "Lime wedges for serving",
    "Fresh cilantro leaves for garnish"
  ],
  "instructions": "1. In a bowl, combine the coconut milk, tamarind juice, palm sugar, chili paste, minced garlic, grated ginger, turmeric powder, coriander powder, cumin powder, and salt. Mix well to make the marinade.\n2. Place the chicken pieces in a large bowl and pour the marinade over them. Make sure the chicken is coated evenly. Marinate for at least 2 hours, or preferably overnight in the refrigerator.\n3. Preheat the grill to medium-high heat.\n4. Remove the chicken from the marinade, reserving the marinade for basting.\n5. Grill the chicken on each side for about 8-10 minutes, basting with the reserved marinade occasionally, until the chicken is cooked through and nicely charred.\n6. Remove from the grill and let the chicken rest for a few minutes.\n7. Serve the Ayam Percik hot with lime wedges on the side and garnish with fresh cilantro leaves."
},
  {
  "name": "Bibimbap",
  "ingredients": [
    "2 cups cooked short-grain rice",
    "1 carrot, julienned",
    "1 zucchini, julienned",
    "1 cup bean sprouts",
    "1 cup spinach",
    "4 shiitake mushrooms, sliced",
    "1/2 pound beef, thinly sliced",
    "4 eggs",
    "2 tablespoons soy sauce",
    "1 tablespoon sesame oil",
    "1 tablespoon vegetable oil",
    "Salt to taste",
    "Gochujang (Korean chili paste) for serving",
    "Sesame seeds for garnish",
    "Sliced green onions for garnish"
  ],
  "instructions": "1. Cook the short-grain rice according to package instructions and set aside.\n2. In separate bowls, blanch the bean sprouts and spinach in boiling water until tender. Drain and rinse with cold water. Squeeze out excess water from the spinach and season with a pinch of salt and a drizzle of sesame oil. Set aside.\n3. Heat vegetable oil in a pan over medium heat. Add the carrots and zucchini and stir-fry for a few minutes until tender. Season with a pinch of salt. Remove from the pan and set aside.\n4. In the same pan, cook the beef until browned and cooked through. Season with soy sauce and sesame oil. Remove from the pan and set aside.\n5. In a separate pan, fry the eggs sunny-side up or to your preferred doneness.\n6. To assemble the Bibimbap, divide the cooked rice among serving bowls. Arrange the cooked vegetables and beef on top of the rice. Place a fried egg on each bowl.\n7. Serve the Bibimbap with a dollop of Gochujang, sesame seeds, and sliced green onions. Mix everything together before eating."
},
  {
  "name": "Japchae",
  "ingredients": [
    "8 ounces sweet potato glass noodles",
    "4 ounces beef (ribeye or sirloin), thinly sliced",
    "1/2 onion, thinly sliced",
    "1 carrot, julienned",
    "1/2 red bell pepper, thinly sliced",
    "2 cups spinach",
    "4 shiitake mushrooms, sliced",
    "2 cloves garlic, minced",
    "2 tablespoons soy sauce",
    "1 tablespoon sesame oil",
    "1 tablespoon vegetable oil",
    "1 tablespoon sugar",
    "Salt and pepper to taste",
    "Toasted sesame seeds for garnish",
    "Green onions for garnish"
  ],
  "instructions": "1. Cook the sweet potato glass noodles according to package instructions. Drain and rinse with cold water. Set aside.\n2. In a bowl, marinate the beef with soy sauce, sesame oil, minced garlic, sugar, salt, and pepper. Set aside for 10-15 minutes.\n3. Heat vegetable oil in a pan over medium heat. Stir-fry the marinated beef until cooked. Remove from the pan and set aside.\n4. In the same pan, stir-fry the onion, carrot, red bell pepper, and shiitake mushrooms until tender. Season with salt and pepper.\n5. Blanch the spinach in boiling water for a minute. Drain and rinse with cold water. Squeeze out excess water and season with salt and sesame oil.\n6. In a large bowl, combine the cooked glass noodles, cooked vegetables, beef, and spinach. Toss well.\n7. Garnish with toasted sesame seeds and green onions.\n8. Serve the Japchae warm or at room temperature as a side dish or main course."
},
  {
  "name": "Kimchi Jjigae",
  "ingredients": [
    "1 cup kimchi, chopped",
    "8 ounces pork belly or shoulder, thinly sliced",
    "1/2 onion, thinly sliced",
    "2 cloves garlic, minced",
    "1 tablespoon gochujang (Korean red pepper paste)",
    "1 tablespoon gochugaru (Korean red pepper flakes)",
    "1 tablespoon soy sauce",
    "1 teaspoon sesame oil",
    "1 teaspoon sugar",
    "2 cups vegetable or beef broth",
    "1/2 cup tofu, diced",
    "2 green onions, chopped",
    "1 tablespoon vegetable oil",
    "Salt and pepper to taste"
  ],
  "instructions": "1. Heat vegetable oil in a pot over medium heat. Add the pork and cook until browned.\n2. Add the sliced onion and minced garlic. Sauté until the onion is translucent.\n3. Add the chopped kimchi, gochujang, gochugaru, soy sauce, sesame oil, and sugar. Stir well to combine.\n4. Pour in the vegetable or beef broth. Bring to a boil, then reduce the heat and simmer for about 15 minutes.\n5. Add the diced tofu and green onions. Simmer for an additional 5 minutes.\n6. Season with salt and pepper to taste.\n7. Serve the Kimchi Jjigae hot with a bowl of steamed rice.\n8. Enjoy the spicy and comforting flavors of Kimchi Jjigae!"
},
  {
  "name": "Doenjang Jjigae",
  "ingredients": [
    "1 tablespoon vegetable oil",
    "1 onion, sliced",
    "2 cloves garlic, minced",
    "1 zucchini, sliced",
    "1 potato, peeled and cubed",
    "1 cup tofu, cubed",
    "2 tablespoons doenjang (Korean soybean paste)",
    "4 cups water or vegetable broth",
    "1 tablespoon gochujang (Korean red pepper paste)",
    "2 green onions, chopped",
    "1 tablespoon sesame oil",
    "Salt and pepper to taste"
  ],
  "instructions": "1. Heat vegetable oil in a pot over medium heat. Add the sliced onion and minced garlic. Sauté until the onion is translucent.\n2. Add the zucchini, potato, and tofu to the pot. Stir and cook for a few minutes.\n3. In a small bowl, mix the doenjang with a bit of water to make a smooth paste. Add the doenjang paste to the pot and stir well.\n4. Pour in the water or vegetable broth. Bring to a boil, then reduce the heat and simmer for about 15-20 minutes, or until the vegetables are tender.\n5. Stir in the gochujang, green onions, and sesame oil. Cook for another 2-3 minutes.\n6. Season with salt and pepper to taste.\n7. Serve the Doenjang Jjigae hot with a bowl of steamed rice.\n8. Enjoy the rich and savory flavors of Doenjang Jjigae!"
},
  {
  "name": "Jjajangmyeon",
  "ingredients": [
    "200g pork belly, diced",
    "1 onion, finely chopped",
    "2 cloves garlic, minced",
    "2 tablespoons vegetable oil",
    "4 tablespoons black bean paste (chunjang)",
    "2 tablespoons sugar",
    "1 tablespoon oyster sauce",
    "1 cup water",
    "2 tablespoons cornstarch mixed with 4 tablespoons water",
    "4 servings of fresh or dried wheat noodles",
    "2 cucumbers, julienned",
    "4 eggs, fried sunny-side up",
    "Optional toppings: sliced green onions, shredded carrots"
  ],
  "instructions": "1. Heat vegetable oil in a large skillet or wok over medium heat.\n2. Add diced pork belly and stir-fry until browned.\n3. Add chopped onions and minced garlic. Continue stir-frying until onions become translucent.\n4. Add black bean paste (chunjang) and stir-fry for a few minutes to release its aroma.\n5. Stir in sugar and oyster sauce.\n6. Pour in water and bring the mixture to a boil. Reduce heat and let it simmer for 10 minutes.\n7. Gradually add the cornstarch mixture, stirring constantly, until the sauce thickens to your desired consistency.\n8. Cook the noodles according to the package instructions and drain.\n9. Serve the cooked noodles in bowls and top with the black bean sauce.\n10. Garnish with julienned cucumbers, fried eggs, and any optional toppings.\n11. Mix everything together before eating and enjoy your delicious Jjajangmyeon!"
},
  {
  "name": "Jjamppong",
  "ingredients": [
    "200g mixed seafood (shrimp, squid, mussels)",
    "100g pork belly, thinly sliced",
    "2 tablespoons vegetable oil",
    "1 onion, thinly sliced",
    "2 cloves garlic, minced",
    "1 teaspoon grated ginger",
    "2 tablespoons gochugaru (Korean red pepper flakes)",
    "4 cups chicken or seafood broth",
    "2 tablespoons soy sauce",
    "1 tablespoon oyster sauce",
    "1 tablespoon gochujang (Korean red pepper paste)",
    "1 teaspoon sesame oil",
    "2 green onions, sliced",
    "200g fresh or dried noodles",
    "Salt and pepper to taste"
  ],
  "instructions": "1. Heat vegetable oil in a large pot or wok over medium heat.\n2. Add pork belly slices and cook until lightly browned.\n3. Add sliced onions, minced garlic, and grated ginger. Stir-fry until onions become translucent.\n4. Stir in gochugaru and cook for a minute to release its flavor and spice.\n5. Add mixed seafood and continue stir-frying for a few minutes.\n6. Pour in chicken or seafood broth, soy sauce, oyster sauce, and gochujang. Bring the soup to a boil.\n7. Reduce heat and let it simmer for 10-15 minutes to allow the flavors to meld together.\n8. Meanwhile, cook the noodles according to the package instructions and drain.\n9. Add cooked noodles to the pot and stir gently to combine.\n10. Season with salt, pepper, and sesame oil to taste.\n11. Garnish with sliced green onions.\n12. Serve hot and enjoy your spicy and flavorful Jjamppong!"
},
  {
  "name": "Pajeon (Korean Pancake)",
  "ingredients": [
    "1 cup all-purpose flour",
    "1 cup water",
    "2 eggs",
    "1/2 teaspoon salt",
    "1/4 teaspoon black pepper",
    "1 cup chopped scallions (green onions)",
    "1/2 cup chopped kimchi (optional)",
    "2 tablespoons vegetable oil"
  ],
  "instructions": "1. In a mixing bowl, whisk together flour, water, eggs, salt, and black pepper until well combined.\n2. Add chopped scallions and kimchi (if using) to the batter and mix well.\n3. Heat vegetable oil in a non-stick skillet or frying pan over medium heat.\n4. Pour the batter onto the pan, spreading it evenly to form a round pancake.\n5. Cook for about 3-4 minutes, or until the bottom is golden brown and crispy.\n6. Flip the pancake and cook for an additional 3-4 minutes on the other side.\n7. Once cooked, transfer the pancake to a serving plate.\n8. Cut into slices and serve hot with a dipping sauce of your choice.\n9. Enjoy your delicious Pajeon, a Korean pancake perfect as an appetizer or snack!"
},
  {
  "name": "Haemul Pajeon (Korean Seafood Pancake)",
  "ingredients": [
    "1 cup all-purpose flour",
    "1 cup water",
    "2 eggs",
    "1/2 teaspoon salt",
    "1/4 teaspoon black pepper",
    "1 cup mixed seafood (such as shrimp, squid, and mussels), chopped",
    "1/2 cup chopped scallions (green onions)",
    "2 tablespoons vegetable oil"
  ],
  "instructions": "1. In a mixing bowl, whisk together flour, water, eggs, salt, and black pepper until well combined.\n2. Add chopped mixed seafood and scallions to the batter and mix well.\n3. Heat vegetable oil in a non-stick skillet or frying pan over medium heat.\n4. Pour the batter onto the pan, spreading it evenly to form a round pancake.\n5. Cook for about 3-4 minutes, or until the bottom is golden brown and crispy.\n6. Flip the pancake and cook for an additional 3-4 minutes on the other side.\n7. Once cooked, transfer the pancake to a serving plate.\n8. Cut into slices and serve hot with a dipping sauce of your choice.\n9. Enjoy your delicious Haemul Pajeon, a Korean pancake with a savory seafood twist!"
},
  {
  "name": "Kimchi Jeon (Kimchi Pancake)",
  "ingredients": [
    "1 cup all-purpose flour",
    "1 cup water",
    "1/2 cup kimchi, chopped",
    "1/4 cup kimchi juice",
    "2 green onions, chopped",
    "2 tablespoons vegetable oil",
    "1/2 teaspoon salt",
    "1/4 teaspoon black pepper"
  ],
  "instructions": "1. In a mixing bowl, combine all-purpose flour and water, and whisk until smooth.\n2. Add chopped kimchi, kimchi juice, green onions, salt, and black pepper to the batter. Mix well.\n3. Heat vegetable oil in a non-stick skillet or frying pan over medium heat.\n4. Pour the batter onto the pan, spreading it evenly to form a round pancake.\n5. Cook for about 3-4 minutes, or until the bottom is golden brown and crispy.\n6. Flip the pancake and cook for an additional 3-4 minutes on the other side.\n7. Once cooked, transfer the pancake to a serving plate.\n8. Cut into slices and serve hot with a dipping sauce of your choice.\n9. Enjoy your flavorful Kimchi Jeon, a Korean pancake with a tangy and spicy kimchi twist!"
},
  {
  "name": "California Roll",
  "ingredients": [
    "1 cup sushi rice",
    "2 sheets of nori (seaweed)",
    "1/2 avocado, sliced",
    "1/2 cucumber, julienned",
    "4 imitation crab sticks, sliced",
    "Sesame seeds for garnish",
    "Soy sauce, wasabi, and pickled ginger for serving"
  ],
  "instructions": "1. Rinse the sushi rice under cold water until the water runs clear. Cook the rice according to package instructions.\n2. Place a sheet of nori on a bamboo sushi mat or a sheet of plastic wrap.\n3. Wet your hands with water and evenly spread half of the sushi rice on the nori, leaving a small border at the top.\n4. Sprinkle sesame seeds over the rice.\n5. Flip the nori sheet over so that the rice is facing down.\n6. Place avocado, cucumber, and crab sticks in a line across the nori sheet, about one-third of the way up.\n7. Using the sushi mat or plastic wrap, tightly roll the nori sheet, applying gentle pressure to keep the ingredients in place.\n8. Repeat the process with the second sheet of nori and the remaining ingredients.\n9. Use a sharp knife to slice each sushi roll into bite-sized pieces.\n10. Serve the California rolls with soy sauce, wasabi, and pickled ginger.\n11. Enjoy your homemade California Roll sushi!"
},
  {
  "name": "Spicy Tuna Roll",
  "ingredients": [
    "4 sheets of nori (seaweed)",
    "2 cups sushi rice",
    "8 ounces fresh tuna, diced",
    "2 tablespoons mayonnaise",
    "1 tablespoon sriracha sauce",
    "1/2 teaspoon sesame oil",
    "1/4 teaspoon salt",
    "1/4 teaspoon black pepper",
    "1/2 cucumber, thinly sliced",
    "Soy sauce and wasabi for serving"
  ],
  "instructions": "1. In a bowl, combine the diced tuna, mayonnaise, sriracha sauce, sesame oil, salt, and black pepper. Mix well to coat the tuna with the spicy mayo sauce.\n2. Place a sheet of nori on a bamboo sushi mat or a clean kitchen towel.\n3. Wet your hands with water and take a handful of sushi rice. Spread the rice evenly on the nori, leaving about 1 inch of the nori uncovered at the top.\n4. Place a line of sliced cucumber and a line of the spicy tuna mixture in the center of the rice.\n5. Start rolling the sushi tightly using the bamboo mat or towel, applying gentle pressure to keep the roll firm.\n6. Repeat the process with the remaining nori, rice, cucumber, and tuna mixture.\n7. Once all the rolls are made, use a sharp knife to slice each roll into bite-sized pieces.\n8. Serve the Spicy Tuna Rolls with soy sauce and wasabi on the side.\n9. Enjoy your homemade Spicy Tuna Rolls!"
},
  {
  "name": "Tempura Shrimp Roll",
  "ingredients": [
    "4 sheets of nori (seaweed)",
    "2 cups sushi rice",
    "8 large shrimp, peeled and deveined",
    "1 cup tempura batter mix",
    "1 cup ice-cold water",
    "Vegetable oil for frying",
    "1/2 avocado, thinly sliced",
    "1/2 cucumber, thinly sliced",
    "Soy sauce and wasabi for serving"
  ],
  "instructions": "1. Prepare the tempura batter by combining the tempura batter mix and ice-cold water in a bowl. Stir until the batter is smooth.\n2. Heat vegetable oil in a deep pan or fryer to 350°F (175°C).\n3. Dip each shrimp into the tempura batter, making sure to coat it completely, and carefully place it into the hot oil. Fry until the shrimp turns golden brown and crispy. Remove and drain on a paper towel.\n4. Place a sheet of nori on a bamboo sushi mat or a clean kitchen towel.\n5. Wet your hands with water and take a handful of sushi rice. Spread the rice evenly on the nori, leaving about 1 inch of the nori uncovered at the top.\n6. Place a line of sliced avocado, cucumber, and tempura shrimp in the center of the rice.\n7. Start rolling the sushi tightly using the bamboo mat or towel, applying gentle pressure to keep the roll firm.\n8. Repeat the process with the remaining nori, rice, avocado, cucumber, and tempura shrimp.\n9. Once all the rolls are made, use a sharp knife to slice each roll into bite-sized pieces.\n10. Serve the Tempura Shrimp Rolls with soy sauce and wasabi on the side.\n11. Enjoy your delicious Tempura Shrimp Rolls!"
},
  
































  




  



    # Add more dishes here
    # ...
    # Up to a total of 50 dishes
]
# Main program
allergies, likes, dislikes = get_user_preferences()
suggest_dish(allergies, likes, dislikes)
