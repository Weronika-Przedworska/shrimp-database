### Shrimp Database

Welcome to my final project. I create this basic Django web application to help me manage my aquarium, which currently contains mainly *neocaridinia* shrimp. As of today, the webapp has the basic functionalities of the final project requirements, but I will likely add more for my own personal use later on. Here is an overview of the currently available features:

1. Data submission view: accessible through the home page (url ending in /add), this page allows you to add water parameter measurements such as ammonia and nitrate levels to the model.
2. Parameters view: also accessible through the home page (url ending in /measurements) I use chart.js to visualize historic water parameter data. So far I use plain barcharts for different parameters over time. There is also an option to export the data in an .xlsx file (featured as link on the same measurements page). 
3. Admin view: Allow administrator (me) to manage submissions. 
4. Models: As per the ERD below, the **measurements** model has a many-to-one relationship with the **tank** model. That is, I can collect many (time-stamped) measurements per tank. Note that I currently only own one aquarium, but this might change in the future. 
