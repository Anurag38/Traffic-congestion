import argparse
import os
import sys
from datetime import datetime
import random

if "SUMO_HOME" in os.environ:
    tools = os.path.join(os.environ["SUMO_HOME"], "tools")
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")

from sumo_rl import SumoEnvironment

if __name__ == "__main__":
    prs = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter, description="""Random Movement Single-Intersection"""
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
    out_csv = f"outputs/single-intersection/rand/b"
    
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
                # Generate random action for each agent
                action = random.randint(0, env.action_space.n - 1)
                actions[agent_id] = action
                
            s, r, done, _ = env.step(action=actions)

        env.save_csv(out_csv, run)
        env.close()
