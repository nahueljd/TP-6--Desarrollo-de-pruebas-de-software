Feature: Resta de dos números
  Como usuario
  Quiero restar dos números
  Para obtener la diferencia correcta

  Scenario: Restar dos números positivos
    Given que tengo los números 2 y 1
    When los resto
    Then el resultado debería ser 1

  Scenario: Restar un número positivo y uno negativo
    Given que tengo los números 1 y -1
    When los resto
    Then el resultado debería ser 2

  Scenario: Restar dos números negativos
    Given que tengo los números -1 y -1
    When los resto
    Then el resultado debería ser 0
