package ru.psu.martyshenko.trrp.lab3;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ru.psu.martyshenko.trrp.lab3.entity.Answer;
import ru.psu.martyshenko.trrp.lab3.entity.Params;

@RestController
@RequestMapping(value = "/service", produces = "application/json; charset=UTF-8")
public class MainController {

    @PostMapping
    public Answer calcSum(@RequestBody Params params) {
        return Calc.calculate(params);
    }
}
