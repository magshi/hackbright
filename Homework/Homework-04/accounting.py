def main():
    print "******************************************"
    f = open("orders_by_type.csv")

    melon_tallies = {"musk": 0, "hybrid": 0, "watermelon": 0, "winter": 0}
    for line in f:
        data = line.split(",")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count

    f.close()
    melon_prices = { "musk": 1.15, "hybrid": 1.30, "watermelon": 1.75, "winter": 4.00 }
    total_revenue = 0
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print "We sold %d %smelons at $%0.2f each for a total of $%0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)

    print "******************************************"
    f = open("orders_with_sales.csv")

    sales = [0, 0]
    for line in f:
        data = line.split(",")
        if data[1] == "0":
            sales[0] += float(data[3])
        else:
            sales[1] += float(data[3])
    print "Phone sales generated $%0.2f in revenue." % sales[1]
    print "Internet sales generated $%0.2f in revenue." % sales[0]
    if sales[1] > sales[0]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"
    print "******************************************"


if __name__ == "__main__":
    main()