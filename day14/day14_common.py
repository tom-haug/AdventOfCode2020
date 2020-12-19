import os
import re
import sys
from enum import Enum
from typing import Callable


class MaskBits(Enum):
    PASS_THROUGH = 'X'
    FLOATING = 'Z'
    ZERO = '0'
    ONE = '1'


class MemoryBank:
    def __init__(self, mask_len):
        self.memory_addresses = {}
        # default value and address mask are all 'unchanged' bits
        self.value_mask = MaskBits.PASS_THROUGH.value * mask_len
        self.address_masks = [MaskBits.PASS_THROUGH.value * mask_len]

    def set_value_mask(self, value_mask: str):
        self.value_mask = value_mask

    def set_address_mask(self, input_address_mask: str):
        # address mask the X is actually a floating bit
        working_mask = input_address_mask.replace(MaskBits.PASS_THROUGH.value, MaskBits.FLOATING.value)
        # address mask the 0 is actually a pass-though
        working_mask = working_mask.replace(MaskBits.ZERO.value, MaskBits.PASS_THROUGH.value)
        self.address_masks = self.split_mask_next_floating_bit(working_mask)

    @staticmethod
    def get_masked_value(mask: str, input_value: int):
        # 1 means we always want a 1 in this position, create mask to OR with the value
        set_mask_str = ''.join([MaskBits.ONE.value if item == MaskBits.ONE.value else MaskBits.ZERO.value for item in mask])
        set_mask = int(set_mask_str, 2)

        # 0 means we always want a 0 in this position, create mask to AND with the value
        un_set_mask_str = ''.join([MaskBits.ZERO.value if item == MaskBits.ZERO.value else MaskBits.ONE.value for item in mask])
        un_set_mask = int(un_set_mask_str, 2)

        output_value = (input_value | set_mask) & un_set_mask
        return output_value

    def set_memory_value(self, address: int, value: int):
        value = self.get_masked_value(self.value_mask, value)

        for address_mask in self.address_masks:
            cur_address = self.get_masked_value(address_mask, address)
            self.memory_addresses[cur_address] = value

    def memory_address_sum(self):
        return sum([self.memory_addresses[key] for key in self.memory_addresses])

    def split_mask_next_floating_bit(self, input_mask: str) -> list[str]:
        first_floating_idx = input_mask.find(MaskBits.FLOATING.value)

        # if no more floating bits are found, we are done searching
        if first_floating_idx == -1:
            return [input_mask]

        # get the mask with the floating bit replaced with both a ONE and a ZERO
        first_child_mask = input_mask[:first_floating_idx] + MaskBits.ZERO.value + input_mask[first_floating_idx + 1:]
        second_child_mask = input_mask[:first_floating_idx] + MaskBits.ONE.value + input_mask[first_floating_idx + 1:]

        # recurse to replace other floating bits
        first_child_mask_list = self.split_mask_next_floating_bit(first_child_mask)
        second_child_mask_list = self.split_mask_next_floating_bit(second_child_mask)

        return first_child_mask_list + second_child_mask_list


def process_instructions_from_file(file_name: str, set_mask_fn: Callable[[str], None],
                                   set_value_fn: Callable[[int, int], None]):
    file_path = os.path.join(sys.path[0], file_name)
    f = open(file_path, "r")
    input = f.read().splitlines()
    f.close()

    for line in input:
        parts = line.split(' = ')
        if parts[0] == 'mask':
            set_mask_fn(parts[1])
        else:
            match = re.search('\\d+', parts[0])
            memory_address = int(match[0])
            store_value = int(parts[1])
            set_value_fn(memory_address, store_value)
