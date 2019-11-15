test = {   'name': 'q3a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> res_q3a.shape\n(5, 3)',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all(res_q3a == '
                                               "res_q3a.sort_values('count', "
                                               'ascending=False))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "print(sorted(res_q3a['total_amount'].unique()))\n"
                                               '[316019, 492567, 499659, '
                                               '6989835, 25099091]\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
