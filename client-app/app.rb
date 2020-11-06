#!/usr/bin/env ruby

require 'json'
require_relative 'params.rb'
require_relative 'calc.rb'
require_relative 'operation.rb'

def menu
  begin
    puts "Выберите операцию:"
    puts "1. Сложение"
    puts "2. Вычитание"
    puts "3. Умножение"
    puts "4. Деление"
    puts "0. Выход"
    option = gets().to_i
    case option
    when 1..4
      operation = ""
      case option
      when 1
        operation = Operation::ADD
      when 2
        operation = Operation::SUB
      when 3
        operation = Operation::MUL
      when 4
        operation = Operation::DIV
      end
      puts "Введите 1 операнд:"
      arg1 = gets().to_i
      puts "Введите 2 операнд:"
      arg2 = gets().to_i
      puts "Ответ:"
      puts calculate(arg1, arg2, operation)
    when 0
      break
    else
      puts "Неверный ввод"
    end
  end until option == 0
end

menu
