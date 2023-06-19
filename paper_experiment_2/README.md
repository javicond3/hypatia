# RTT experiment

## Steps to run

**Step 0: installation:**

1. System setup:
   - Python version 3.7+
   - Recent Linux operating system (e.g., Ubuntu 18+)

2. Install dependencies -> only the first time:
   ```
   bash hypatia_install_dependencies.sh
   ```
   
3. Build all four modules (as far as possible) -> only the first time:
   ```
   bash hypatia_build.sh
   ```
   
4. Run tests (to validate the scenario):
   ```
   bash hypatia_run_tests.sh
   ```

**Step 1: generating LEO satellite network dynamic state over time**

Instructions can be found in `<hypatia>/paper_experiment_2/satellite_networks_state/README.md`

**Step 2: build ns-3 simulator**

Only the first time:
Instructions can be found in `<hypatia>/ns3-sat-sim/README.md`

<!-- **Step 3: performing analysis using satgenpy**

Instructions can be found in `<hypatia>/paper_experiment_2/satgenpy_analysis/README.md` -->

**Step 4: running ns-3 experiments**

Instructions can be found in `<hypatia>/paper_experiment_2/ns3_experiments/README.md`

**Step 5: generating satviz figures**

Instructions can be found in `<hypatia>/satviz/README.md` under `Visualizations in the paper_experiment_2`.

**Step 6: plotting figures of the paper_experiment_2**

Instructions can be found in `<hypatia>/paper_experiment_2/figures/README.md`
