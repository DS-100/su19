test = {
  'name': 'q1b',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> clean_taxi.shape
          (96445, 9)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(clean_taxi['duration'])
          74383078
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
