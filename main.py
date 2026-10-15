# candidate verification system
from pyscript import display, document


def candidate(e):
    document.getElementById('output').innerHTML = ''
    glee = ['Cady Bower', 'Alexa Salcedo', 'Nicole Alverez', 'Lia Galang', 'Clara Sabanal']

    first_name = document.getElementById('firstName').value
    last_name = document.getElementById('lastName').value

    glee_member = first_name + ' ' + last_name

    offical = glee_member in glee

    display_accepted = (f'Sorry, you are not included in Glee Club 26-27', f'Congratulations {glee_member}, you are part of Glee Club 26-27')

    display(display_accepted[offical], target='output')