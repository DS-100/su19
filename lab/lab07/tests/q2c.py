test = {   'name': 'q2c',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> abs_loss(2, 1)\n1',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> abs_loss(-2, 1)\n3',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> abs_loss(1, -3)\n4',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.linalg.norm(abs_loss(np.array([1,2]), '
                                               'np.array([-3,3])) - '
                                               'np.array([4, 1]), ord=1)\n'
                                               '0.0',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
