test = {
  'name': 'q6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 'Hour' in calls.columns
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(calls["Hour"]) == set(range(24))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(calls["Hour"][:5]) == [22, 21, 20, 8, 13]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(calls['Hour'].mean(), 13.35823)
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
