test = {
  'name': 'q3b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(l2(linear_model(revised_analytical_thetas, one_hot_X_revised), tips).mean(), 1.03328557, rtol=1)
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
