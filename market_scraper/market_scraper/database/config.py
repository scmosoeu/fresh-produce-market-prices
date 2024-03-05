from configparser import ConfigParser


def load_config(filename: str = 'database.ini', section: str = 'postgresql') -> dict:
    """
    Read configuration data from the database.ini

    Parameters
    -----------
    filename: .ini filename where postgresql details are
        stored
    section: section within the .ini file where the details
        are stored 
    """

    parser = ConfigParser()
    parser.read(filename)

    # Get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]

    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return config
