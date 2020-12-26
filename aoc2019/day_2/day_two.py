from day_2.day_two_data import memory_part_one, test_codes

opcode_parameters = {
    1: 3,
    2: 3,
    99: 0,
}


def set_1202_program_alarm(memory):
    print('set 1202 program alarm...')
    _set_noun(memory, 12)
    _set_verb(memory, 2)
    return memory


def _set_noun(memory, noun):
    memory[1] = noun


def _set_verb(memory, verb):
    memory[2] = verb


def get_noun_verb_code(noun, verb):
    return noun * 100 + verb


def process_memory(memory):
    instruction_pointer = 0
    while (instruction_pointer is not None):
        memory, instruction_pointer = _process_instruction(memory, instruction_pointer)

    # print('Result: {}'.format(memory))
    return memory


def _process_instruction(memory, instruction_pointer):
    opcode = memory[instruction_pointer + 0]
    if opcode not in (1, 2, 99):
        raise ValueError('Invalid opcode.')
    if opcode == 99:
        # halt and return memory
        return memory, None
    else:
        parameter_one_idx = memory[instruction_pointer + 1]
        parameter_one = memory[parameter_one_idx]

        parameter_two_idx = memory[instruction_pointer + 2]
        parameter_two = memory[parameter_two_idx]

        output_idx = memory[instruction_pointer + 3]

    if opcode == 1:
        # print('add')
        memory[output_idx] = parameter_one + parameter_two

    if opcode == 2:
        # print('multiply')
        memory[output_idx] = parameter_one * parameter_two

    return memory, (instruction_pointer + opcode_parameters[opcode] + 1)


def _test_sample_memorys():
    print('run tests...\n')
    for test_set in test_codes:
        print(test_set['code'])
        expected = test_set["solution"]
        res = process_memory(test_set['code'])
        if expected == res:
            print('✅ Test successful.')
        else:
            print('❌ Test not successful.')
            print('{} (expected {})'.format(res, expected))
        print('\n')


def search_noun_verb_code(target, initial_memory):
    for noun in range(100):
        for verb in range(100):
            memory = initial_memory.copy()
            _set_noun(memory, noun)
            _set_verb(memory, verb)

            try:
                res = process_memory(memory)
                # print(res[0])
                if target == res[0]:
                    return noun, verb
            except ValueError:
                continue
    return None


if __name__ == '__main__':
    print('start...\n')
    _test_sample_memorys()

    print('1️⃣ Part One')
    print('process memory...')
    memory = set_1202_program_alarm(memory_part_one.copy())
    # Part One Result: 5110675
    _ = process_memory(memory)

    print('\n')
    print('2️⃣ Part Two')
    target = 19690720
    res = search_noun_verb_code(target, memory_part_one.copy())
    if res is None:
        print('No Noun-Verb-Code found.')
        exit(1)

    noun_verb_code = get_noun_verb_code(*res)
    # Part Two Result: 4847
    print('Noun-Verb-Code: {}'.format(noun_verb_code))
