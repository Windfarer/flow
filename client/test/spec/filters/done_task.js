'use strict';

describe('Filter: doneTask', function () {

  // load the filter's module
  beforeEach(module('flowApp'));

  // initialize a new instance of the filter before each test
  var doneTask;
  beforeEach(inject(function ($filter) {
    doneTask = $filter('doneTask');
  }));

  it('should return the input prefixed with "doneTask filter:"', function () {
    var text = 'angularjs';
    expect(doneTask(text)).toBe('doneTask filter: ' + text);
  });

});
