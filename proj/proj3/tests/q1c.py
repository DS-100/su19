test = {
  'name': 'q1c',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> manhattan_taxi.shape
          (82800, 9)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(manhattan_taxi['duration'])
          54551565
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> manhattan_taxi.iloc[0,:]['duration']
          981
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
