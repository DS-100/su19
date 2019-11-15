test = {   'name': 'q2a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> iris_mean.size\n4',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.all(np.isclose(iris_mean, '
                                               'np.array([5.84333333, 3.054, '
                                               '3.75866667, 1.19866667])))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.all(np.isclose(np.zeros(4), '
                                               'np.mean(normalized_features, '
                                               'axis=0))) # make sure data is '
                                               'centered at 0\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> -0.31 < '
                                               'np.sum(normalized_features[0]) '
                                               '< -0.28 # make sure scaling '
                                               'was done correctly\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
