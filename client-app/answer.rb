#!/usr/bin/env ruby

require 'json'

class Answer
  @result = 0

  def initialize(ans)
    @result = JSON.parse(ans)['result']
  end

  def getResult
    return @result
  end
end