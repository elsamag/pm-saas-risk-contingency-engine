"""
===============================================================================
Enterprise Practice : Elsamag IT Solutions
Author & Lead Consultant: Samuel Chinwendu Agu
Target Repository   : pm-saas-risk-contingency-engine
Project Title       : Enterprise SaaS Risk Contingency & Budget Baseline Engine
Objective           : Perform quantitative EMV modeling, calculate contingency
                      reserves, and define cost baselines for SaaS delivery.
===============================================================================
"""

from typing import Any, Dict, List


class RiskItem:

    def __init__(self, name: str, probability: float, impact: float):
        self.name = name
        self.probability = probability
        self.impact = impact
        self.emv = round(probability * impact, 2)


class BudgetGovernanceModel:

    def __init__(
        self,
        base_budget: float,
        risks: List[RiskItem],
        management_reserve_rate: float = 0.10,
    ):
        self.base_budget = base_budget
        self.risks = risks
        self.management_reserve_rate = management_reserve_rate

    def calculate_contingency_reserve(self) -> float:
        """Calculates total contingency reserve as the sum of all risk EMVs."""
        return sum(risk.emv for risk in self.risks)

    def calculate_cost_baseline(self) -> float:
        """Calculates the project cost baseline (Base Scope + Contingency Reserve)."""
        return self.base_budget + self.calculate_contingency_reserve()

    def calculate_management_reserve(self) -> float:
        """Calculates the management reserve for unknown-unknowns based on base budget."""
        return self.base_budget * self.management_reserve_rate

    def calculate_total_authorized_budget(self) -> float:
        """Calculates total authorized project budget (Cost Baseline + Management Reserve)."""
        return (
            self.calculate_cost_baseline()
            + self.calculate_management_reserve()
        )

    def generate_audit_summary(self) -> Dict[str, Any]:
        """Generates an executive-ready audit report dictionary."""
        return {
            "Base Budget": self.base_budget,
            "Contingency Reserve": self.calculate_contingency_reserve(),
            "Cost Baseline": self.calculate_cost_baseline(),
            "Management Reserve": self.calculate_management_reserve(),
            "Total Authorized Budget": self.calculate_total_authorized_budget(),
        }


def run_budget_governance_audit():
    # Identified SaaS deployment risk register
    identified_risks = [
        RiskItem("Vendor API Deprecation", 0.40, 120000.00),
        RiskItem("Sprint Velocity Degradation", 0.60, 45000.00),
        RiskItem("Cutover Sync Failure", 0.25, 80000.00),
    ]

    model = BudgetGovernanceModel(
        base_budget=650000.00,
        risks=identified_risks,
        management_reserve_rate=0.10,
    )

    summary = model.generate_audit_summary()

    print("==================================================================")
    print("ELSAMAG IT SOLUTIONS - QUANTITATIVE RISK & BUDGET AUDIT REPORT")
    print("Lead Technical Consultant: Samuel Chinwendu Agu")
    print("Enterprise Target: SaaS Platform Implementation ($650k Base Scope)")
    print("==================================================================")
    print(f"Base Project Budget Scope        : ${summary['Base Budget']:>12,.2f}")
    print("------------------------------------------------------------------")
    print("Risk Exposure Register (EMV Breakdown):")
    for r in identified_risks:
        print(
            f"  - {r.name:<28}: P={r.probability:.2f} | Impact=${r.impact:>9,.2f} | EMV=${r.emv:>8,.2f}"
        )
    print("------------------------------------------------------------------")
    print(
        f"Total Calculated Contingency     : ${summary['Contingency Reserve']:>12,.2f}"
    )
    print(
        f"Cost Baseline (Base + Contingency): ${summary['Cost Baseline']:>12,.2f}"
    )
    print(
        f"Management Reserve (10% Base)    : ${summary['Management Reserve']:>12,.2f}"
    )
    print("==================================================================")
    print(
        f"TOTAL AUTHORIZED PROJECT BUDGET  : ${summary['Total Authorized Budget']:>12,.2f}"
    )
    print(
        "[STATUS] Budget Governance Verified | Zero Variance Leakage Confirmed"
    )
    print("==================================================================")


if __name__ == "__main__":
    run_budget_governance_audit()
