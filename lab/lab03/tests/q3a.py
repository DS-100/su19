test = {
  'name': 'q3a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> set(calls["Day"]) == {'Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday'}
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(calls["Day"][:5]) == ['Wednesday', 'Wednesday', 'Friday', 'Tuesday', 'Saturday']
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
