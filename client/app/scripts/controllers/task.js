'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:TaskCtrl
 * @description
 * # TaskCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .config(function($mdIconProvider) {
    $mdIconProvider
      .iconSet('social', 'img/icons/sets/social-icons.svg', 24)
      .iconSet('device', 'img/icons/sets/device-icons.svg', 24)
      .iconSet('communication', 'img/icons/sets/communication-icons.svg', 24)
      .defaultIconSet('img/icons/sets/core-icons.svg', 24);
  })
  .controller('TaskCtrl', function($scope, restAPI) {
    $scope.task = new restAPI.tasks();
    $scope.tasks = restAPI.tasks.query();

    $scope.submitTask = function () {
      $scope.task.$save()
    };

  });
