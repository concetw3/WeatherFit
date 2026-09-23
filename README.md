# WeatherFit – Weather-Based Clothing Recommendation System

WeatherFit is a Python-based clothing recommendation program that generates a suitable outfit based on the current and upcoming weather conditions.

The program retrieves weather data from the Norwegian Meteorological Institute's weather API and uses information such as temperature, precipitation, and weather conditions to determine which types of clothing are appropriate. It then selects clothing items from a collection of JSON-based clothing databases, covering categories such as jackets, trousers, shoes, sweaters, shirts, hats, sunglasses, gloves, belts, and other accessories.

The outfit is generated dynamically, with different clothing items being selected randomly within the appropriate weather conditions. For example, colder temperatures can result in warmer sweaters, jackets, gloves, and shoes, while warmer or sunny conditions can lead to lighter clothing and sunglasses. Rain predictions can also cause the program to prioritize waterproof clothing and footwear.

The project also contains functionality for creating a visual representation of the generated outfit. Clothing items are associated with image files, which can be arranged into a grid to provide a visual overview of the recommended outfit.

The project demonstrates the use of:

* Python programming
* REST APIs and weather data
* JSON data processing
* Conditional logic and filtering
* Randomized item selection
* File and image handling
* The Pillow (PIL) library for image generation
* Modular functions for different clothing categories

Overall, WeatherFit combines weather data with a structured clothing database to automatically create personalized outfit suggestions based on the expected weather.
