test = {
  'name': 'q1a',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all_taxi.shape
          (97692, 9)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(all_taxi['duration'])
          90553549
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
