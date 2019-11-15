test = {
  'name': 'q4c',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> list(design_matrix(test).sum())[10:15]
          [290.0, 511.0, 699.0, 687.0, 683.0]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 250 <= linear_rmse <= 260
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(linear_rmse, 255.19147, 1e-4)
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
