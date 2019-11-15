test = {
  'name': 'q1b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> linear_model(np.arange(1,5), np.arange(1,5))
          30
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> (linear_model(2*np.eye(100), np.ones(100)) == 2*np.ones(100)).all()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> test_theta = np.array([[1, 2], [3, 4], [5, 6]]);
          >>> test_x = np.array([[1, 3, 5], [2, 4, 6]]);
          >>> expected = np.array([[35, 44], [44, 56]]);
          >>> actual = linear_model(test_theta, test_x);
          >>> np.array_equal(actual, expected)
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
