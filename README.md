# Pygame-GeneticAlgo
Genetic algorithm that learns how to play a Pygame mini-game

# What You Need
The Pygame module

# Neural Network
Architecture: An input layer of 4 nodes, no hidden layers, an output layer of 3 nodes, and a chromosome consisting
of 12 numbers 1-1000 that represent the weights on the connections between the layers. The output node with the highest
value is selected. Fitness is simply calculated as distance from the objective but I am meaning to update that in the
future to include distance from start and how far up it moved

Input Layer: <br />
    1 - Distance to the nearest obstruction on the left <br />
    2 - Distance to the nearest obstruction in front <br />
    3 - Distance to the nearest obstruction on the right <br />
    4 - Distance to the objective (Red square) <br />
   
Output Layer: <br />
    1 - Move left<br />
    2 - Move forward<br />
    3 - Move right<br />