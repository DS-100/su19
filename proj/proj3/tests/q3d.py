test = {
  'name': 'q3d',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(s[0], 0.02514825, 1e-3)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> train.shape
          (53680, 16)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> test.shape
          (13421, 16)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(train['region'][:8])
          [1, 1, 0, 1, 2, 1, 1, 0]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(test['region'][:8])
          [2, 1, 2, 0, 1, 0, 1, 2]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(train[train['region']==1]['duration'])
          11666210
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(test[test['region']==1]['duration'])
          2897696
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
