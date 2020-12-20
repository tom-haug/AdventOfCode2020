import os
import sys
import re
from typing import Optional

REQUIREMENTS_REGEX = r'^([\w\s]+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)$'
TICKET_REGEX = r'\d+'


class TicketRequirement:
    def __init__(self, from_value: int, to_value: int):
        self.from_value = from_value
        self.to_value = to_value
        self.from_value = from_value
        self.to_value = to_value

    def property_meets_requirement(self, property_value: int) -> bool:
        return self.from_value <= property_value <= self.to_value


class TicketPropertyDefinition:
    def __init__(self, description: str, from_value_1: int, to_value_1: int, from_value_2: int, to_value_2: int):
        self.description = description
        self.requirements = [TicketRequirement(from_value_1, to_value_1)] + [TicketRequirement(from_value_2, to_value_2)]
        self.position_on_ticket: Optional[int] = None

    def property_meets_requirement(self, property_value: int) -> bool:
        any_requirements_met = any([True if requirement.property_meets_requirement(property_value) else False for
                                    requirement in self.requirements])
        return any_requirements_met


class Ticket:
    def __init__(self, property_values: list[int]):
        self.property_values = property_values

    def all_invalid_property_values(self, property_definitions: list[TicketPropertyDefinition]) -> list[int]:
        invalid_values: list[int] = []
        for property_value in self.property_values:
            satisfied_requirements = [property_definition for property_definition in property_definitions
                                      if property_definition.property_meets_requirement(property_value)]
            if not any(satisfied_requirements):
                invalid_values.append(property_value)

        return invalid_values


def deduce_next_property_position(all_property_definitions: list[TicketPropertyDefinition], tickets: list[Ticket]) -> bool:
    unassigned_property_definitions = [property_definition for property_definition in all_property_definitions
                                       if property_definition.position_on_ticket is None]
    total_property_positions = list(range(len(tickets[0].property_values)))
    taken_property_positions = [definition.position_on_ticket for definition in all_property_definitions if definition.position_on_ticket is not None]
    remaining_property_positions = [property_position for property_position in total_property_positions if not property_position in taken_property_positions]

    if len(unassigned_property_definitions) == 1 and len(remaining_property_positions) == 1:
        unassigned_property_definitions[0].position_on_ticket = remaining_property_positions[0]
        return False


    for check_property_definition in unassigned_property_definitions:
        potential_positions_on_ticket: list[int] = []
        for check_property_position in remaining_property_positions:
            all_tickets_meet_property_position_requirement = True
            for ticket in tickets:
                check_property_value = ticket.property_values[check_property_position]
                if not check_property_definition.property_meets_requirement(check_property_value):
                    all_tickets_meet_property_position_requirement = False
                    break
            if all_tickets_meet_property_position_requirement:
                potential_positions_on_ticket.append(check_property_position)
        if len(potential_positions_on_ticket) == 1:
            check_property_definition.position_on_ticket = potential_positions_on_ticket[0]
            return True

    return False


if __name__ == "__main__":
    file_name = 'input.txt'
    file_path = os.path.join(sys.path[0], file_name)
    f = open(file_path, "r")
    input = f.read()
    f.close()

    sections = input.split('\n\n')
    requirement_section = sections[0]
    your_ticket_section = sections[1]
    nearby_ticket_section = sections[2]

    property_matches = re.findall(REQUIREMENTS_REGEX, requirement_section, re.MULTILINE)
    property_definitions: list[TicketPropertyDefinition] = []
    for match in property_matches:
        ticket_property = TicketPropertyDefinition(match[0], int(match[1]), int(match[2]), int(match[3]), int(match[4]))
        property_definitions.append(ticket_property)

    your_ticket_matches = re.findall(TICKET_REGEX, your_ticket_section, re.MULTILINE)
    ticket_values = [int(match) for match in your_ticket_matches]
    your_ticket = Ticket(ticket_values)

    nearby_ticket_lines = nearby_ticket_section.splitlines()
    nearby_tickets: list[Ticket] = []
    for nearby_ticket_line in nearby_ticket_lines:
        nearby_ticket_matches = re.findall(TICKET_REGEX, nearby_ticket_line)
        if any(nearby_ticket_matches):
            ticket_values = [int(match) for match in nearby_ticket_matches]
            nearby_tickets.append(Ticket(ticket_values))

    valid_tickets: list[Ticket] = []
    for nearby_ticket in nearby_tickets:
        invalid_values_on_nearby_tickets = nearby_ticket.all_invalid_property_values(property_definitions)
        if not any(invalid_values_on_nearby_tickets):
            valid_tickets.append(nearby_ticket)

    print('len(nearby_tickets)', len(nearby_tickets))
    print('len(valid_tickets)', len(valid_tickets))

    valid_tickets.append(your_ticket)

    keep_going = True
    while keep_going:
        keep_going = deduce_next_property_position(property_definitions, valid_tickets)

    for property_definition in property_definitions:
        print(f'{property_definition.description}, position: {property_definition.position_on_ticket}')


    result_properties_to_report = [property_definition for property_definition in property_definitions if 'departure' in property_definition.description]

    result = 1
    for cur_property in result_properties_to_report:
        property_position = cur_property.position_on_ticket
        result *= your_ticket.property_values[property_position]

    print('result', result)
