test = {   'name': 'q10',
    'points': 15,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'isinstance(test_predictions, '
                                               'np.ndarray) # must be ndarray '
                                               'of predictions\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.unique(test_predictions) # '
                                               'must be binary labels (0 or 1) '
                                               'and not probabilities\n'
                                               'array([0, 1])',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> test_predictions.shape # '
                                               'must be the right number of '
                                               'predictions\n'
                                               '(1000,)',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
