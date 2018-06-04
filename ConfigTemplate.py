configtemplate = {

'General Setup': {
    'save_path': 'string',
    'input_features': ['string', 'string_list', 'Auto'],
    'target_feature': 'string',
    'grouping_feature': 'string',
    'labeling_features': ['string'],
},

'Data Setup': {
    'string': {'data_path': 'string'},
},

'Feature Normalization': {
    'normalize_x_features': 'bool',
    'normalize_y_feature': 'bool',
    'feature_normalization_type': ['standardize', 'normalize'],
    'feature_scale_min': 'float',
    'feature_scale_max': 'float',
},

'Feature Generation': {
    'perform_feature_generation': 'bool',
    'add_magpie_features': 'bool',
    'add_materialsproject_features': 'bool',
    'add_citrine_features': 'bool',
    'materialsproject_apikey': 'string',
    'citrine_apikey': 'string',
},

'Feature Selection': {
    'perform_feature_selection': 'bool',
    'remove_constant_features': 'bool',
    'feature_selection_algorithm': [
        'univariate_feature_selection',
        'recursive_feature_elimination',
        'sequential_forward_selection',
        'basic_forward_selection',
        ],
    'use_mutual_information':  'bool',
    'number_of_features_to_keep':  'integer',
    'scoring_metric':  [
        'mean_squared_error',
        'mean_absolute_error',
        'root_mean_squared_error',
        'r2_score',
    ],
    'generate_feature_learning_curve': 'bool',
    'model_to_use_for_learning_curve': [
        'linear_model_regressor',
        'linear_model_lasso_regressor',
        'lkrr_model_regressor',
        'gkrr_model_regressor',
        'support_vector_machine_model_regressor',
        'decision_tree_model_regressor',
        'extra_trees_model_regressor',
        'randomforest_model_regressor',
        'adaboost_model_regressor',
        'nn_model_regressor',
        'gaussianprocess_model_regressor',
    ],
},

 # TODO: 'Models and Tests to Run' duplicates items in 'Test Parameters' and 'Model Parameters'.
 #       So 'Models and Tests to Run' should be eliminated, and the things that use it should use
 #       the keys of 'Test Parameters' and 'Model Parameters' instead
'Models and Tests to Run' : {
    'models': [
        'linear_model_regressor',
        'linear_model_lasso_regressor',
        'lkrr_model_regressor',
        'gkrr_model_regressor',
        'dummy_model',
        'support_vector_machine_model_regressor',
        'decision_tree_model_regressor',
        'extra_trees_model_regressor',
        'randomforest_model_regressor',
        'adaboost_model_regressor',
        'nn_model_regressor',
        'gaussianprocess_model_regressor',
        'k_nearest_neighbors_classifier',
        'logistic_regression_model_classifier',
        'support_vector_machine_model_classifier',
        'decision_tree_model_classifier',
        'random_forest_model_classifier',
        'extra_trees_model_classifier',
    ],
    'test_cases': [
        'MultiClass',
        'SingleFit',
        'SingleFitPerGroup',
        'SingleFitGrouped',
        'KFoldCV',
        'LeaveOneOutCV',
        'LeaveOutPercentCV',
        'LeaveOutGroupCV',
        'PredictionVsFeature',
        'PlotNoAnalysis',
        'ParamGridSearch',
        'ParamOptGA',
    ],
},

'Test Parameters': {
    'MultiClass': {
        'training_dataset': 'string',
        'testing_dataset': 'string',
        'xlabel': 'string',
        'ylabel': 'string',
        'plot_filter_out': 'string',
    },
    'SingleFit': {
        'training_dataset': 'string',
        'testing_dataset': 'string',
        'xlabel': 'string',
        'ylabel': 'string',
        'plot_filter_out': 'string',
    },
    'SingleFitPerGroup': {
        'training_dataset': 'string',
        'testing_dataset': 'string',
        'xlabel': 'string',
        'ylabel': 'string',
        'plot_filter_out': 'string',
    },
    'SingleFitGrouped': {
        'training_dataset': 'string',
        'testing_dataset': 'string',
        'xlabel': 'string',
        'ylabel': 'string',
        'plot_filter_out': 'string',
    },
    'KFoldCV': {
        'training_dataset': 'string',
        'testing_dataset': 'string',
        'xlabel': 'string',
        'ylabel': 'string',
        'num_cvtests': 'integer',
        'mark_outlying_points': 'integer',
        'num_folds': 'integer',
    },
    'LeaveOneOutCV': {
        'training_dataset': 'string',
        'testing_dataset': 'string',
        'xlabel': 'string',
        'ylabel': 'string',
        'num_cvtests': 'integer',
        'mark_outlying_points': 'integer',
    },
    'LeaveOutPercentCV': {
        'training_dataset': 'string',
        'testing_dataset': 'string',
        'xlabel': 'string',
        'ylabel': 'string',
        'num_cvtests': 'integer',
        'mark_outlying_points': 'integer',
        'percent_leave_out': 'float',
    },
    'LeaveOutGroupCV': {
        'training_dataset': 'string',
        'testing_dataset': 'string',
        'xlabel': 'string',
        'ylabel': 'string',
        'num_cvtests': 'integer',
        'mark_outlying_points': 'integer',
    },
    'PredictionVsFeature': {
        'training_dataset': 'string',
        'testing_dataset': 'string',
        'xlabel': 'string',
        'ylabel': 'string',
        'feature_plot_feature': 'string',
        'plot_filter_out': 'string',
        'data_labels': 'string',
    },
    'PlotNoAnalysis': {
        'training_dataset': 'string',
        'testing_dataset': 'string',
        'xlabel': 'string',
        'ylabel': 'string',
        'feature_plot_feature': 'string',
        'plot_filter_out': 'string',
        'data_labels': 'string',
    },
    'ParamGridSearch': {
        'training_dataset': 'string',
        'testing_dataset': 'string',
        'xlabel': 'string',
        'ylabel': 'string',
        'training_dataset': 'string',
        'testing_dataset': 'string',
        'num_folds': 'integer',
        'num_cvtests': 'integer',
        'percent_leave_out': 'float',
        'pop_upper_limit': 'integer',
    },
    'ParamOptGA': {
        'training_dataset': 'string',
        'testing_dataset': 'string',
        'xlabel': 'string',
        'ylabel': 'string',
        'training_dataset': 'string',
        'testing_dataset': 'string',
        'num_folds': 'integer',
        'num_cvtests': 'integer',
        'percent_leave_out': 'float',
        'pop_upper_limit': 'integer',
    },
},

'Model Parameters': {
    'linear_model_regressor': {
        'fit_intercept': 'bool',
    },
    'linear_model_lasso_regressor': {
        'fit_intercept': 'bool',
        'alpha': 'float',
    },
    'lkrr_model_regressor': { # TODO (are these the right params?)
        'alpha': 'float',
        'gamma': 'float',
        'coef0': 'float',
        'degree': 'integer',
        'kernel': ['linear', 'cosine', 'polynomial', 'sigmoid', 'rbf', 'laplacian'],
    },
    'gkrr_model_regressor': {
        'alpha': 'float',
        'gamma': 'float',
        'coef0': 'float',
        'degree': 'integer',
        'kernel': ['linear', 'cosine', 'polynomial', 'sigmoid', 'rbf', 'laplacian'],
    },
    'dummy_model': {
    },
    'support_vector_machine_model_regressor': {
        'C': 'float',
        'gamma': 'float',
        'coef0': 'float',
        'degree': 'integer',
        'kernel': ['linear', 'cosine', 'polynomial', 'sigmoid', 'rbf', 'laplacian'],
    },
    'decision_tree_model_regressor': {
        'criterion': ['mae', 'mse', 'friedman_mse'],
        'splitter': ['random', 'best'],
        'max_depth': 'integer',
        'min_samples_leaf': 'integer',
        'min_samples_split': 'integer',
    },
    'extra_trees_model_regressor': {
        'criterion': ['mse', 'mae'],
        'n_estimators': 'integer',
        'max_depth': 'integer',
        'min_samples_leaf': 'integer',
        'min_samples_split': 'integer',
        'max_leaf_nodes': 'integer',
    },
    'randomforest_model_regressor': {
        'criterion': ['mse', 'mae'],
        'n_estimators': 'integer',
        'max_depth': 'integer',
        'min_samples_leaf': 'integer',
        'min_samples_split': 'integer',
        'max_leaf_nodes': 'integer',
        'n_jobs': 'integer',
        'warm_start': 'bool',
    },
    'adaboost_model_regressor': {
        'base_estimator_max_depth': 'integer',
        'n_estimators': 'integer',
        'learning_rate': 'float',
        'loss': ['linear' 'square', 'exponential'],
    },
    'nn_model_regressor': {
        'hidden_layer_sizes': 'tuple',
        'activation': ['identity', 'logistic', 'tanh', 'relu'],
        'solver': ['lbfgs', 'sgd', 'adam'],
        'alpha': 'float',
        'max_iterations': 'integer',
        'tolerance': 'float',
    },
    'gaussianprocess_model_regressor': {
        'kernel': ['rbf'],
        'RBF_length_scale': 'float',
        'RBF_length_scale_bounds': 'tuple',
        'alpha': 'float',
        'optimizer': ['fmin_l_bfgs_b'],
        'n_restarts_optimizer': 'integer',
        'normalize_y': 'bool',
    },
    'k_nearest_neighbors_classifier': {
    },
    'logistic_regression_model_classifier': {
    },
    'support_vector_machine_model_classifier': {
        'C': 'float',
        'kernel': 'string',
        'degree': 'integer',
        'gamma': 'float',
        'coef0': 'float',
    },
    'decision_tree_model_classifier': {
        'criterion': 'string',
        'splitter': 'string',
        'max_depth': 'integer',
        'min_samples_leaf': 'integer',
        'min_samples_split': 'integer',
    },
    'random_forest_model_classifier': {
        'criterion': 'string',
        'n_estimators': 'integer',
        'max_depth': 'integer',
        'min_samples_split': 'integer',
        'min_samples_leaf': 'integer',
        'max_leaf_nodes': 'integer',
    },
    'extra_trees_model_classifier': {
        'criterion': 'string',
        'n_estimators': 'integer',
        'max_depth': 'integer',
        'min_samples_split': 'integer',
        'min_samples_leaf': 'integer',
        'max_leaf_nodes': 'integer',
    },
},

}
