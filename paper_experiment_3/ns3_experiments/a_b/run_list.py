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

# Core values
dynamic_state_update_interval_ms = 1000                         # 1000 millisecond update interval
simulation_end_time_s = 200                                     # 200 seconds
pingmesh_interval_ns = 1 * 1000 * 1000                          # A ping every 1ms
enable_isl_utilization_tracking = True                          # Enable utilization tracking
isl_utilization_tracking_interval_ns = 1 * 1000 * 1000 * 1000   # 1 second utilization intervals

# Derivatives
dynamic_state_update_interval_ns = dynamic_state_update_interval_ms * 1000 * 1000
simulation_end_time_ns = simulation_end_time_s * 1000 * 1000 * 1000
dynamic_state = "dynamic_state_" + str(dynamic_state_update_interval_ms) + "ms_for_" + str(simulation_end_time_s) + "s"

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



def get_pings_run_list():

    run_list = []
    for p in chosen_pairs:
        run_list += [
            {
                "name": p[0] + "_" + str(p[1]) + "_to_" + str(p[2]) + "_pings",
                "satellite_network": p[3],
                "dynamic_state": dynamic_state,
                "dynamic_state_update_interval_ns": dynamic_state_update_interval_ns,
                "simulation_end_time_ns": simulation_end_time_ns,
                "data_rate_megabit_per_s": 10000.0,
                "queue_size_pkt": 100000,
                "enable_isl_utilization_tracking": enable_isl_utilization_tracking,
                "isl_utilization_tracking_interval_ns": isl_utilization_tracking_interval_ns,
                "from_id": p[1],
                "to_id": p[2],
                "pingmesh_interval_ns": pingmesh_interval_ns,
            }
        ]

    return run_list
