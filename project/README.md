# Tony's Menu
#### Video Demo: https://youtu.be/hg0eP3V6lLM
#### Description:
Tony's Menu, a project of a fast food restaurent that delivers many kind of food to people
around, pleasing their hunger with its high food quality. And like other restaurents, an online program
of application is set for a better connections between persons and the restaurant.

In the scope of programmming through terminal, the code will run showing four main options
option 1 "Menu", option 2 "Adding a meal", option 3 "Canceling a meal", option 4 "Exit"

- Option 1, "Menu", there is a CSV file in which Menu is included, so while clicking option 1,
it opens the Menu as a dictionary, showing all kind of foods in the restaurant, clarifing its names,
calories and prices for each for example : {'Name': 'Chicken burger', 'Calories': '265', 'Price': '18'}
This method is new and explains more the nature of foods.

- Option 2, "Adding a meal" after clicking on this option, a question of "What do you want to add?"
is shown, so the individual enters the name of the food needed so his demand appears in a list of dictionaries
that every meal is a dictionary in this list, in another way the meals are dictionaries that while ordering
them, every meal appears as a dictionary in the list of dictionaries. This idea is programmed in the way
because it oppens a way of canceling a meal if the individual want agter that to cancel an order as will
option 3 show after, if a person enters a type of food that is not available in the reataurant, he will turn back
to the first step of choosing an option anf nothing will be added.

- Option 3, "Canceling a meal" as we said before in option 2 a person can cancel a meal. While clicking
on this option a question of "What do you want to remove? " is shown, so the person types the name of the meal
that he wants to remove from the list added before and the dictionary of this meal will be removed immediatly
and showing the new updated order. It is important while removing a meal to type the name of the dictionary added
in the list of dictionnaries before because while putting another name of dictionary, nothing will change in
the order and the person reenter the main step that shows the four options.

- Option 4, "Exit" is more like an approval to the order mainly with a small description to it.
first, while clicking on it a message will appear saying "This is your order, Thank You! " a table is shown and it
includes: name, description, cost.
    -Name:
          showing the name of food ordered
    -Description:
                 Is mainly an advice for the people it is describes in four ways
                 *First, if the food is less than 150 calories than the food can be eaten by all weights.
                 *Second, if the food is between 150 and 300 calories than the food can be eaten by people
                 under 120 Kg
                 *Third, if the food is between 300 and 400 calories than the food can be eaten by people
                 under 100 Kg
                 *Fourth, if the food is more than 400 calories than the food can be eaten by people
                 under 80 Kg
    -Cost:
          it shows the total cost of the order and gives like a small information about it.
          *If the cost is less than $15 it shows "Low cost"
          *If the cost is between $15 and $25 it shows "Well cost"
          *If the cost is more than $25 it shows "High cost"
