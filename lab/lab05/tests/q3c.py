test = {   'name': 'q3c',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> res_q3c.shape\n(5, 2)',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all(res_q3c == '
                                               "res_q3c.sort_values('cand_name', "
                                               'ascending=False))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> print(sorted(map(str, '
                                               "res_q3c['cmte_nm'].unique())))\n"
                                               "['CITIZENS TO ELECT DANIEL P "
                                               "ZUTLER FOR PRESIDENT', 'JOE "
                                               "ZUCCOLO FOR CONGRESS', 'None', "
                                               "'ZUKOWSKI FOR CONGRESS', "
                                               "'ZUMWALT FOR CONGRESS']\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
