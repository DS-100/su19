test = {   'name': 'q5a2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> def count_null_sol(s):\n'
                                               '...     return '
                                               'len(s[s.isnull()]);\n'
                                               '>>> \n'
                                               '>>> bus_sf_sol = '
                                               "bus[bus['postal_code_5'].isin(sf_dense_zip)];\n"
                                               '>>> '
                                               'num_missing_in_each_zip_sol = '
                                               'bus_sf_sol[\'longitude\'].groupby(bus_sf_sol["postal_code_5"]).agg(count_null_sol).sort_values(ascending '
                                               '= False);\n'
                                               '>>> \n'
                                               '>>> '
                                               'sorted(num_missing_in_each_zip_sol.index) '
                                               '== sorted(sf_dense_zip)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
