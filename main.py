import argparse

import pdb, logging

logging.basicConfig(level=logging.DEBUG,
                    filename='logs.log',
                    filemode='w')

def main(arguments, options):
    for argument in arguments:
        recursion_times = int(argument)
        # initial input must be set manually to '1'
        number = "1"
        for i in xrange(1,recursion_times):
            number = say_number(str(number))
        print(number)

def say_number(number):
    """Takes 'number' input and reads it out in the look-and-say method."""
    number_block = ""
    output_number = ""

    for i,v in enumerate(number):
        number_block += v
        if ((i+1) >= len(number)) or not (number[i] == number[i+1]):
            #example: 111 will be expressed as '31', in other words 'three ones'
            block_expression = str(len(number_block)) + v
            output_number += block_expression
            logging.debug( """ End of Block. (number={n}, number_block={b},block_expression={e})
                          """.format( n=number,
                                      b=number_block,
                                      e=block_expression ))
            number_block = ""
        # Prevent overflow by pruning to 500 digits and breaking.
        if len(output_number)>=500:
            logging.info(""" Reached 500 digit limit. Length of output is: {l}
                          """.format( l= len(output_number )))
            output_number = output_number[0:500]
            break

    logging.debug( """ End of say_number. (output_number={o}, number={n})
                  """.format( o=output_number, n=number ))
    return output_number


parser = argparse.ArgumentParser(description='Write description here')
parser.add_argument('basic_arguments', nargs='*')

args = parser.parse_args()

main(args.basic_arguments, args)
