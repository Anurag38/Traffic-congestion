# import os
# import sys

# import gymnasium as gym
# from stable_baselines3.dqn.dqn import DQN


# if "SUMO_HOME" in os.environ:
#     tools = os.path.join(os.environ["SUMO_HOME"], "tools")
#     sys.path.append(tools)
# else:
#     sys.exit("Please declare the environment variable 'SUMO_HOME'")
# import traci

# from sumo_rl import SumoEnvironment


# if __name__ == "__main__":
#     env = SumoEnvironment(
#         net_file="nets/single-intersection/single-intersection.net.xml",
#         route_file="nets/single-intersection/single-intersection.rou.xml",
#         out_csv_name="outputs/single-intersection/dqn/d",
#         single_agent=True,
#         use_gui=True,
#         num_seconds=20000,
#     )

#     model = DQN(
#         env=env,
#         policy="MlpPolicy",
#         learning_rate=0.001,
#         learning_starts=0,
#         train_freq=1,
#         target_update_interval=500,
#         exploration_initial_eps=0.05,
#         exploration_final_eps=0.01,
#         verbose=1,
#     )
#     model.learn(total_timesteps=400000)

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

# Get the path of the current script
current_path = os.path.dirname(os.path.abspath(__file__))

# Get the path to the folder containing the CSV files from command line argument
csv_folder = sys.argv[1]

# Check if the provided path is a directory
if not os.path.isdir(csv_folder):
    print("Error: The provided path is not a directory.")
    sys.exit(1)

# Get a list of CSV files in the folder
csv_files = [file for file in os.listdir(csv_folder) if file.endswith('.csv')]

# Create a list to store the data frames
dfs = []

# Process each CSV file
for csv_file in csv_files:
    # Read the CSV file
    df = pd.read_csv(os.path.join(csv_folder, csv_file))
    dfs.append(df)

# Create the violin plot
plt.figure()
plt.violinplot([df['system_total_waiting_time'] for df in dfs], showmedians=True)

# Set the x-axis tick labels
plt.xticks(range(1, len(csv_files) + 1), [os.path.splitext(file)[0] for file in csv_files], rotation=45)

# Set the labels and title
plt.xlabel('CSV File')
plt.ylabel('Total Waiting Time')
plt.title('Total Waiting Time Distribution Comparison')

# Save the violin plot
output_violinplot_path = os.path.join(csv_folder, 'violinplot.png')
plt.savefig(output_violinplot_path)

# Close the plot
plt.close()

print(f"Violin plot saved as: {output_violinplot_path}")





# import os
# import sys

# import gymnasium as gym
# from stable_baselines3.dqn.dqn import DQN

# # Check SUMO_HOME environment variable
# if "SUMO_HOME" in os.environ:
#     tools = os.path.join(os.environ["SUMO_HOME"], "tools")
#     sys.path.append(tools)
# else:
#     sys.exit("Please declare the environment variable 'SUMO_HOME'")

# import traci
# from sumo_rl import SumoEnvironment

# if __name__ == "__main__":
#     env = SumoEnvironment(
#         net_file="nets/single-intersection/single-intersection.net.xml",
#         route_file="nets/single-intersection/single-intersection.rou.xml",
#         out_csv_name="outputs/single-intersection/dqn",
#         single_agent=True,
#         use_gui=True,
#         num_seconds=20000,
#     )

#     model = DQN(
#         env=env,
#         policy="MlpPolicy",
#         learning_rate=0.001,
#         learning_starts=0,
#         train_freq=1,
#         target_update_interval=500,
#         exploration_initial_eps=0.05,
#         exploration_final_eps=0.01,
#         verbose=1,
#     )

#     num_episodes = 10

#     # Check if the environment has a num_seconds attribute or parameter
#     if hasattr(env, "num_seconds"):
#         timesteps_per_episode = env.num_seconds  # Assuming each episode has the same number of timesteps
#     else:
#         # Set a default value if the num_seconds attribute/parameter is not available
#         timesteps_per_episode = 1000  # Update with an appropriate default value

#     total_timesteps = num_episodes * timesteps_per_episode
#     model.learn(total_timesteps=total_timesteps)
