'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:UserCtrl
 * @description
 * # UserCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('UserCtrl', function ($scope, restAPI, Auth) {
    $scope.user = restAPI.user.get({user_id:Auth.getId()});

    $scope.saveUser = function() {
      $scope.user.$update()
    };
    $scope.deleteUser = function() {
      $scope.user.$delete();
    };
  });
