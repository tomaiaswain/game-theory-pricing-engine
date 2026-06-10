# =====================================================================
# PROJECT 5: GAME THEORY NASH EQUILIBRIUM SOLVER
# =====================================================================

# PHASE 1: DEFINE THE OLIGOPOLY PAYOFF MATRIX
# Format: { (Player A Strategy, Player B Strategy): (Player A Profit, Player B Profit) }
# Profits are represented in millions of dollars ($M)
payoff_matrix = {
    ("Maintain Price", "Maintain Price"): (10, 10),
    ("Drop Price", "Maintain Price"): (15, 2),
    ("Maintain Price", "Drop Price"): (2, 15),
    ("Drop Price", "Drop Price"): (5, 5)
}

strategies_A = ["Maintain Price", "Drop Price"]
strategies_B = ["Maintain Price", "Drop Price"]

def find_nash_equilibrium(matrix, strats_A, strats_B):
    print("⚙️  [ENGINE] Analyzing Oligopoly Payoff Matrix...")
    equilibriums = []
    
    # PHASE 2: ALGORITHMIC GAME THEORY RESOLUTION
    # We iterate through every possible scenario to see if either company 
    # has a mathematical incentive to betray the other.
    for strat_A in strats_A:
        for strat_B in strats_B:
            current_payoff_A, current_payoff_B = matrix[(strat_A, strat_B)]
            
            # 1. Check if Company A has an incentive to change their strategy
            A_will_deviate = False
            for alt_A in strats_A:
                if matrix[(alt_A, strat_B)][0] > current_payoff_A:
                    A_will_deviate = True
                    
            # 2. Check if Company B has an incentive to change their strategy
            B_will_deviate = False
            for alt_B in strats_B:
                if matrix[(strat_A, alt_B)][1] > current_payoff_B:
                    B_will_deviate = True
                    
            # 3. If NEITHER company wants to change, it's a Nash Equilibrium!
            if not A_will_deviate and not B_will_deviate:
                equilibriums.append((strat_A, strat_B))
                
    return equilibriums

# PHASE 3: EXECUTIVE DASHBOARD OUTPUT
def generate_strategy_report(matrix, equilibriums):
    print("\n=========================================================")
    print("    STRATEGIC ECONOMICS: DUOPOLY PRICING WAR MODEL       ")
    print("=========================================================")
    print("📊 MARKET SCENARIO (PAYOFFS IN MILLIONS):")
    for scenarios, payoffs in matrix.items():
        print(f"   [{scenarios[0]} vs {scenarios[1]}] -> A: ${payoffs[0]}M | B: ${payoffs[1]}M")
    print("---------------------------------------------------------")
    print("🎯 NASH EQUILIBRIUM(S) DETECTED:")
    if not equilibriums:
        print("   No pure strategy Nash Equilibrium found.")
    else:
        for eq in equilibriums:
            profit_A, profit_B = matrix[eq]
            print(f"   => Company A Strategy: {eq[0]}")
            print(f"   => Company B Strategy: {eq[1]}")
            print(f"   Expected Market Outcome: A makes ${profit_A}M, B makes ${profit_B}M")
    print("=========================================================\n")

# Execute the pipeline
found_equilibriums = find_nash_equilibrium(payoff_matrix, strategies_A, strategies_B)
generate_strategy_report(payoff_matrix, found_equilibriums)
