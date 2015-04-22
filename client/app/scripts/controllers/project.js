'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:GroupCtrl
 * @description
 * # GroupCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('ProjectCtrl', function ($scope) {
    $scope.groups = [{
      avatar : '/images/60.jpeg',
      name: 'Brunch this weekend?'
    }, {
      avatar : '/images/60.jpeg',
      name: 'Brunch this weekend?'
    }, {
      avatar : '/images/60.jpeg',
      name: 'Brunch this weekend?'
    }, {
      avatar : '/images/60.jpeg',
      name: 'Brunch this weekend?'
    }, {
      avatar : '/images/60.jpeg',
      name: 'Brunch this weekend?'
    }];
  });
