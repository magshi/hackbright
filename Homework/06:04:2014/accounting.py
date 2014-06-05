def parse_sales_log():
    sales_log = open("customer_orders.csv")

    for line in sales_log:
        entries = line.split(',')

        customer_id = entries[0]
        customer_name = entries[1]
        melons_ordered = float(entries[2])
        customer_owes = melons_ordered * 1.00
        customer_paid = float(entries[3])
        customer_expected = float(customer_owes - customer_paid)

        if customer_owes != customer_paid:
            print "%s (#%s) ordered %d melons and has paid $%r; customer owes $%.2f. \n" %(customer_name, customer_id, melons_ordered, customer_paid, customer_expected)

def main():
    parse_sales_log()

if __name__ == "__main__":
    main()