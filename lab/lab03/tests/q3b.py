test = {
  'name': 'q3b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import matplotlib ;
          >>> np.alltrue(np.array([l.get_text() for l in ax_3b.xaxis.get_ticklabels()]) == days)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import matplotlib ;
          >>> bars = [rect.get_height() for rect in ax_3b.get_children() 
          ...         if isinstance(rect, matplotlib.patches.Rectangle) and rect.get_x() != 0.0
          ...        ];
          >>> np.alltrue(np.array(bars) == calls['Day'].value_counts()[days].values)
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
