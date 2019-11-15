test = {
  'name': 'q3b',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 180220 <= y_fitted.mean() <= 180225
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 181492 <= y_predicted.mean() <= 181512
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
