Feature: Cuadrado de un binomio
  Como usuario
  Quiero calcular el cuadrado de un binomio
  Para obtener el resultado correcto

  Scenario: Calcular el cuadrado de binomio con números positivos
    Given que tengo los números 2 y 3
    When calculo el cuadrado del binomio
    Then el resultado debería ser 25

  Scenario: Calcular el cuadrado de binomio con un número positivo y uno negativo
    Given que tengo los números -1 y 1
    When calculo el cuadrado del binomio
    Then el resultado debería ser 0

  Scenario: Calcular el cuadrado de binomio con ceros
    Given que tengo los números 0 y 0
    When calculo el cuadrado del binomio
    Then el resultado debería ser 0
