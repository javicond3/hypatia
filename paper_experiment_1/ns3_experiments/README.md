# ns-3 experiments

Given that you have generated the constellation dynamic state data over time in 
`satgenpy`, here you can run the ns-3 experiments used in the paper.

## A to B experiments

**Explanation**

There is communication for three directed pairs presented in the paper. 
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
Madrid             0     1156 + 0 = 1156   1584 + 0 = 1584    351 + 0 = 351
Barcelona          1     1156 + 1 = 1157   1584 + 1 = 1585    351 + 1 = 352
Riyadh             2     1156 + 2 = 1158   1584 + 2 = 1586    351 + 2 = 353
Los-Angeles        3     1156 + 3 = 1159   1584 + 3 = 1587    351 + 3 = 354
New-York           4     1156 + 4 = 1160   1584 + 4 = 1588    351 + 4 = 355
Mexico-City        5     1156 + 5 = 1161   1584 + 5 = 1589    351 + 5 = 356
Bogota       6     1156 + 6 = 1162   1584 + 6 = 1590    351 + 6 = 357
Cairo            7     1156 + 7 = 1163   1584 + 7 = 1591    351 + 7 = 358
Tokyo            8     1156 + 8 = 1164   1584 + 8 = 1592    351 + 8 = 359
Sidney             9     1156 + 9 = 1165   1584 + 9 = 1593    351 + 9 = 360
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