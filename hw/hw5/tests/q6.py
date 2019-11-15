test = {   'name': 'q6',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> train.shape == (1600, 82) '
                                               '# train should contain 80% of '
                                               'the data\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> test.shape == (400, 82) # '
                                               'test should contain 20% of the '
                                               'data\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.intersect1d(train_indices, '
                                               'test_indices).size # make sure '
                                               'train_indices and test_indices '
                                               'have no overlap\n'
                                               '0',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "np.intersect1d(train['PID'], "
                                               "test['PID']).size # make sure "
                                               'train and test have no '
                                               'overlapping houses\n'
                                               '0',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> sum(train['SalePrice']) # "
                                               "If this doesn't match, you "
                                               'might have still answered the '
                                               'question, but please adjust '
                                               'your code so that your split '
                                               'matches ours by following the '
                                               'implementation instructions '
                                               'about using shuffled_indices '
                                               'to split the data.\n'
                                               '287346111',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> sum(test['SalePrice']) # "
                                               "If this doesn't match, you "
                                               'might have still answered the '
                                               'question, but please adjust '
                                               'your code so that your split '
                                               'matches ours by following the '
                                               'implementation instructions '
                                               'about using shuffled_indices '
                                               'to split the data.\n'
                                               '74205684',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
