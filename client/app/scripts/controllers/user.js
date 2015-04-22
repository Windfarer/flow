'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:UserCtrl
 * @description
 * # UserCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('UserCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
