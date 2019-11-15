test = {   'name': 'q3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> y = data['tip'];\n"
                                               ">>> x = data['total_bill'];\n"
                                               '>>> '
                                               'np.isclose(minimize_average_loss(squared_loss, '
                                               'model, x, y), '
                                               '0.14373189123158361)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> y = data['tip'];\n"
                                               ">>> x = data['total_bill'];\n"
                                               '>>> '
                                               'np.isclose(minimize_average_loss(abs_loss, '
                                               'model, x, y), '
                                               '0.1495886219625012)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.isclose(minimize_average_loss(squared_loss, '
                                               "model, data['total_bill'], "
                                               "data['tip']), "
                                               '0.14373189229218733)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.isclose(minimize_average_loss(squared_loss, '
                                               "model, data['total_bill'], "
                                               "data['tip']), "
                                               '0.14373189229218733)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
