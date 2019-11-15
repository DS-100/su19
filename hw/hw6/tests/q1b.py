test = {
  'name': 'q1b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(find_rich_neighborhoods(training_data, 5, np.median))
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(rich_neighborhoods, list)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all([isinstance(neighborhood, str) for neighborhood in rich_neighborhoods])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(rich_neighborhoods) == set(['StoneBr', 'NridgHt', 'NoRidge']) # Check to see if correct neighborhoods identified
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(find_rich_neighborhoods(training_data, 2, np.min)) == set(['GrnHill', 'NoRidge'])
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
