#!/usr/bin/env ruby

class Params

  def initialize(arg1, arg2, op)
    @arg1 = arg1
    @arg2 = arg2
    @operation = op
  end

  def setArg1(arg)
    @arg1 = arg
  end

  def setArg2(arg)
    @arg2 = arg
  end

  def setOperation(op)
    @operation = op
  end

  def to_json
    {:arg1 => @arg1, :arg2 => @arg2, :operation => @operation}.to_json
  end
end