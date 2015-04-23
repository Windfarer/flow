'use strict';

describe('Service: taskFilterOption', function () {

  // load the service's module
  beforeEach(module('flowApp'));

  // instantiate service
  var taskFilterOption;
  beforeEach(inject(function (_taskFilterOption_) {
    taskFilterOption = _taskFilterOption_;
  }));

  it('should do something', function () {
    expect(!!taskFilterOption).toBe(true);
  });

});
