# RentalEngine HQ - Core Operational Calculation Array Matrix
def calculate_system_metrics(gross_pay, allocation_rate, state_tax_rate):
    allocated_gross = float(gross_pay) * float(allocation_rate)
    calculated_state_withholding = allocated_gross * float(state_tax_rate)
    net_allocated_payout = allocated_gross - calculated_state_withholding
    return allocated_gross, calculated_state_withholding, net_allocated_payout
