We are going to implement **Dijkstra** and **A*** algorithms with Python 3. This template is provided to you as a starting point. After you finish coding, you would be able to create your own map to test different algorithms, and visualize the path found by them.

Files included:

- **search.py** is the file where the algorithms are implemented.
- **main.py** is the script that provides helper functions that load the map from csv files and visualize the map and path.
- **map.csv** is the map file you could modify to create your own map.
- **test_map.csv** restores a test map for doc test purpose only. Do not modify this file.


  After implementation, you could run the doc test by:

  `python search.py`

  If you see nothing, it means you pass the simple doc test.

  ---

    Run your code with `python main.py`. You could use the map **map.csv** I provided, but you could also create your own map. Run the test and see the paths you found and the steps/time it takes for these algorithms to find them. 
**REMEMBER:** code follows this order **"right, down, left, up"** to explore the nearby nodes in the map, which means "[0, +1], [+1, 0], [0, -1], [-1, 0]" in coordinates.

## Get Started

Before starting any coding, please run the code first:

`python search.py`

When running **search.py** as a main function, it will run a doc test for all the algorithms. It loads **test_map.csv** as the map for testing.

---

For visualization, please run:

`python main.py`

There should be 2 maps shown representing the results of the 2 algorithms. The **main.py** loads the map file **map.csv**, which you are free to modify to create your own map.
