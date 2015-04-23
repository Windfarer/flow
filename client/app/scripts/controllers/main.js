'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('MainCtrl', function ($scope ,Auth) {
    $scope.showComponent = function () {
      return Auth.isLoggedIn();
    };
  });
