test = {   'name': 'q3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> training_data.shape[0] # '
                                               'Make sure that two '
                                               'observations were removed\n'
                                               '1998',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Make sure that the max '
                                               'Gr_Liv_Area is now below '
                                               '5000;\n'
                                               '>>> '
                                               "max(training_data['Gr_Liv_Area']) "
                                               '< 5000\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Make sure that '
                                               "remove_outliers doesn't mutate "
                                               'its input;\n'
                                               '>>> '
                                               'remove_outliers(training_data, '
                                               "'Gr_Liv_Area', "
                                               'upper=2000).shape == '
                                               'training_data.shape\n'
                                               'False',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Make sure that the sum '
                                               "of Gr_Liv_Area values hasn't "
                                               'been altered somehow;\n'
                                               '>>> '
                                               "sum(training_data['Gr_Liv_Area'])\n"
                                               '2980752',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
