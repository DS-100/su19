test = {
  'name': 'q2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> expected_l1 = np.array([0.1021857, 0.08590592, 0.1181548, 0.28102618, 0.13510419, 0.2640767, 
          ...                         -0.0567563, 0.20579663, -0.03585098, 0.28599161, 0.17696859, 0.22221226]);
          >>> 
          >>> actual_l1 = np.array(minimize_average_loss(l1, linear_model, one_hot_X, tips));
          >>> np.isclose(one_hot_X @ expected_l1, one_hot_X @ actual_l1, rtol=0.1).all()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> expected_l2 = np.array([0.094487, 0.1759912, 0.18411085, 0.21655235, 0.15712761, 0.24353555, 
          ...                         0.01519972, 0.17746092, 0.05600946, 0.15199343, 0.23440129, 0.1662616]);
          >>> actual_l2 = np.array(minimize_average_loss(l2, linear_model, one_hot_X, tips));
          >>> np.isclose(one_hot_X @ expected_l2, one_hot_X @ actual_l2, rtol=0.001).all()
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
