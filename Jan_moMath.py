import random
from collections import defaultdict

class LadybugClockWalk:
    """
    Simulates a ladybug walking randomly on a clock face (positions 1-12).
    The ladybug starts at 12 and moves randomly to neighboring numbers.
    We track which number is the last to be visited (colored).
    """
    
    def __init__(self, num_positions=12, start_position=12):
        """
        Initialize the simulation.
        
        Args:
            num_positions: Number of positions on the clock (12)
            start_position: Starting position (12 for clock)
        """
        self.num_positions = num_positions
        self.start_position = start_position
        self.positions = list(range(1, num_positions + 1))
        
    def run_single_simulation(self, verbose=False):
        """
        Run one complete simulation until all positions are visited.
        
        Args:
            verbose: If True, print detailed output for each step
            
        Returns:
            The last position to be visited
        """
        current_pos = self.start_position
        visited = {current_pos}
        step = 0
        
        if verbose:
            print(f"\n{'='*60}")
            print(f"SIMULATION START")
            print(f"{'='*60}")
            print(f"Step {step}: Starting at position {current_pos}")
            print(f"Visited so far: {sorted(visited)}")
        
        # Continue until all 12 positions are visited
        while len(visited) < self.num_positions:
            # Choose random direction: -1 (counterclockwise) or +1 (clockwise)
            direction = random.choice([-1, 1])
            
            # Move to neighboring position (wrapping around)
            current_pos = ((current_pos - 1 + direction) % self.num_positions) + 1
            
            step += 1
            is_new = current_pos not in visited
            
            if is_new:
                visited.add(current_pos)
                
            if verbose:
                direction_name = "clockwise" if direction == 1 else "counterclockwise"
                status = "🔴 NEW!" if is_new else "(already visited)"
                print(f"Step {step}: Moved {direction_name} to position {current_pos:2d} {status}")
                if is_new:
                    print(f"          Visited: {sorted(visited)} ({len(visited)}/12)")
        
        last_visited = current_pos
        
        if verbose:
            print(f"\n{'='*60}")
            print(f"SIMULATION COMPLETE!")
            print(f"Last position to be colored: {last_visited}")
            print(f"All positions visited in {step} steps")
            print(f"{'='*60}\n")
        
        return last_visited
    
    def run_multiple_simulations(self, num_runs=10000, verbose_first_n=0):
        """
        Run multiple simulations and collect statistics.
        
        Args:
            num_runs: Number of simulations to run
            verbose_first_n: Print detailed output for first n simulations
            
        Returns:
            Dictionary with statistics
        """
        last_position_counts = defaultdict(int)
        
        print(f"\n{'='*70}")
        print(f"RUNNING {num_runs:,} SIMULATIONS")
        print(f"{'='*70}\n")
        
        for run_num in range(num_runs):
            is_verbose = (run_num < verbose_first_n)
            last_pos = self.run_single_simulation(verbose=is_verbose)
            last_position_counts[last_pos] += 1
            
            # Print progress
            if (run_num + 1) % 1000 == 0:
                print(f"Completed {run_num + 1:,} / {num_runs:,} simulations...")
        
        print(f"\n{'='*70}")
        print(f"FINAL RESULTS")
        print(f"{'='*70}\n")
        
        return last_position_counts
    
    def print_statistics(self, last_position_counts, num_runs):
        """
        Print formatted statistics from the simulation runs.
        
        Args:
            last_position_counts: Dictionary of counts for each last position
            num_runs: Total number of runs
        """
        print(f"Total simulations: {num_runs:,}\n")
        print(f"{'Position':<12} {'Count':<12} {'Probability':<15} {'Percentage':<12}")
        print(f"{'-'*51}")
        
        # Sort by position number
        for pos in sorted(last_position_counts.keys()):
            count = last_position_counts[pos]
            prob = count / num_runs
            percentage = (count / num_runs) * 100
            print(f"{pos:<12} {count:<12,} {prob:<15.6f} {percentage:<12.2f}%")
        
        print(f"\n{'='*70}\n")
        
        # Highlight the probability for position 6
        if 6 in last_position_counts:
            prob_6 = last_position_counts[6] / num_runs
            print(f"🎯 PROBABILITY THAT 6 IS LAST: {prob_6:.6f} ({prob_6*100:.2f}%)")
            print(f"   (This is approximately 1/{num_runs/last_position_counts[6]:.1f})\n")
        
        return last_position_counts[6] / num_runs if 6 in last_position_counts else 0


def main():
    """Main execution function."""
    
    # Set random seed for reproducibility (optional)
    # random.seed(42)
    
    # Create the simulation
    sim = LadybugClockWalk(num_positions=12, start_position=12)
    
    # Run a few simulations with detailed output
    print("\n" + "="*70)
    print("DETAILED EXAMPLE RUNS (WITH STEP-BY-STEP OUTPUT)")
    print("="*70)
    
    for i in range(2):
        print(f"\n--- EXAMPLE RUN {i+1} ---")
        sim.run_single_simulation(verbose=True)
    
    # Run many simulations to estimate the probability
    num_simulations = 50000
    last_position_counts = sim.run_multiple_simulations(
        num_runs=num_simulations,
        verbose_first_n=0  # Set to 0 to skip verbose output for main run
    )
    
    # Print statistics
    prob_6 = sim.print_statistics(last_position_counts, num_simulations)
    
    # Additional analysis
    print("="*70)
    print("ADDITIONAL ANALYSIS")
    print("="*70 + "\n")
    
    # Check symmetry
    print("Checking symmetry around the clock:")
    print("(Position 12 is diametrically opposite to 6)")
    print(f"  Prob(last=3):  {last_position_counts[3]/num_simulations:.6f}")
    print(f"  Prob(last=1):  {last_position_counts[1]/num_simulations:.6f}")
    print(f"  Prob(last=6):  {last_position_counts[6]/num_simulations:.6f}\n")
    
    # Theoretical analysis
    print("Note: Due to symmetry of random walk on a cycle,")
    print("positions directly opposite to start (12) tend to be last more often.")
    print(f"Position 6 is exactly opposite to start position 12.\n")


if __name__ == "__main__":
    main()
