test = {
  'name': 'q3b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(ts_decay) == len(loss_decay) == 20 # theta history and loss history are 20 items in them
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ts_decay[0].shape == (2,) # theta history contains theta values
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isscalar(loss[0]) # loss history should be a list of values, not vector
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> loss_decay[1] - loss_decay[-1] > 0 # loss is decreasing
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(np.sum(t_est_decay), 4.5, atol=2e-1)  # theta_est should be close to our value
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
