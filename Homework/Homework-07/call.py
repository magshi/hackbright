"""
call.py - Telemarketing script that displays the next name 
          and phone number of a Customer to call.

          This script is used to drive promotions for 
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""
import datetime

# Load the customers from the passed filename
# Return a dictionary containing the customer data
#    (key = customer_id)
def load_customers(filename):
	customers = {}
	f = open(filename)

	# First line of the file should be the header, 
	#   split that into a list
	header = f.readline().rstrip().split(',')

	# Process each line in a file, create a new
	#   dict for each customer
	for line in f:
		data = line.rstrip().split(',')
		customer = {}

		# Loop through each column, adding the data
		#   to the dictionary using the header keys
		for i in range(len(header)):
			customer[header[i]] = data[i]

		# Add the customer to our dictionary by customer id
		customers[customer['customer_id']] = customer
		# print customer

	# Close the file
	f.close()

	# customers is a dictionary
	return customers

# Load the orders from the passed filename
# Return a list of all the orders
def load_orders(filename):
	orders = []
	f = open(filename)

	# First line of the file should be the header, 
	#   split that into a list
	header = f.readline().rstrip().split(',')

	# Process each line in a file, create a new
	#   dict for each order
	for line in f:
		data = line.rstrip().split(',')

		# Create a dictionary for the order by combining
		#   the header list and the data list
		order = dict(zip(header, data))
		# print order

		# Add the order to our list of orders to return
		orders.append(order)

	# Close the file
	f.close()

	return orders

def display_customer(customer):
	print "---------------------"
	print "Next customer to call"
	print "---------------------\n"
	print "Name: ", customer.get('first', ''), customer.get('last', '')
	print "Phone: ", customer.get('telephone')
	print "\n"

def main():
	# Load data from our csv files
	customers = load_customers('customers.csv')
	orders    = load_orders('orders.csv')

	# Loop through each order
	for order in orders:
		# Is this order over 20 watermelon?
		if order.get('num_watermelons', 0) > 20:
			# Has this customer not been contacted yet?
			customer = customers.get(order.get('customer_id', 0), 0)
			# if customer['called'] == '':
			if customer.get('called', '') == '':
				# if they haven't been contacted yet, show me the next
				# customer who I should call
				display_customer(customer)
				# after they're displayed, add 'called' to customers.csv
				# then run call.py again to get the next customer
				# I want to access the key called 'called' and insert today's
				# date. But I need to edit the actual csv file, not just the info
				# I've pulled into my main function.

				# I think I have to open the file again, I can't update the local
				# dictionary. I have to manually reload the file.
				csv_file = open('customers.csv').read()
				print csv_file[0]

				# items = csv_file.split(',')
				# print items

	# 				f = open(filename)

	# # First line of the file should be the header, 
	# #   split that into a list
	# header = f.readline().rstrip().split(',')

	# # Process each line in a file, create a new
	# #   dict for each customer
	# for line in f:
	# 	data = line.rstrip().split(',')
	# 	customer = {}

	# 	# Loop through each column, adding the data
	# 	#   to the dictionary using the header keys
	# 	for i in range(len(header)):
	# 		customer[header[i]] = data[i]

	# 	# Add the customer to our dictionary by customer id
	# 	customers[customer['customer_id']] = customer

	# 			customer['called'] = datetime.datetime.now()
				break

if __name__ == '__main__':
	main()