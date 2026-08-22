"""
===============================================================================
Enterprise Practice : Elsamag IT Solutions
Author & Lead Consultant: Samuel Chinwendu Agu
Repository Target   : pm-saas-risk-contingency-engine
File Name           : src/emv_calculator.py
Technical Objective : Calculate Expected Monetary Value (EMV), Contingency
                      Reserves, Cost Baselines, and Authorized Budgets.
===============================================================================
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class RiskEvent:
    risk_id: str
    description: str
    probability: float
    impact_cost: float
    emv: float = field(init=False)

    def __post_init__(self):
        self.emv = round(self.probability * self.impact_cost, 2)


class EMVCalculator:
    """Quantitative risk exposure matrix and cost baseline governance calculator."""

    def __init__(
        self, base_budget: float, management_reserve_rate: float = 0.10
    ):
        self.base_budget: float = base_budget
        self.management_reserve_rate: float = management_reserve_rate
        self.risk_register: List[RiskEvent] = []

    def register_risk(
        self, risk_id: str, description: str, probability: float, impact_cost: float
    ) -> None:
        """Appends an identified risk event to the quantitative register."""
        if not (0.0 <= probability <= 1.0):
            raise ValueError("Probability must be between 0.0 and 1.0.")
        risk = RiskEvent(
            risk_id=risk_id,
            description=description,
            probability=probability,
            impact_cost=impact_cost,
        )
        self.risk_register.append(risk)

    def compute_contingency_reserve(self) -> float:
        """Calculates total Expected Monetary Value (EMV) for known-unknowns."""
        return sum(risk.emv for risk in self.risk_register)

    def compute_cost_baseline(self) -> float:
        """Cost Baseline = Base Budget + Total Calculated Contingency Reserve."""
        return self.base_budget + self.compute_contingency_reserve()

    def compute_management_reserve(self) -> float:
        """Management Reserve = Base Budget * Management Reserve Percentage."""
        return self.base_budget * self.management_reserve_rate

    def compute_total_authorized_budget(self) -> float:
        """Total Authorized Budget = Cost Baseline + Executive Management Reserve."""
        return (
            self.compute_cost_baseline() + self.compute_management_reserve()
        )

    def generate_governance_report(self) -> Dict[str, float]:
        """Generates the verified quantitative budget breakdown."""
        return {
            "base_budget": self.base_budget,
            "contingency_reserve": self.compute_contingency_reserve(),
            "cost_baseline": self.compute_cost_baseline(),
            "management_reserve": self.compute_management_reserve(),
            "total_authorized_budget": self.compute_total_authorized_budget(),
        }


def main():
    # Model Initialization with $650,000 Base Project Budget
    engine = EMVCalculator(base_budget=650000.00, management_reserve_rate=0.10)

    # Ingest Core Risk Register
    engine.register_risk(
        risk_id="RSK-01",
        description="Vendor API Deprecation",
        probability=0.40,
        impact_cost=120000.00,
    )
    engine.register_risk(
        risk_id="RSK-02",
        description="Sprint Velocity Degradation",
        probability=0.60,
        impact_cost=45000.00,
    )
    engine.register_risk(
        risk_id="RSK-03",
        description="Cutover Sync Failure",
        probability=0.25,
        impact_cost=80000.00,
    )

    # Output Verified Metrics
    report = engine.generate_governance_report()
    print("==================================================================")
    print("ELSAMAG IT SOLUTIONS — QUANTITATIVE RISK & EMV AUDIT")
    print(f"Base Project Budget     : ${report['base_budget']:,.2f}")
    print(f"Contingency Reserve     : ${report['contingency_reserve']:,.2f}")
    print(f"Cost Baseline           : ${report['cost_baseline']:,.2f}")
    print(f"Management Reserve (10%): ${report['management_reserve']:,.2f}")
    print("------------------------------------------------------------------")
    print(f"Total Authorized Budget : ${report['total_authorized_budget']:,.2f}")
    print("==================================================================")


if __name__ == "__main__":
    main()
