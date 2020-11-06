#!/usr/bin/env ruby

require 'uri'
require 'net/http'
require 'json'
require_relative 'answer.rb'

def calculate(arg1, arg2, operation)
  uri = URI('http://localhost:8080/service')
  http = Net::HTTP.new(uri.host, uri.port)

  params = Params.new(arg1, arg2, operation)

  request = Net::HTTP::Post.new(uri.path, 'Content-Type' => 'application/json')
  request.body = params.to_json

  response = http.request(request)
  answer = Answer.new(response.body)
  answer.getResult
end