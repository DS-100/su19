test = {
  'name': 'q2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(answer2, list)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all([isinstance(elt, str) for elt in answer2])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all([elt in calls['CVLEGEND'].values for elt in answer2])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(answer2) == set(['LARCENY', 'BURGLARY - VEHICLE', 'VANDALISM', 'DISORDERLY CONDUCT', 'ASSAULT'])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
