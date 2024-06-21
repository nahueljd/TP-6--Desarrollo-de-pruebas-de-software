from behave import given, when, then
from app.suma import suma

@given('que tengo los números {num1:d} y {num2:d}')
def step_given_tengo_los_numeros(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('los sumo')
def step_when_los_sumo(context):
    context.result = suma(context.num1, context.num2)

@then('el resultado debería ser {expected:d}')
def step_then_el_resultado_deberia_ser(context, expected):
    assert context.result == expected
