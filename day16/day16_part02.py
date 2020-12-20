from day16_common import TicketPropertyDefinition, load_property_definitions_and_tickets_from_file, Ticket, \
    load_property_positions, filter_valid_tickets, filter_definition_description


def product_of_property_positions(property_definitions: list[TicketPropertyDefinition], ticket: Ticket) -> int:
    result = 1
    for cur_property in property_definitions:
        property_position = cur_property.position_on_ticket
        result *= ticket.property_values[property_position]
    return result


def get_complete_property_definitions_and_your_ticket(file_name: str) -> (list[TicketPropertyDefinition], Ticket):
    property_definitions, your_ticket, nearby_tickets = load_property_definitions_and_tickets_from_file(file_name)

    valid_tickets = filter_valid_tickets(nearby_tickets, property_definitions)

    valid_tickets.append(your_ticket)

    load_property_positions(property_definitions, valid_tickets)

    return property_definitions, your_ticket


if __name__ == "__main__":
    file_name = 'input.txt'

    property_definitions, your_ticket = get_complete_property_definitions_and_your_ticket(file_name)

    result_properties_to_report = filter_definition_description(property_definitions, 'departure')
    result = product_of_property_positions(result_properties_to_report, your_ticket)

    print('result', result)
