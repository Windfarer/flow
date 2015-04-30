'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:GroupCtrl
 * @description
 * # GroupCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('ProjectCtrl', function ($scope,$routeParams ,restAPI) {
    $scope.isNew = $routeParams === 'new';
    if ($scope.isNew) {
      $scope.project = new restAPI.projects();
    }
    else {
      $scope.project = restAPI.projects.get({'project_id':$routeParams.get("project_id")})
    }
    $scope.saveProject = function() {
      if ($scope.isNew) {
        $scope.project.save()
      }
      else {
        $scope.project.update()
      }
    };
  });
