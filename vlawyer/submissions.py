
import requests

# header for requesting data
_headers = {
    'authority': 'vjudge.net',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-dest': 'empty',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://vjudge.net',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://vjudge.net/status/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

# form data
_data = {
    'draw': '1',
    'columns[0][data]': '0',
    'columns[0][name]': '',
    'columns[0][searchable]': 'true',
    'columns[0][orderable]': 'false',
    'columns[0][search][value]': '',
    'columns[0][search][regex]': 'false',
    'columns[1][data]': '1',
    'columns[1][name]': '',
    'columns[1][searchable]': 'true',
    'columns[1][orderable]': 'false',
    'columns[1][search][value]': '',
    'columns[1][search][regex]': 'false',
    'columns[2][data]': '2',
    'columns[2][name]': '',
    'columns[2][searchable]': 'true',
    'columns[2][orderable]': 'false',
    'columns[2][search][value]': '',
    'columns[2][search][regex]': 'false',
    'columns[3][data]': '3',
    'columns[3][name]': '',
    'columns[3][searchable]': 'true',
    'columns[3][orderable]': 'false',
    'columns[3][search][value]': '',
    'columns[3][search][regex]': 'false',
    'columns[4][data]': '4',
    'columns[4][name]': '',
    'columns[4][searchable]': 'true',
    'columns[4][orderable]': 'false',
    'columns[4][search][value]': '',
    'columns[4][search][regex]': 'false',
    'columns[5][data]': '5',
    'columns[5][name]': '',
    'columns[5][searchable]': 'true',
    'columns[5][orderable]': 'false',
    'columns[5][search][value]': '',
    'columns[5][search][regex]': 'false',
    'columns[6][data]': '6',
    'columns[6][name]': '',
    'columns[6][searchable]': 'true',
    'columns[6][orderable]': 'false',
    'columns[6][search][value]': '',
    'columns[6][search][regex]': 'false',
    'columns[7][data]': '7',
    'columns[7][name]': '',
    'columns[7][searchable]': 'true',
    'columns[7][orderable]': 'false',
    'columns[7][search][value]': '',
    'columns[7][search][regex]': 'false',
    'columns[8][data]': '8',
    'columns[8][name]': '',
    'columns[8][searchable]': 'true',
    'columns[8][orderable]': 'false',
    'columns[8][search][value]': '',
    'columns[8][search][regex]': 'false',
    'columns[9][data]': '9',
    'columns[9][name]': '',
    'columns[9][searchable]': 'true',
    'columns[9][orderable]': 'false',
    'columns[9][search][value]': '',
    'columns[9][search][regex]': 'false',
    'start': 0,
    'length': 20,
    'search[value]': '',
    'search[regex]': 'false',
    'onlyFollowee': 'false',
    'orderBy': 'run_id'
}


def get_vjudge_data(username: str = '',
                    oj_id: str = 'All',
                    problem_no: str = '',
                    language: str = '',
                    result: str = 0,
                    contest_id: str = '',
                    limit: int = 0):
    """Function to return vjudge based on parameters

    Parameters:
    username (str): username to search (empty -> all usernames)
    oj_id (str): online judge
        options: All, CodeForces, CodeChef, Gym, LightOJ, UVA, UVALive, Kattis, AtCoder, SPOJ, TopCoder, etc.
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

    """

    # generate data
    query_data = {
        'start': 0,
        'length': 20,
        'un': username,
        'res': result,
        'language': language
    }
    
    # if contest_id is specified
    if contest_id:
        query_data['inContest'] = True
        query_data['contestId'] = contest_id
        query_data['num'] = problem_no if problem_no else '-'
    else:
        query_data['OJId'] = oj_id
        query_data['probNum'] = problem_no

    res = []
    # set limit to a very large integer if limit = 0
    limit = 2**63 if limit == 0 else limit
    length_per_query = min(limit, 20)  # max: 20
    query_data['start'] = 0
    query_data['length'] = length_per_query

    while len(res) < limit:
        response = requests.post(
            'https://vjudge.net/status/data/',
            headers=_headers,
            data={**_data, **query_data}
        )

        entries = response.json()['data']
        if entries:
            res += entries
        else:
            break # if no more responses break

        query_data['start'] += length_per_query

    return res[:limit]


def _main():
    import json
    from timeit import default_timer as timer
    
    # get the 1o most recent submissions from vjudge and measure the time
    start = timer()
    data = get_vjudge_data(limit=10)
    print(f"response time: {timer() - start} s")
    print(f"no. of entries: {len(data)}")
    
    # print output in json
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == "__main__":
    _main()
