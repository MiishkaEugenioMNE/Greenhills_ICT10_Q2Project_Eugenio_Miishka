
from pyscript import display, document


# =========================================
# ELEMENT CHECKER
# =========================================

def elementchecker(e):

    document.getElementById('output').innerHTML = ''

    elements = {
        'H': {
            'Symbol': 'H',
            'Element': 'Hydrogen',
            'Atomic Number': 1,
            'Atomic Mass': 1.008
        },
        'C': {
            'Symbol': 'C',
            'Element': 'Carbon',
            'Atomic Number': 6,
            'Atomic Mass': 12.011
        },
        'N': {
            'Symbol': 'N',
            'Element': 'Nitrogen',
            'Atomic Number': 7,
            'Atomic Mass': 14.007
        },
        'O': {
            'Symbol': 'O',
            'Element': 'Oxygen',
            'Atomic Number': 8,
            'Atomic Mass': 15.999
        },
        'P': {
            'Symbol': 'P',
            'Element': 'Phosphorus',
            'Atomic Number': 15,
            'Atomic Mass': 30.974
        },
        'S': {
            'Symbol': 'S',
            'Element': 'Sulfur',
            'Atomic Number': 16,
            'Atomic Mass': 32.06
        },
        'Se': {
            'Symbol': 'Se',
            'Element': 'Selenium',
            'Atomic Number': 34,
            'Atomic Mass': 78.971
        },
        'F': {
            'Symbol': 'F',
            'Element': 'Fluorine',
            'Atomic Number': 9,
            'Atomic Mass': 18.998
        },
        'Cl': {
            'Symbol': 'Cl',
            'Element': 'Chlorine',
            'Atomic Number': 17,
            'Atomic Mass': 35.45
        },
        'Br': {
            'Symbol': 'Br',
            'Element': 'Bromine',
            'Atomic Number': 35,
            'Atomic Mass': 79.904
        },
        'I': {
            'Symbol': 'I',
            'Element': 'Iodine',
            'Atomic Number': 53,
            'Atomic Mass': 126.904
        },
        'At': {
            'Symbol': 'At',
            'Element': 'Astatine',
            'Atomic Number': 85,
            'Atomic Mass': 210
        },
        'Ts': {
            'Symbol': 'Ts',
            'Element': 'Tennessine',
            'Atomic Number': 117,
            'Atomic Mass': 294
        },
        'He': {
            'Symbol': 'He',
            'Element': 'Helium',
            'Atomic Number': 2,
            'Atomic Mass': 4.003
        },
        'Ne': {
            'Symbol': 'Ne',
            'Element': 'Neon',
            'Atomic Number': 10,
            'Atomic Mass': 20.180
        },
        'Ar': {
            'Symbol': 'Ar',
            'Element': 'Argon',
            'Atomic Number': 18,
            'Atomic Mass': 39.948
        },
        'Kr': {
            'Symbol': 'Kr',
            'Element': 'Krypton',
            'Atomic Number': 36,
            'Atomic Mass': 83.798
        },
        'Xe': {
            'Symbol': 'Xe',
            'Element': 'Xenon',
            'Atomic Number': 54,
            'Atomic Mass': 131.293
        },
        'Rn': {
            'Symbol': 'Rn',
            'Element': 'Radon',
            'Atomic Number': 86,
            'Atomic Mass': 222
        }
    }

    elementsymbol = document.getElementById('element_symbol').value.strip()

    # Allow lowercase input as well
    elementsymbol = elementsymbol.capitalize()

    element = elements.get(elementsymbol, {
        'Symbol': 'N/A',
        'Element': 'Element not found',
        'Atomic Number': 'N/A',
        'Atomic Mass': 'N/A'
    })

    display(element, target='output')


# =========================================
# HOMEPAGE / CANDIDATE VERIFICATION
# =========================================

def student_club(e):

    document.getElementById('output').innerHTML = ''

    student_fname = document.getElementById('student_firstname').value.strip()
    student_lname = document.getElementById('student_lastname').value.strip()

    chiikawa_members = [
        'Chiikawa Dela Cruz',
        'Usagi Santos',
        'Hachiware Bautista',
        'Momonga Garcia',
        'Rakko Ramos',
        'Kurimanju Fernandez',
        'Shisa Castillo'
    ]

    full_name = student_fname + ' ' + student_lname

    if not student_fname or not student_lname:
        message = 'Please enter both your first name and last name.'

    elif full_name in chiikawa_members:
        message = f'Congratulations, {full_name}! You are part of the Chiikawa club.'

    else:
        message = 'Sorry, your name is not on the list.'

    display(message, target='output')


# =========================================
# SCHOOL CLUB MEMBERS
# =========================================

club7 = {'Chiikawa Dela Cruz', 'Usagi Santos'}
club8 = {'Hachiware Bautista', 'Momonga Garcia'}
club9 = {'Rakko Ramos', 'Kurimanju Fernandez'}
club10 = {'Shisa Castillo', 'Furuhonya Gonzales'}

club_members = club7 | club8 | club9 | club10


def student_members(e):

    document.getElementById('output').innerHTML = ''

    student_fname = document.getElementById('student_firstname').value.strip()
    student_lname = document.getElementById('student_lastname').value.strip()

    if not student_fname or not student_lname:
        display('Please enter both your first name and last name.', target='output')
        return

    full_name = student_fname + ' ' + student_lname

    if full_name in club_members:
        message = f'{full_name} is already a club member.'

    else:
        club_members.add(full_name)
        message = f'{full_name} has been successfully added to the club!'

    display_len = len(club_members)

    display(
        f'{message}\n\n'
        f'Here is the updated list of club members: {sorted(club_members)}. '
        f'The total number of members is: {display_len}',
        target='output'
    )
