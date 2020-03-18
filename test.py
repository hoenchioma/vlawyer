import vlawyer
import json

# see documentation (press q to exit)
help(vlawyer.submissions)

# prints the latest 10 submissions from vjudge.net
# converted to json for better readability
print(json.dumps(vlawyer.get_vjudge_data(limit=10), indent=4, sort_keys=True)) 

# prints the submissions by xxx in contest no yyy
# replace xxx with actual username and yyy with an actual contest (otherwise you'll get an error)
print(json.dumps(vlawyer.get_vjudge_data(username='xxx', contest_id='yyy'), indent=4, sort_keys=True))

response = vlawyer.get_vjudge_data(limit=12)
print(len(response)) # get length of response (12)
print(type(response)) # get the type of response (dict)