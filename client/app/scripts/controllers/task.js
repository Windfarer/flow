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
  .controller('TaskCtrl', function($scope, $mdDialog) {
    $scope.tasks=[
      {"title":"taksdfsddf",
      "finished":false},
      {"title":"taksdfsddf",
        "finished":true},
      {"title":"taksdfsddf",
        "finished":false}
    ]
  });
