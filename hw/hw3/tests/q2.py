test = {   'name': 'q2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> from datetime import '
                                               'datetime;\n'
                                               '>>> ELEC_DATE = datetime(2016, '
                                               '11, 8);\n'
                                               '>>> INAUG_DATE = '
                                               'datetime(2017, 1, 20);\n'
                                               ">>> set(trump[(trump['time'] > "
                                               "ELEC_DATE) & (trump['time'] < "
                                               'INAUG_DATE) '
                                               "]['source'].unique()) == "
                                               "set(['Twitter Ads',\n"
                                               "...  'Twitter Web Client',\n"
                                               "...  'Twitter for Android',\n"
                                               "...  'Twitter for iPhone'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
