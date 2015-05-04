'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('MainCtrl', function ($scope, Auth, $location) {
    $scope.showComponent = function () {
      return Auth.isLoggedIn();
    };
    $scope.goToUserProfile = function () {
      $location.path('/user')
    };
    $scope.logout = function () {
      Auth.logout();
      $location.path("/landing");
    };
  });
