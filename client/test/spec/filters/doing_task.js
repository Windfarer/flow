'use strict';

describe('Filter: doingTask', function () {

  // load the filter's module
  beforeEach(module('flowApp'));

  // initialize a new instance of the filter before each test
  var doingTask;
  beforeEach(inject(function ($filter) {
    doingTask = $filter('doingTask');
  }));

  it('should return the input prefixed with "doingTask filter:"', function () {
    var text = 'angularjs';
    expect(doingTask(text)).toBe('doingTask filter: ' + text);
  });

});
