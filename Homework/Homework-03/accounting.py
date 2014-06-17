def parse_sales_log(filename):
    sales_log = open(filename)

    delinquents = []

    for line in sales_log:
        entries = line.split(',')
        print entries
        customer_id = entries[0]
        customer_name = entries[1]
        melons_ordered = int(entries[2])
        print melons_ordered
        customer_owes = melons_ordered * 1.00
        customer_paid = float(entries[3])
        customer_expected = float(customer_owes - customer_paid)

        if customer_owes != customer_paid:
            print "%s (#%s) ordered %d melons and has paid $%r; customer owes $%.2f. \n" %(customer_name, customer_id, melons_ordered, customer_paid, customer_expected)

            delinquents.append(customer_name)

def main():
    # print "Enter log file: "
    # filename = raw_input()
    parse_sales_log("customer_orders.csv")

if __name__ == "__main__":
    main()