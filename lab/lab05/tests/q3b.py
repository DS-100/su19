test = {   'name': 'q3b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> res_q3b.shape\n(5, 2)',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all(res_q3b == '
                                               "res_q3b.sort_values('cand_name', "
                                               'ascending=False))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "print(sorted(res_q3b['cmte_nm'].unique()))\n"
                                               "['CITIZENS TO ELECT DANIEL P "
                                               "ZUTLER FOR PRESIDENT', "
                                               "'CONSTITUTIONAL COMMITTEE', "
                                               "'JOE ZUCCOLO FOR CONGRESS', "
                                               "'ZUKOWSKI FOR CONGRESS', "
                                               "'ZUMWALT FOR CONGRESS']\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
