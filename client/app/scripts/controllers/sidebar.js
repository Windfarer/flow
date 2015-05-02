'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:NavbarCtrl
 * @description
 * # NavbarCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('SidebarCtrl', function ($scope, $location, restAPI) {
    $scope.projects = restAPI.projects.query();
    $scope.editProject = function (project) {
      $location.path('/project/'+project.id)
    };
    $scope.goToProject = function (project) {
      $location.path('/task/project/'+project.id)
    };
    $scope.goToPersonal = function () {
      $location.path('/task')
    };
    $scope.createProject = function () {
      $location.path("/project/new");
    };

  });
