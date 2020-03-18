# vlawyer

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

An unofficial [vjudge](https://vjudge.net/) statistics API

You can use this package to get:
- submissions data
- contest standings *(comming soon)*

**Disclaimer:** All rights to the site and its data are reserved by the site owner. This is merely a tool to obtain the already acquirable data in a machine readable format. What you do with this data and it's legallity are entirely your responsibility.

### Installation
#### Using pip
Assuming you have pip installed, just run the following command on the terminal
```
pip install vlawyer
```
#### Manually
Clone the repository
```
git clone https://github.com/hoenchioma/vlawyer.git
```
Then install the package
```
cd vlawyer
python setup.py install
```

### Usage
Available functions:
```
FUNCTIONS
    get_vjudge_data(username: str = '', 
                    oj_id: str = 'All', 
                    problem_no: str = '', 
                    language: str = '', 
                    result: str = 0, 
                    contest_id: str = '', 
                    limit: int = 0)
        Function to return vjudge based on parameters
        
        Parameters:
        username (str): username to search (empty -> all usernames)
        oj_id (str): online judge
            options: All, CodeForces, CodeChef, Gym, LightOJ, UVA, UVALive, 
                     Kattis, AtCoder, SPOJ, TopCoder, etc.
            (ignored if contest_id is specified)
        problem_no (str): problem number (can be found from a problem url in vjudge)
            (if contest id is specified, problem_no is A, B, C, etc. of contest)
        language (str): language of submission
            options: C, CPP, JAVA, PASCAL, PYTHON, CSHARP, RUBY, OTHER (empty -> all)
        result (int): result of submission
            options:
            0 -> All
            1 -> Accepted
            2 -> Presentation Error
            3 -> Wrong Answer
            4 -> Time Limit Exceed
            5 -> Memory Limit Exceed
            6 -> Output Limit Exceed
            7 -> Runtime Error
            8 -> Compile Error
            9 -> Unknown Error
            10 -> Submit Error
            11 -> Queuing && Judging
        contest_id (str): contest id (empty -> no particular contest)
        limit (int): maximum number of returned entries (0 -> no limit)
        
        Returns:
            list: list of dictionaries containing the entries
```
Example:
```python
import vlawyer
import json

# prints the latest 10 submissions from vjudge.net
# converted to json for better readability
print(json.dumps(vlawyer.get_vjudge_data(limit=10), indent=4, sort_keys=True)) 

# prints the submissions by xxx in contest no yyy
# replace xxx with actual username and yyy with an actual contest (otherwise you'll get an error)
print(json.dumps(vlawyer.get_vjudge_data(username='xxx', contest_id='yyy'), indent=4, sort_keys=True))

response = vlawyer.get_vjudge_data(limit=12)
print(len(response)) # get length of response (12)
print(type(response)) # get the type of response (dict)
```
