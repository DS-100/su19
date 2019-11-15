test = {
  'name': 'q1a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> one_hot_X.shape
          (244, 12)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all([np.issubdtype(one_hot_X[column].dtype, np.number) for column in one_hot_X])
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
