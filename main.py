from cash_on_hand import calculate_cash_on_hand
from overheads import calculate_overheads
from profits_loss import calculate_profit_loss

# calculate the cash on hand, overheads, profit and loss using the appropriate function
cash_output = calculate_cash_on_hand()
overheads_output = calculate_overheads()
profit_loss_output = calculate_profit_loss()

# open a file named "summary_report.txt" in write mode
with open("summary_report.txt", "w") as file:
    file.write("Cash On Hand\n==========================\n")
    file.write(cash_output)

    file.write("\nOverheads\n==========================\n")
    file.write(overheads_output)

    file.write("\nProfits and Loss\n==========================\n")
    file.write(profit_loss_output)