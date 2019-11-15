test = {
  'name': 'q2a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(missing_counts, pd.Series)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> missing_counts.size # Should have 84 total features (82 features + TotalBathrooms + in_rich_neighborhood)
          84
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(missing_counts.index.values) == set(training_data.columns.values)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> missing_counts.loc['Fireplace_Qu'] # Make sure you are calculating the counts correctly
          975
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> missing_counts.iloc[0] # Make sure you are sorting correctly
          1991
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
