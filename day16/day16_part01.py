import os
import sys
import re

REQUIREMENTS_REGEX = r'^([\w\s]+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)$'
TICKET_REGEX = r'\d+'


class TicketRequirement:
    def __init__(self, description: str, from_value: int, to_value: int):
        self.description = description
        self.from_value = from_value
        self.to_value = to_value

    def property_meets_requirement(self, property_value: int):
        return self.from_value <= property_value <= self.to_value


class Ticket:
    def __init__(self, property_values: list[int]):
        self.property_values = property_values

    def invalid_property_values(self, requirements: list[TicketRequirement]):
        invalid_values: list[int] = []
        for property_value in self.property_values:
            satisfied_requirements = [requirement for requirement in requirements
                                      if requirement.property_meets_requirement(property_value)]
            if not any(satisfied_requirements):
                invalid_values.append(property_value)

        return invalid_values

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

    requirement_matches = re.findall(REQUIREMENTS_REGEX, requirement_section, re.MULTILINE)
    ticket_requirements: list[TicketRequirement] = []
    for match in requirement_matches:
        first_requirement = TicketRequirement(match[0], int(match[1]), int(match[2]))
        second_requirement = TicketRequirement(match[0], int(match[3]), int(match[4]))
        ticket_requirements.append(first_requirement)
        ticket_requirements.append(second_requirement)

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

    invalid_values_on_nearby_tickets: list[int] = []
    for nearby_ticket in nearby_tickets:
        invalid_values_on_nearby_tickets += nearby_ticket.invalid_property_values(ticket_requirements)

    invalid_value_sum = sum(invalid_values_on_nearby_tickets)
    print('invalid_value_sum', invalid_value_sum)
