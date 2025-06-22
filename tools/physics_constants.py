from typing import Optional, Dict, Any


# Physics constants database
PHYSICS_CONSTANTS = {
    "planck constant": {"value": "6.62607015e-34", "unit": "J·s", "description": "Fundamental constant relating energy and frequency."},
    "boltzmann constant": {"value": "1.380649e-23", "unit": "J/K", "description": "Relates average kinetic energy to temperature."},
    "avogadro number": {"value": "6.02214076e23", "unit": "1/mol", "description": "Number of particles in a mole."},
    "gravitational constant": {"value": "6.67430e-11", "unit": "m³/kg·s²", "description": "Newtonian constant of gravitation."},
    "coulomb constant": {"value": "8.9875517923e9", "unit": "N·m²/C²", "description": "Electrostatic force constant."},
    "elementary charge": {"value": "1.602176634e-19", "unit": "C", "description": "Charge of a proton."},
    "electron mass": {"value": "9.10938356e-31", "unit": "kg", "description": "Rest mass of an electron."},
    "proton mass": {"value": "1.67262192369e-27", "unit": "kg", "description": "Rest mass of a proton."},
    "neutron mass": {"value": "1.67492749804e-27", "unit": "kg", "description": "Rest mass of a neutron."},
    "speed of light": {"value": "299792458", "unit": "m/s", "description": "Speed of light in vacuum."},
    "universal gas constant": {"value": "8.314462618", "unit": "J/(mol·K)", "description": "Gas constant in ideal gas law."},
    "faraday constant": {"value": "96485.33212", "unit": "C/mol", "description": "Electric charge per mole of electrons."},
    "vacuum permittivity": {"value": "8.854187817e-12", "unit": "F/m", "description": "Permittivity of free space."},
    "vacuum permeability": {"value": "1.25663706212e-6", "unit": "N/A²", "description": "Permeability of free space."},
    "fine structure constant": {"value": "7.2973525693e-3", "unit": "(dimensionless)", "description": "Characterizes strength of electromagnetic interaction."},
    "bohr radius": {"value": "5.29177210903e-11", "unit": "m", "description": "Most probable distance from nucleus to electron in hydrogen atom."}
}


def get_physics_constant(name: str):
    key = name.lower().strip()
    if key in PHYSICS_CONSTANTS:
        return PHYSICS_CONSTANTS[key]
    for k in PHYSICS_CONSTANTS:
        if key in k:
            return PHYSICS_CONSTANTS[k]
    return None


def list_available_constants() -> list:
    """
    Get a list of all available physics constants.
    
    Returns:
        List of constant names
    """
    return list(PHYSICS_CONSTANTS.keys())


def search_constants(search_term: str) -> list:
    """
    Search for constants containing the search term.
    
    Args:
        search_term: Term to search for in constant names
        
    Returns:
        List of matching constant names
    """
    search_term = search_term.lower()
    matches = []
    
    for constant_name in PHYSICS_CONSTANTS.keys():
        if search_term in constant_name:
            matches.append(constant_name)
    
    return matches


# Example usage and testing
if __name__ == "__main__":
    # Test retrieving constants
    test_constants = [
        "planck constant",
        "speed of light",
        "gravitational constant",
        "nonexistent constant"
    ]
    
    for constant in test_constants:
        result = get_physics_constant(constant)
        if result:
            print(f"{constant}: {result['value']} {result['unit']}")
            print(f"  Description: {result['description']}")
        else:
            print(f"{constant}: Not found")
    
    print("\nAvailable constants:")
    print(list_available_constants())
    
    print("\nSearching for 'mass':")
    print(search_constants("mass")) 