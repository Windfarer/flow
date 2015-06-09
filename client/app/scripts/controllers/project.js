'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:GroupCtrl
 * @description
 * # GroupCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('ProjectCtrl', function ($scope, $routeParams ,restAPI, $location) {
    $scope.isNew = $routeParams.project_id === 'new';
    if ($scope.isNew) {
      $scope.project = new restAPI.projects();
    }
    else {
      $scope.project = restAPI.projects.get({'project_id':$routeParams.project_id})
    }
    $scope.saveProject = function() {
      if ($scope.isNew) {
        console.log($scope.project);
        $scope.project.$save()
      }
      else {
        $scope.project.$update()
      }
    };
    $scope.deleteProject = function () {
      $scope.project.$delete();
      $location.path("/")
    };
    $scope.insertMemberEmail = function () {
      $scope.project.members.push({email:$scope.email});
      $scope.project.$update();
    };
    $scope.removeMember = function (index) {
      console.log("remove member",index);
      $scope.project.members.splice(index,1);
    };
  });
