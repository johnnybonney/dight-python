"""Assignment 1."""

from sg_pl_pairs import pairs


def pluralize(sg):
    """Return list of plural form(s) of input_word.

    Building this function is the purpose of Assignment 1.
    The most basic case is already provided.
    """
    plurals = []
    if sg in ['auto', 'kangaroo', 'kilo', 'memo', 'photo', 'piano', 'pimento',
              'pro', 'solo', 'soprano', 'studio', 'tattoo', 'video', 'zoo']:
        plurals.append(sg + 's')
    elif sg in ['buffalo', 'cargo', 'halo', 'mosquito', 'motto', 'no',
                'tornado', 'volcano', 'zero']:
        plurals.append(sg + 's')
        plurals.append(sg + 'es')
    elif sg in ['fish', 'sheep', 'barracks']:
        plurals.append(sg)
    elif sg in ['axis', 'basis', 'crisis', 'diagnosis', 'emphasis', 'analysis',
                'hypothesis', 'neurosis', 'oasis', 'parenthesis', 'synopsis',
                'thesis']:
        plurals.append(sg[:-2] + 'es')
    elif sg in ['cactus', 'focus', 'fungus', 'nucleus', 'radius', 'stimulus',
                'syllabus', 'terminus']:
        plurals.append(sg[:-2] + 'i')
    elif sg in ['criterion', 'phenomenon', 'automaton']:
        plurals.append(sg[:-2] + 'a')
    elif sg in ['foot', 'tooth', 'goose']:
        plurals.append(sg.replace('oo', 'ee'))
    elif sg in ['woman', 'man']:
        plurals.append(sg.replace('a', 'e'))
    elif sg in ['amoeba', 'antenna', 'formula', 'larva', 'nebula', 'vertebra']:
        plurals.append(sg + 's')
        plurals.append(sg + 'e')
    elif sg in ['news', 'gymnastics', 'economics', 'mathematics', 'statistics',
                'luggage', 'baggage', 'furniture', 'information']:
        plurals.append('')
    elif sg[-2:] == 'is':
        plurals.append(sg[:-3] + 'es')
    elif sg[-1] in ['x', 'o', 's'] or sg[-2:] in ['ch', 'sh']:
        plurals.append(sg + 'es')
    elif sg[-1] == 'y':
        if sg[-2] in ['a', 'e', 'i', 'o', 'u']:
            plurals.append(sg + 's')
        else:
            plurals.append(sg[:-1] + 'ies')
    elif sg[-1] == 'f':
        plurals.append(sg[:-1] + 'ves')
    elif sg[-2:] == 'fe':
        plurals.append(sg[:-2] + 'ves')
    else:
        plurals.append(sg + 's')
    return plurals


def evaluate(pl_func=pluralize, pair_data=pairs):
    """Evaluate the performance of pluralize function based on pairs data.

    pl_func -- function that pluralizes input word (default=pluralize)
    pair_data -- list of 2-tuples: [(sg1, pl1), (sg2, pl2),...] (default=pairs)
    """
    total = len(pair_data)
    # Determine how many lexemes have more than one plural form.
    # duplicates = len(set([i for i, j in pair_data]))
    correct = 0
    for sg, pl in pair_data:
        predicted_pl = pl_func(sg)
        if pl == predicted_pl or pl in predicted_pl:
            correct += 1
            print('correct:', sg, predicted_pl, '({})'.format(pl), sep='\t')
        else:
            print('INcorrect:', sg, predicted_pl, '({})'.format(pl), sep='\t')
    print('Your score:', correct, '/', total, '{:.2%}'.format(correct / total))


evaluate()
