import twitter
import markov

message = markov.main()
print message

api_file = open("lanakeys.txt").read()
api_keys = api_file.split()
api_dict = {}

for item in api_keys:
	key_value = item.split(':')
	api_dict[key_value[0]] = key_value[1]

api = twitter.Api(consumer_key = api_dict['consumer_key'],
	consumer_secret = api_dict['consumer_secret'],
	access_token_key = api_dict['access_token_key'],
	access_token_secret = api_dict['access_token_secret'])

status = api.PostUpdate(message)