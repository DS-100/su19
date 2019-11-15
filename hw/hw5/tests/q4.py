test = {   'name': 'q4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> not '
                                               "training_data['TotalBathrooms'].isnull().any() "
                                               '# Check that missing values '
                                               'are dealt with\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "training_data['TotalBathrooms'].sum() "
                                               '# Check that the values are as '
                                               'expected\n'
                                               '4421.5',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "list(training_data.loc[training_data['PID'] "
                                               '== 903230120, '
                                               "'TotalBathrooms'])\n"
                                               '[1.0]',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sum(training_data.loc[:, '
                                               "'TotalBathrooms'] < 2.5)\n"
                                               '1124',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
