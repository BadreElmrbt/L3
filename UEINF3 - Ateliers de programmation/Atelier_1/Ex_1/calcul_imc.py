#Question 1
def message_imc(imc:float)->str:
    imc_messages = {
        (0, 16.5): "dénutrition ou famine",
        (16.5, 18.5): "maigreur",
        (18.5, 25): "corpulence normale",
        (25, 30): "surpoids",
        (30, 35): "obésité modérée",
        (35, 40): "obésité sévère",
        (40, float('inf')): "obésité morbide"
    }
    
    for imc_range, message in imc_messages.items():
        if imc_range[0] <= imc < imc_range[1]:
            return message

#Question 2
def test_message_imc():
    print("Réponse attendue : dénutrition ou famine -----> " + message_imc(15))
    print("Réponse attendue : corpulance normale -----> " + message_imc(24.75))
    print("Réponse attendue : obésité modérée -----> " + message_imc(31))
    print("Réponse attendue : obésité morbide -----> " + message_imc(78))

#Question 3
test_message_imc() 