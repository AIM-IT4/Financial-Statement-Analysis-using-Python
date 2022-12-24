def dcf_valuation(cash_flows, discount_rate, perpetual_growth_rate):
    # Calculate the present value of each cash flow
    present_values = []
    for i in range(len(cash_flows)):
        present_value = cash_flows[i] / (1 + discount_rate)**(i+1)
        present_values.append(present_value)

    # Calculate the terminal value
    terminal_value = (cash_flows[-1] * (1 + perpetual_growth_rate)) / (discount_rate - perpetual_growth_rate)

    # Sum the present values and the terminal value to get the intrinsic value
    intrinsic_value = sum(present_values) + terminal_value

    return intrinsic_value

# Example usage
cash_flows = [100, 110, 120, 130]
discount_rate = 0.1
perpetual_growth_rate = 0.05
intrinsic_value = dcf_valuation(cash_flows, discount_rate, perpetual_growth_rate)
print(intrinsic_value)
