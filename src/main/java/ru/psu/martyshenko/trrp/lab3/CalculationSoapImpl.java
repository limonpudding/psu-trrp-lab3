package ru.psu.martyshenko.trrp.lab3;

import ru.psu.martyshenko.trrp.lab3.wsdl.Answer;
import ru.psu.martyshenko.trrp.lab3.wsdl.CalculationSoap;
import ru.psu.martyshenko.trrp.lab3.wsdl.Params;

import javax.jws.WebService;

@WebService(
        endpointInterface = "ru.psu.martyshenko.trrp.lab3.wsdl.CalculationSoap",
        targetNamespace = "http://localhost:8080/")
public class CalculationSoapImpl implements CalculationSoap {

    public Answer calculate(Params params) {
        System.out.println("----------------------------------------");
        System.out.println("Новый запрос с параметрами:");
        System.out.print("  Операнд 1: ");
        System.out.println(params.getArg1());
        System.out.print("  Операнд 2: ");
        System.out.println(params.getArg2());
        System.out.print("  Операция: ");
        System.out.println(params.getOperation());
        Answer answer = new Answer();
        int result = 0;
        switch (params.getOperation()) {
            case ADD:
                result = params.getArg1() + params.getArg2();
                break;
            case SUB:
                result = params.getArg1() - params.getArg2();
                break;
            case MUL:
                result = params.getArg1() * params.getArg2();
                break;
            case DIV:
                result = params.getArg1() / params.getArg2();
                break;
            default:
                break;
        }
        answer.setResult(result);
        System.out.print("  Ответ: ");
        System.out.println(result);
        System.out.println("----------------------------------------");
        return answer;
    }
}
