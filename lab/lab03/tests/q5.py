test = {
  'name': 'q5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import matplotlib ;
          >>> np.alltrue(np.array([l.get_text() for l in ax_5.xaxis.get_ticklabels()]) == days)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import matplotlib ;
          >>> bars = [rect.get_height() for rect in ax_5.get_children() 
          ...         if isinstance(rect, matplotlib.patches.Rectangle) and rect.get_x() != 0.0
          ...        ];
          >>> np.alltrue(np.array(bars) == np.array([27, 32, 29, 33, 35, 40, 12]))
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
