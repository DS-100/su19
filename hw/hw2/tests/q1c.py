test = {
  'name': 'q1c',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.round(daily_counts['casual'].mean())
          848.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.round(daily_counts['casual'].var())
          471450.0
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
