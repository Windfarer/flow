'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:LandingCtrl
 * @description
 * # LandingCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('LandingCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
