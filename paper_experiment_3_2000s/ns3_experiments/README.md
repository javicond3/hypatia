# ns-3 experiments

Given that you have generated the constellation dynamic state data over time in 
`satgenpy`, here you can run the ns-3 experiments used in the paper_experiment_3.

## A to B experiments

**Explanation**

There is communication for three directed pairs presented in the paper_experiment_3. 
These were chosen from among the 100 ground stations used, which were an 
input in `satgenpy`:

```
satgenpy/data/ground_stations_cities_experiment.basic.txt
```

The Kuiper-610 shell has 34 x 34 = 1156 satellites. Node identifiers start 
with the satellites, as such the 100 ground stations have node identifiers 
1156 (incl.) till 1256 (excl.). This similarly applies to Starlink (22 x 72 = 1584) 
and Telesat (27 x 13 = 351). 

The following ground stations are used:

```
City name          GID           Kuiper id        Starlink id         Telesat id
TODO
```

... of which the following directed pairs are run in Telesat:

* Madrid (351) to Barcelona (352)


**Commands**

Run and analyze these pairs by executing:

```
cd a_b || exit 1
python step_1_generate_runs.py || exit 1
python step_2_run.py || exit 1
python step_3_generate_plots.py || exit 1
```