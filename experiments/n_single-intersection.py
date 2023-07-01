# import argparse
# import os
# import sys
# from datetime import datetime
# import random

# if "SUMO_HOME" in os.environ:
#     tools = os.path.join(os.environ["SUMO_HOME"], "tools")
#     sys.path.append(tools)
# else:
#     sys.exit("Please declare the environment variable 'SUMO_HOME'")

# from sumo_rl import SumoEnvironment

# if __name__ == "__main__":
#     prs = argparse.ArgumentParser(
#         formatter_class=argparse.ArgumentDefaultsHelpFormatter, description="""Random Movement Single-Intersection"""
#     )
#     prs.add_argument(
#         "-route",
#         dest="route",
#         type=str,
#         default="nets/single-intersection/single-intersection.rou.xml",
#         help="Route definition xml file.\n",
#     )
#     prs.add_argument("-s", dest="seconds", type=int, default=100000, required=False, help="Number of simulation seconds.\n")
#     prs.add_argument("-runs", dest="runs", type=int, default=1, help="Number of runs.\n")
#     prs.add_argument("-gui", action="store_true", default=False, help="Run with visualization on SUMO.\n")
#     args = prs.parse_args()

#     experiment_time = str(datetime.now()).split(".")[0]
#     out_csv = f"outputs/single-intersection/rand/b"
    
#     env = SumoEnvironment(
#         net_file="nets/single-intersection/single-intersection.net.xml",
#         route_file=args.route,
#         out_csv_name=out_csv,
#         num_seconds=args.seconds,
#         use_gui=args.gui,  # Enable GUI visualization
#     )

#     for run in range(1, args.runs + 1):
#         initial_states = env.reset()
#         done = {"__all__": False}
#         if args.seconds <= 0:
#             raise ValueError("Number of simulation seconds must be greater than zero.")
        
#         while not done["__all__"]:
#             actions = {}
            
#             for agent_id in initial_states:
#                 # Generate random action for each agent
#                 action = random.randint(0, env.action_space.n - 1)
#                 actions[agent_id] = action
                
#             s, r, done, _ = env.step(action=actions)

#         env.save_csv(out_csv, run)
#         env.close()



# import argparse
# import os
# import sys
# from datetime import datetime

# if "SUMO_HOME" in os.environ:
#     tools = os.path.join(os.environ["SUMO_HOME"], "tools")
#     sys.path.append(tools)
# else:
#     sys.exit("Please declare the environment variable 'SUMO_HOME'")

# from sumo_rl import SumoEnvironment

# if __name__ == "__main__":
#     prs = argparse.ArgumentParser(
#         formatter_class=argparse.ArgumentDefaultsHelpFormatter, description="""Real-life Traffic Signal Single-Intersection"""
#     )
#     prs.add_argument(
#         "-route",
#         dest="route",
#         type=str,
#         default="nets/single-intersection/single-intersection.rou.xml",
#         help="Route definition xml file.\n",
#     )
#     prs.add_argument("-s", dest="seconds", type=int, default=100000, required=False, help="Number of simulation seconds.\n")
#     prs.add_argument("-runs", dest="runs", type=int, default=1, help="Number of runs.\n")
#     prs.add_argument("-gui", action="store_true", default=False, help="Run with visualization on SUMO.\n")
#     args = prs.parse_args()

#     experiment_time = str(datetime.now()).split(".")[0]
#     out_csv = f"outputs/single-intersection/real_traffic/{experiment_time}"

#     env = SumoEnvironment(
#         net_file="nets/single-intersection/single-intersection.net.xml",
#         route_file=args.route,
#         out_csv_name=out_csv,
#         num_seconds=args.seconds,
#         use_gui=args.gui,  # Enable GUI visualization
#     )

#     for run in range(1, args.runs + 1):
#         initial_states = env.reset()
#         done = {"__all__": False}
#         if args.seconds <= 0:
#             raise ValueError("Number of simulation seconds must be greater than zero.")

#         current_time = 0  # Initialize the current time

#         while not done["__all__"]:
#             actions = {}

#             for agent_id in initial_states:
#                 # Simulate real-life traffic signal timing
#                 green_time = 30  # Duration of the green phase (30 seconds)
#                 yellow_time = 5  # Duration of the yellow phase (5 seconds)
#                 red_time = 40  # Duration of the red phase (40 seconds)

#                 cycle_time = green_time + yellow_time + red_time  # Total cycle time

#                 # Calculate the current phase based on the current time
#                 phase_time = current_time % cycle_time

#                 if phase_time < green_time:
#                     action = 0  # Green phase
#                 elif phase_time < green_time + yellow_time and phase_time < cycle_time - red_time:
#                     action = 1  # Yellow phase
#                 else:
#                     action = 2  # Red phase

#                 actions[agent_id] = action

#             s, r, done, _ = env.step(action=actions)
#             current_time += 1  # Increment the current time by 1

#         env.save_csv(out_csv, run)
#         env.close()

import argparse
import os
import sys
from datetime import datetime

if "SUMO_HOME" in os.environ:
    tools = os.path.join(os.environ["SUMO_HOME"], "tools")
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")

from sumo_rl import SumoEnvironment

if __name__ == "__main__":
    prs = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter, description="""Fixed Waiting Time Single-Intersection"""
    )
    prs.add_argument(
        "-route",
        dest="route",
        type=str,
        default="nets/single-intersection/single-intersection.rou.xml",
        help="Route definition xml file.\n",
    )
    prs.add_argument("-s", dest="seconds", type=int, default=100000, required=False, help="Number of simulation seconds.\n")
    prs.add_argument("-runs", dest="runs", type=int, default=1, help="Number of runs.\n")
    prs.add_argument("-gui", action="store_true", default=False, help="Run with visualization on SUMO.\n")
    args = prs.parse_args()

    experiment_time = str(datetime.now()).split(".")[0]
    out_csv = f"outputs/single-intersection/rand/fixed_waiting_time"
    
    env = SumoEnvironment(
        net_file="nets/single-intersection/single-intersection.net.xml",
        route_file=args.route,
        out_csv_name=out_csv,
        num_seconds=args.seconds,
        use_gui=args.gui,  # Enable GUI visualization
    )

    for run in range(1, args.runs + 1):
        initial_states = env.reset()
        done = {"__all__": False}
        if args.seconds <= 0:
            raise ValueError("Number of simulation seconds must be greater than zero.")
        
        while not done["__all__"]:
            actions = {}
            
            for agent_id in initial_states:
                
                print("-----")
                # Set the action based on the fixed waiting time for each traffic light
                if agent_id.startswith("traffic_light"):
                    print(agent_id)
                    # Assuming a fixed waiting time of 30 seconds for traffic lights
                    action = 0 if env.seconds_in_episode() % 60 < 30 else 1
                else:
                    # Generate random action for other agents (vehicles)
                    action = env.action_space.sample()
                
                actions[agent_id] = action
                
            s, r, done, _ = env.step(action=actions)

        #env.save_csv(out_csv, run)
        env.close()
