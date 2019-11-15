test = {   'name': 'q2b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> bootstrap_parallel_time < '
                                               'bootstrap_serial_time # Try '
                                               'restart and run all cells '
                                               'above if this fails\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.isclose(boot_sample_means_parallel.mean(), '
                                               'boot_sample_means_serial.mean(), '
                                               'rtol=1)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
