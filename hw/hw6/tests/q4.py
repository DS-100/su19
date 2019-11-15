test = {
  'name': 'q4',
  'points': 6,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def rmse(predicted, actual):
          ...     return np.sqrt(np.mean((actual - predicted)**2));
          >>> 
          >>> training_data = pd.read_csv('ames_train_cleaned.csv');
          >>> X_train, y_train = process_data_fm(training_data);
          >>> 
          >>> final_model.fit(X_train, y_train);
          >>> y_predicted_train = final_model.predict(X_train);
          >>> training_rmse = rmse(y_predicted_train, y_train);
          >>> 
          >>> training_rmse <= 40000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def rmse(predicted, actual):
          ...     return np.sqrt(np.mean((actual - predicted)**2));
          >>> 
          >>> training_data = pd.read_csv('ames_train_cleaned.csv');
          >>> X_train, y_train = process_data_fm(training_data);
          >>> 
          >>> final_model.fit(X_train, y_train);
          >>> y_predicted_train = final_model.predict(X_train);
          >>> training_rmse = rmse(y_predicted_train, y_train);
          >>> 
          >>> training_rmse <= 38000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def rmse(predicted, actual):
          ...     return np.sqrt(np.mean((actual - predicted)**2));
          >>> 
          >>> training_data = pd.read_csv('ames_train_cleaned.csv');
          >>> X_train, y_train = process_data_fm(training_data);
          >>> 
          >>> final_model.fit(X_train, y_train);
          >>> y_predicted_train = final_model.predict(X_train);
          >>> training_rmse = rmse(y_predicted_train, y_train);
          >>> 
          >>> training_rmse <= 36000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def rmse(predicted, actual):
          ...     return np.sqrt(np.mean((actual - predicted)**2));
          >>> 
          >>> training_data = pd.read_csv('ames_train_cleaned.csv');
          >>> test_data = pd.read_csv('ames_test_cleaned.csv');
          >>> 
          >>> X_train, y_train = process_data_fm(training_data);
          >>> X_test, y_test = process_data_fm(test_data);
          >>> 
          >>> X_test_public, y_test_public = X_test[::2], y_test[::2];
          >>> X_test_private, y_test_private = X_test[1::2], y_test[1::2];
          >>> 
          >>> final_model.fit(X_train, y_train);
          >>> y_predicted_train = final_model.predict(X_train);
          >>> y_predicted_test_public = final_model.predict(X_test_public);
          >>> y_predicted_test_private = final_model.predict(X_test_private);
          >>> 
          >>> training_rmse = rmse(y_predicted_train, y_train);
          >>> public_test_rmse = rmse(y_predicted_test_public, y_test_public);
          >>> private_test_rmse = rmse(y_predicted_test_private, y_test_private);
          >>> 
          >>> public_test_rmse <= 43000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def rmse(predicted, actual):
          ...     return np.sqrt(np.mean((actual - predicted)**2));
          >>> 
          >>> training_data = pd.read_csv('ames_train_cleaned.csv');
          >>> test_data = pd.read_csv('ames_test_cleaned.csv');
          >>> 
          >>> X_train, y_train = process_data_fm(training_data);
          >>> X_test, y_test = process_data_fm(test_data);
          >>> 
          >>> X_test_public, y_test_public = X_test[::2], y_test[::2];
          >>> X_test_private, y_test_private = X_test[1::2], y_test[1::2];
          >>> 
          >>> final_model.fit(X_train, y_train);
          >>> y_predicted_train = final_model.predict(X_train);
          >>> y_predicted_test_public = final_model.predict(X_test_public);
          >>> y_predicted_test_private = final_model.predict(X_test_private);
          >>> 
          >>> training_rmse = rmse(y_predicted_train, y_train);
          >>> public_test_rmse = rmse(y_predicted_test_public, y_test_public);
          >>> private_test_rmse = rmse(y_predicted_test_private, y_test_private);
          >>> 
          >>> public_test_rmse <= 40000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def rmse(predicted, actual):
          ...     return np.sqrt(np.mean((actual - predicted)**2));
          >>> 
          >>> training_data = pd.read_csv('ames_train_cleaned.csv');
          >>> test_data = pd.read_csv('ames_test_cleaned.csv');
          >>> 
          >>> X_train, y_train = process_data_fm(training_data);
          >>> X_test, y_test = process_data_fm(test_data);
          >>> 
          >>> X_test_public, y_test_public = X_test[::2], y_test[::2];
          >>> X_test_private, y_test_private = X_test[1::2], y_test[1::2];
          >>> 
          >>> final_model.fit(X_train, y_train);
          >>> y_predicted_train = final_model.predict(X_train);
          >>> y_predicted_test_public = final_model.predict(X_test_public);
          >>> y_predicted_test_private = final_model.predict(X_test_private);
          >>> 
          >>> training_rmse = rmse(y_predicted_train, y_train);
          >>> public_test_rmse = rmse(y_predicted_test_public, y_test_public);
          >>> private_test_rmse = rmse(y_predicted_test_private, y_test_private);
          >>> 
          >>> public_test_rmse <= 37000
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
