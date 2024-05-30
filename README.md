# Genetic Algorithm for Solving Sudoku Puzzles

This project approaches to solve Sudoku puzzles by utilizing a custom written genetic algorithm. This is my first attempt at creating a genetic algorithm (GA). The inspiration behind this project was the video "Using AI to Create the Perfect Keyboard" by the channel adumb on [YouTube](https://www.youtube.com/watch?v=EOaPb9wrgDY&pp=ygUaZ2VuZXRpYyBhbGdvcml0aG0ga2V5Ym9hcmQ%3D). The choice of Sudoku as the optimization problem was due to the fact that I like the game, and saw online that this problem had been solved via GA [previously](https://nidragedd.github.io/sudoku-genetics/). I primarily used the [Wikipedia](https://en.wikipedia.org/wiki/Genetic_algorithm) page for GA's, and the guide on [Medium](https://medium.com/@Data_Aficionado_1083/genetic-algorithms-optimizing-success-through-evolutionary-computing-f4e7d452084f) by Rayan Ali.

## Installation

This project uses python; specifically it uses the libraries [numpy](https://numpy.org/) and [matplotlib](https://matplotlib.org/), and the python [random](https://docs.python.org/3/library/random.html) module.



 These can be installed using the [pip](https://pip.pypa.io/en/stable/) installation manager

```bash
pip install matplotlib
pip install numpy
```

## Usage

In order to start using thee Sudoku solver, we need puzzles. I used the "1 million Sudoku games" dataset by Kyubyong Park on Kaggle in this project. Since the dataset was large, it is not included in this github page. The dataset can be found [here](https://www.kaggle.com/datasets/bryanpark/sudoku) and added into a data/ folder to get a large number of Sudoku games to use. After adding this folder the predefined function in main can be called to generate a .npz file for faster access to the dataset at the cost of more space as follows:

to main.py adding:
```python
generate_sudoku_npz()

```
then running:

```bash
python main.py
```

After generating the sudoku.npz file code runs much faster, since each lookup from the file is O(1). 

Then, to use the solver one can use the functions solve_game() and solve_random_subset() with their respective arguments (explained in the comments in code) to solve puzzles. This can again be done by calling the function in main and running the main.py file. 