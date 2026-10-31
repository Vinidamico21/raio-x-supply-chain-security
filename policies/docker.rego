package main

deny contains msg if {
    not has_non_root_user
    msg := "SECURITY: Dockerfile deve declarar um usuario nao privilegiado."
}

deny contains msg if {
    some instruction in input
    instruction.Cmd == "user"
    lower(instruction.Value[0]) == "root"

    msg := "SECURITY: execucao como root nao permitida."
}

has_non_root_user if {
    some instruction in input
    instruction.Cmd == "user"
    lower(instruction.Value[0]) != "root"
}