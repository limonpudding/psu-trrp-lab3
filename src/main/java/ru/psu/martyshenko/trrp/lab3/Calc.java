package ru.psu.martyshenko.trrp.lab3;

import ru.psu.martyshenko.trrp.lab3.entity.Answer;
import ru.psu.martyshenko.trrp.lab3.entity.Params;

public class Calc {

    public static Answer calculate(Params params) {
        Answer answer = new Answer();
        switch (params.getOperation()) {
            case ADD:
                answer.setResult(params.getArg1()+params.getArg2());
                break;
            case SUB:
                answer.setResult(params.getArg1()-params.getArg2());
                break;
            case MUL:
                answer.setResult(params.getArg1()*params.getArg2());
                break;
            case DIV:
                answer.setResult(params.getArg1()/params.getArg2());
                break;
            default:
                break;
        }
        return answer;
    }
}
