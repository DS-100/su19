test = {
  'name': 'q3a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(l2(linear_model(analytical_thetas, one_hot_X),tips).mean(), 328.61824697, rtol=1) or np.isclose(l2(linear_model(analytical_thetas, one_hot_X), tips).mean(), 7566.07726721, rtol=1)
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
