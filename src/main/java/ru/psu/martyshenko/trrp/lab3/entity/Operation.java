package ru.psu.martyshenko.trrp.lab3.entity;

public enum Operation {
    ADD("add"),
    MUL("mul"),
    DIV("div"),
    SUB("sub");

    private String description;

    Operation(String description) {
    }

    public String getDescription() {
        return description;
    }
}
