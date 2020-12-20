from day16_common import load_property_definitions_and_tickets_from_file, get_invalid_property_count_on_tickets

if __name__ == "__main__":
    file_name = 'input.txt'

    property_definitions, your_ticket, nearby_tickets = load_property_definitions_and_tickets_from_file(file_name)

    invalid_value_sum = get_invalid_property_count_on_tickets(property_definitions, nearby_tickets)

    print('invalid_value_sum', invalid_value_sum)
