# Traffic-congestion
# Clone this repository and go into the leading sumo_rl directory

# All the Python scripts are in the experiments folder 


# To run the single-intersection network with Q Learning this is the terminal command to be used
python experiments/ql_single-intersection.py -s <number> -runs <number> -gui
# For the results show we had used -s as 20000 and runs as 10
# This will store all the CSV files will be saved in outputs/single-intersection/ql

# To run the single-intersection network with DQN this is the terminal command to be used
python experiments/dqn_single-intersection.py 
# Here no arguments are required because every parameter has been set in the script, changes can be made to num_seconds and total_timesteps
# For the results we had used num_seconds = 20000 and total_timesteps = 400000
# This will store all the CSV files will be saved in outputs/single-intersection/dqn

# To run the single-intersection network with random traffic signals this is the terminal command to be used
python experiments/n_single-intersection.py -s <number> -runs <number> -gui
# For the results show we had used -s as 20000 and runs as 10
# This will store all the CSV files will be saved in outputs/single-intersection/rand


# For plotting the graph the script is inside the outputs folder

# To run the plotting for Q learning, run the following command
python outputs/ourplot.py single-intersection/ql
# This will then have all the bar-plot and the violin charts for each number of runs that the algorithm had been run for

# To run the plotting for DQN, run the following command
python outputs/ourplot.py single-intersection/dqn
# This will then have all the bar-plot and the violin charts for each number of runs that the algorithm had been run for

# To run the plotting for random, run the following command
python outputs/ourplot.py single-intersection/rand
# This will then have all the bar-plot and the violin charts for each number of runs that the algorithm had been run for
