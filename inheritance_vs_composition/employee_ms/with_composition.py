"""
Very advanced Employee management system. Not very scalable.

Consider a case where we need to add yearly bonus and then calculate pay. In this case, we need to add one more level of
inheritance with each sub-class, like without bonus and with bonus. It will be huge level of hierarchy.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class Contract(ABC):

    @abstractmethod
    def compute_pay(self):
        pass


@dataclass
class Commission(ABC):

    @abstractmethod
    def get_commission(self):
        pass

@dataclass
class ContractCommission(Commission):

    commission: float = 100
    contract_landed: int = 0

    def get_commission(self):
        return self.commission * self.contract_landed




@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    # Can be refactored further, since employeee class has many responsibility like basic info and salary detail.

    name: str
    id: int
    contract: Contract
    commission: Optional[Commission] = None

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""

        payout = self.contract.compute_pay()
        if(self.commission is not None):
            payout += self.commission.get_commission()

        return payout



@dataclass
class HourlyContract(Contract):
    """Employee that's paid based on number of worked hours."""

    pay_rate: float
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost


@dataclass
class SalariedContract(Contract):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float
    percentage: float = 1

    def compute_pay(self) -> float:
        return self.monthly_salary * self.percentage


@dataclass
class FreelancerContract(Contract):
    """Freelancer that's paid based on number of worked hours."""

    pay_rate: float
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked


def main() -> None:
    """Main function."""

    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=123456, contract=henry_contract)
    print(
        f"{henry.name} worked for {henry_contract.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah_contract = SalariedContract(monthly_salary=5000)

    sarah_commission = ContractCommission(contract_landed=100)

    sarah = Employee(name="Sarah", id=47832, contract=sarah_contract, commission=sarah_commission)

    print(
        f"{sarah.name} landed {sarah_commission.contract_landed} contracts and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()
