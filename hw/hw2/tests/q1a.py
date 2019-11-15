test = {
  'name': 'q1a',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(bike, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bike['holiday'].dtype == np.dtype('O')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(bike['holiday'].iloc[370:375]) == ['no', 'no', 'yes', 'yes', 'yes']
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bike['weekday'].dtype == np.dtype('O')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bike['workingday'].dtype == np.dtype('O')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bike['weathersit'].dtype == np.dtype('O')
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
