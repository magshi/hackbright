def print_sales_log(day, filename):
    print "Day %d" % day
    my_file = open(filename)
    for line in my_file:
        line = line.rstrip()
        words = line.split(',')

        melon = words[0]
        count = words[1]
        amount = words[2]

        log_text =  "Delivered %s %ss for a total of: $%s" % (count, melon, amount)
        print log_text.upper()
    my_file.close()
    print "\n",

def main():

    # Day 1
#    print "Day 1"
    my_file = "um-deliveries-20140519.csv"
    print_sales_log(1, my_file)

    output = call_my_function()

    # Day 2
    my_file = "um-deliveries-20140520.csv"
    print_sales_log(2, my_file)

    # Day 3
    my_file = "um-deliveries-20140521.csv"
    print_sales_log(3, my_file)


if __name__ == "__main__":
    main()
