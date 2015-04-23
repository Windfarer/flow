'use strict';

/**
 * @ngdoc service
 * @name flowApp.taskFilterOption
 * @description
 * # taskFilterOption
 * Factory in the flowApp.
 */
angular.module('flowApp')
  .service('taskFilterOption', function () {
    // Service logic
    // ...

    // Public API here
    return {
      done: false,
      doing: false
    };
  });
