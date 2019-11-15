test = {
  'name': 'q4g',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 240 <= tree_rmse <= 245
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 225 <= tree_speed_rmse <= 240
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
