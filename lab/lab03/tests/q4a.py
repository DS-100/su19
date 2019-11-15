test = {
  'name': 'q4a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import matplotlib ;
          >>> np.alltrue(np.array([l.get_text() for l in ax_4a.xaxis.get_ticklabels()]) == days)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bars = [rect.get_height() for rect in ax_4a.get_children() 
          ...         if isinstance(rect, matplotlib.patches.Rectangle) and rect.get_x() != 0.0
          ...        ];
          >>> np.alltrue(np.array(bars)[4:] == [1, 1, 2])
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
