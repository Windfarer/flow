'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:TaskCtrl
 * @description
 * # TaskCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('TaskCtrl', function($scope, $routeParams, restAPI, $timeout, $q) {
    $scope.item_limit = 10;

    var project_id = $routeParams.project_id;
    console.log(project_id);
    if (project_id) {
      $scope.project = restAPI.projects.get({project_id: project_id});
    }

    $scope.tasks =  restAPI.tasks.query({project:project_id});
    $scope.task = new restAPI.tasks();
    $scope.task_status = 0;

    //$scope.tasks = {
    //  inbox: restAPI.tasks.query({status:0, project:project_id}),
    //  doing: restAPI.tasks.query({status:1, project:project_id}),
    //  done: restAPI.tasks.query({status:2, project:project_id})
    //};

    $scope.updateTask = function (task) {
      console.log(task);
      task.$update();
    };
    $scope.deleteTask = function (task) {
      task.$delete();
    };
    $scope.submitTask = function () {
        console.log($scope.task);
        $scope.task.$save({project:project_id})
          .then(function(data) {
            if (project_id){
              $scope.task = new restAPI.tasks({project:project_id});
            }
            else {
              $scope.task = new restAPI.tasks();
            }
            $scope.tasks.push(data);
          })

    };

    $scope.addSubTask = function (task) {
      if (!task.sub_tasks){
        task.sub_tasks = [];
      }
      task.sub_tasks.push({title:task.newsubtask.title, status:0, deleted:0});
      task.newsubtask.title = "";
    };
    $scope.deleteSubTask = function (index, task) {
      console.log("remove",index);
      task.sub_tasks[index].deleted = 1;
    };

    var createFilterFor = function (query) {
      var lowercaseQuery = angular.lowercase(query);

      return function filterFn(contact) {
        console.log(contact);
        return (contact.nickname.indexOf(lowercaseQuery) != -1);
      };
    };
    $scope.querySearch = function (query) {
      var results = query ? $scope.project.members.filter(createFilterFor(query)) : [];
      console.log(results);
      return results;
    };

  })
.filter('dateFilter', function() {
    return function (task) {
      console.log(task);
      task.deadline = new Date(task[0].deadline*1000);
      return task
    }
  });
