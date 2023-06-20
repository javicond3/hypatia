# The MIT License (MIT)
#
# Copyright (c) 2020 ETH Zurich
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import exputil
import time

local_shell = exputil.LocalShell()
max_num_processes = 6

dynamic_state_update_interval_ms = 1000                         # 1000 millisecond update interval
simulation_end_time_s = 200                                     # 200 seconds

# Check that no screen is running
if local_shell.count_screens() != 0:
    print("There is a screen already running. "
          "Please kill all screens before running this analysis script (killall screen).")
    exit(1)

# Re-create data directory
local_shell.remove_force_recursive("data")
local_shell.make_full_dir("data")
local_shell.make_full_dir("data/command_logs")

# Where to store all commands
commands_to_run = []

#scenarios
def generateAtoBPoints(constellation):
    paths = []
    count = 0
    if constellation == "kuiper":
        count = 1156
    elif constellation == "starlink":
        count = 1584
    elif constellation == "telesat":
        count = 351
    else:
        print("Error in constellation")
        
    for orig in range(10):
        for dest in range(orig,10):
            if (orig != dest): 
                paths.append((orig + count, dest + count))
    return paths


experiments = [ 
        {
        "name":"kuiper_630_isls_plus_grid_ground_stations_experiment_algorithm_free_one_only_over_isls",
        "constellation": "kuiper_630_isls",
        "paths": generateAtoBPoints("kuiper")
        },
        {
        "name":"starlink_550_isls_plus_grid_ground_stations_experiment_algorithm_free_one_only_over_isls",
        "constellation": "starlink_550_isls",
        "paths": generateAtoBPoints("starlink")
        },
        {
        "name":"telesat_1015_isls_plus_grid_ground_stations_experiment_algorithm_free_one_only_over_isls",
        "constellation": "telesat_1015_isls",
        "paths": generateAtoBPoints("telesat")
        }
    ]

def generateChosenPairs(experiments):
    chosen_pairs = []
    for experiment in experiments:
        for path in experiment["paths"]:
            chosen_pairs.append((experiment["constellation"], path[0], path[1], experiment["name"]))
    return chosen_pairs

# Example of chose_pairs
# [ ("telesat_1015_isls", 351, 352, "telesat_1015_isls_plus_grid_ground_stations_experiment_algorithm_free_one_only_over_isls")]
chosen_pairs = generateChosenPairs(experiments)

    
command_init = "cd ../../satgenpy; python -m satgen.post_analysis.main_print_routes_and_rtt ../paper/satgenpy_analysis/data ../paper/satellite_networks_state/gen_data/"


for chosen_pair in chosen_pairs:
    command_end = "{} {} {} {} {} > ../paper/satgenpy_analysis/data/command_logs/{}_{}_to_{}.log 2>&1".format(
        chosen_pair[3], dynamic_state_update_interval_ms, 
        simulation_end_time_s, chosen_pair[1], chosen_pair[2],
        chosen_pair[0], chosen_pair[1], chosen_pair[2],)
    commands_to_run.append(command_init + command_end)


# "cd ../../satgenpy; python -m satgen.post_analysis.main_print_routes_and_rtt "
# "../paper/satgenpy_analysis/data ../paper/satellite_networks_state/gen_data/"
# "telesat_1015_isls_plus_grid_ground_stations_experiment_algorithm_free_one_only_over_isls "
# "1000 200 351 352 "
# "> ../paper/satgenpy_analysis/data/command_logs/manual_telesat_isls_351_to_352.log 2>&1"


# Manual
print("Generating commands for selected endpoints pair (printing of routes and RTT over time)...")

# Run the commands
print("Running commands (at most %d in parallel)..." % max_num_processes)
for i in range(len(commands_to_run)):
    print("Starting command %d out of %d: %s" % (i + 1, len(commands_to_run), commands_to_run[i]))
    local_shell.detached_exec(commands_to_run[i])
    while local_shell.count_screens() >= max_num_processes:
        time.sleep(2)

# Awaiting final completion before exiting
print("Waiting completion of the last %d..." % max_num_processes)
while local_shell.count_screens() > 0:
    time.sleep(2)
print("Finished.")
