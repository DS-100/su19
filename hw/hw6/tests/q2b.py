test = {
  'name': 'q2b',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sum(training_data['Fireplace_Qu'] == 'No Fireplace') # Make sure you've replaced all the missing values with 'No Fireplace'
          975
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(training_data.loc[:, 'Fireplace_Qu'].isnull() == 0) # Make sure you haven't introduced anything strange
          1998
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(training_data.loc[:, 'Fireplace_Qu'] == 'Excellent')
          30
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
