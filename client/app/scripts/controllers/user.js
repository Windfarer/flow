'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:UserCtrl
 * @description
 * # UserCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('UserCtrl', function ($scope, restAPI) {
    $scope.user = restAPI.user.get();

    $scope.saveUser = function() {
      $scope.project.update()
    }
  });
