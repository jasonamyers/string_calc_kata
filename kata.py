import re
class string_calculator:
    @classmethod
    def add(cls, values):
        if values == '':
            return 0
        delimiter_list = []
        if values.startswith('//'):
            lines = values.splitlines()
            delimiter = lines[0].strip('/')
            if delimiter.startswith('['):
                dirty_delimiter_list = delimiter.split(']')
                delimiter_list = [x.strip('[]') for x in dirty_delimiter_list]
            else:
                delimiter_list = [delimiter]
            values = lines[1]
        else:
            delimiter_list.append(',')
        delimiter_exp = '|'.join(map(re.escape, delimiter_list))
        values_list = re.split(delimiter_exp, values)
        if len(values_list) == 1:
            if int(values_list[0]) >= 0:
                return int(values_list[0])
            else:
                raise ValueError('negatives not allowed')
        else:
            total = 0
            for value in values_list:
                if int(value) < 0:
                    raise ValueError('negatives not allowed')
                if int(value) > 1000:
                    continue
                total += int(value)
            return total
